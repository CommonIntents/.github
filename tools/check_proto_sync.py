#!/usr/bin/env python3
"""跨器官 schema 副本的一致性断言 —— "之间"这一层唯一会被静默丢失的东西。

**为什么需要它。** 同一份 `.proto` 在两个器官各存一份，而在实测之前**没有任何东西
比对它们**。实测（2026-09-20）：两对跨器官副本的**注释都已漂移**，字段集侥幸没漂。
其中一对里有人写下了 "the two copies' comments have already drifted apart … the drift
is worth knowing about" —— 写下来了，但**没有任何机制会在他写错字段时叫醒他**。
写下与做到之间的那道缝，就是这个脚本要堵的。

**它断言什么。** 见 `proto_pairs.toml` 的表头：跨器官对断言**字段集**（去掉注释与空行后
逐字节相同），同仓的源→发布对断言**逐字节相同**。两类要求的不是同一种严格，
因为关系不是同一种关系。

**它不做什么。** 它不比 `.pyi`/生成物，不碰代码生成的接线，也不判断某个字段
*该不该*存在。它只回答一个问题：**同一份声明，两边的字段集是不是同一个。**

退出码：0 = 全部一致；1 = 有字段集漂移（**这是红的**）；2 = 检查器自身出错。
注释漂移只 WARN，**永不改退出码** —— 它是给人看的信息，不是判据。
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PAIRS = os.path.join(HERE, "proto_pairs.toml")


def strip_comments(text: str) -> str:
    """去注释、去行尾空白、去空行 —— 剩下的就是 wire 上真正存在的东西。

    只处理 `//`。块注释 `/* */` 在 .proto 里合法但本工作区一份都没用；
    若将来用了，**这里不会静默放过** —— 见 `assert_no_block_comments`。
    """
    out = []
    for line in text.split("\n"):
        line = re.sub(r"//.*$", "", line).rstrip()
        if line:
            out.append(line)
    return "\n".join(out)


def assert_no_block_comments(name: str, text: str) -> None:
    """块注释会让 `strip_comments` 的结果不再是字段集，而它不会报错 —— 于是断言会
    在错误的输入上安静地给出结论。宁可拒绝检查，也不给一个自信的错答案。"""
    if "/*" in text:
        raise SystemExit(
            f"CHECKER ERROR: {name} 含块注释，strip_comments 只懂 // —— "
            "在这种输入上给结论是错的，所以拒绝检查"
        )


def load_pairs(path: str) -> list[dict]:
    """极小的 TOML 读取：只有 [[pair]] 与 key = "value"，够用且不引依赖。"""
    pairs: list[dict] = []
    cur: dict | None = None
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line == "[[pair]]":
                cur = {}
                pairs.append(cur)
                continue
            m = re.match(r'^([A-Za-z_]+)\s*=\s*"(.*)"$', line)
            if m and cur is not None:
                cur[m.group(1)] = m.group(2)
    if not pairs:
        # 空表会让这个检查器"全部通过"而实际什么都没看 —— 那是最坏的一种绿。
        raise SystemExit(f"CHECKER ERROR: {path} 里没有任何 [[pair]]，检查器什么都没查")
    return pairs


def main() -> int:
    try:
        pairs = load_pairs(PAIRS)
    except OSError as e:
        print(f"CHECKER ERROR: 读不到 {PAIRS}: {e}", file=sys.stderr)
        return 2

    drift: list[str] = []
    warn: list[str] = []

    for p in pairs:
        name = p.get("name", "?")
        mode = p.get("mode", "")
        src = os.path.join(ROOT, p.get("source", ""))
        ven = os.path.join(ROOT, p.get("vendored", ""))
        if mode not in ("byte", "field-set"):
            print(f"CHECKER ERROR: {name} 的 mode={mode!r} 不认识", file=sys.stderr)
            return 2
        try:
            a = open(src, encoding="utf-8").read()
            b = open(ven, encoding="utf-8").read()
        except OSError as e:
            print(f"CHECKER ERROR: {name}: {e}", file=sys.stderr)
            return 2
        try:
            assert_no_block_comments(name, a)
            assert_no_block_comments(name, b)
        except SystemExit as e:
            print(e, file=sys.stderr)
            return 2

        if mode == "byte":
            if a != b:
                drift.append(f"{name}: 同仓两处不同（应逐字节一致）\n    {p['source']}\n    {p['vendored']}")
            continue

        # field-set：字段集是判据，注释漂移只是信息
        fa, fb = strip_comments(a), strip_comments(b)
        if fa != fb:
            drift.append(
                f"{name}: **字段集漂移** —— 这正是会在 wire 上静默丢失的东西\n"
                f"    源   {p['source']}\n    副本 {p['vendored']}"
            )
        elif a != b:
            warn.append(f"{name}: 注释已漂移（字段集相同，不影响 wire）")

    for w in warn:
        print(f"WARN  {w}")
    if drift:
        print(f"FAIL  {len(drift)} 对副本的字段集不一致：")
        for d in drift:
            print(f"    {d}")
        print("      修法：把**源**的字段改动同步到副本；不要用改副本的方式消红。")
        return 1

    print(f"OK    {len(pairs)} 对 schema 副本的判据全部成立（跨器官比字段集，同仓比逐字节）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
