# IP 防护清单（许可与知识产权）

> **目标**：所有仓的许可与 IP 防护做到位，且**交付可复验的证据，而非声明**。
> **判据**：`sha256` 与官方原文一致、覆盖表可复跑。**"看起来像 Apache" 不算达成。**
> **日期**：2026-09-20 ｜ **范围**：工作区 20 个 git 仓

---

## 0. 不要发明新形状 —— 本仓**已有**的 IP 框架（照它办）

| 对象 | 许可 | 既有出处 |
|---|---|---|
| **代码** | **Apache License 2.0**（含 §5 专利授权） | 各仓 `LICENSE` |
| **规范 / 文档** | **CC BY-ND 4.0**（署名 · **禁止演绎**） | 规范文档头部的 `> © <年> <版权人>. Licensed under CC BY-ND 4.0 …` |
| **贡献者条款** | 四条：有权授权 · 代码→Apache · 规范→CC BY-ND · 无需另签版权转让（永久/全球/不可撤销） | `BIND-19:CONTRIBUTING.md` 的 *Contributor Intellectual Property Terms* |
| **第三方归属** | NOTICE 里一段显式归属 + **明确免责**（"不含其代码或文本，全部原创，列出仅为归属与透明"） | `commonintents/.github:NOTICE` |

**⇒ 这套分工是对的**：代码可被商用/修改（Apache），**规范不可被改头换面**（CC BY-ND），
贡献进来的东西默认按这两条授权。**新仓照抄这套，不要另立一套。**

---

## 1. 现状（2026-09-20 实测，命令见 §4）

| 仓 | LICENSE | NOTICE | 带 CC BY-ND 的文档 |
|---|---|---|---|
| BIND-19 | ✅ Apache 2.0 逐字 | — | 5 |
| Cellrix | ✅ Apache 2.0 逐字（**2026-09-20 由 MIT 换证**） | — | 0 |
| FlowModus | ✅ Apache 2.0 逐字 | 有 | 1 |
| Helix-MCP-Learner | ✅ Apache 2.0 逐字（**2026-09-20 新增**） | — | 0 |
| HelixECO-Glove | ✅ Apache 2.0 逐字 | — | 0 |
| Tuck | ✅ Apache 2.0 逐字 | — | 0 |
| anaphase-helix | ✅ Apache 2.0 逐字 | — | 0 |
| commonintents/.github | ✅ Apache 2.0 逐字 | 有 | 2 |
| commonintents/BIND-19 | ✅ Apache 2.0 逐字 | — | 5 |
| commonintents/CAPABILITY-13 | ✅ Apache 2.0 逐字 | — | 3 |
| commonintents/INTENT-7 | ✅ Apache 2.0 逐字 | — | 3 |
| commonintents/INTENT-7-SECURE | ✅ Apache 2.0 逐字 | — | 3 |
| commonintents/PFP-xCF14 | ✅ Apache 2.0 逐字 | — | 1 |
| commonintents/SAP-xCF14 | ✅ Apache 2.0 逐字 | — | 1 |
| helix-mind | ✅ Apache 2.0 逐字 | — | 0 |
| helix-tentacle | ✅ Apache 2.0 逐字 | — | 0 |
| lodestone-md | ✅ Apache 2.0 逐字（**2026-09-20 由 MIT 换证**） | — | 0 |
| lodestone-spec | ✅ Apache 2.0 逐字 | — | 0 |
| lumtract | ✅ Apache 2.0 逐字 | 有 | 0 |
| phyt-DNA | ✅ Apache 2.0 逐字 | — | 1 |

**小计**：LICENSE 逐字 Apache 2.0 **20/20** ✅（2026-09-20 达成）。NOTICE 仍仅 **3/20**。
NOTICE 仅 **3/20**。

---

## 2. 三类缺口与处置顺序

### ✅ A. LICENSE 不是 Apache 2.0 或没有 —— **已关闭（2026-09-20）**

三个仓都先做了**第三方代码审计**，再动许可证。审计结论（判据：跟踪文件集，不是含构建产物的工作树）：

| 仓 | 换证前 | 跟踪文件 | 审计结论 | 处置 |
|---|---|---|---|---|
| `Cellrix` | MIT（sha 前 12 位 `5f471a6ed609`） | 209 | 作者全为你本人（非 fork）· 无外来版权头 · 依赖全宽松（serde/tokio/thiserror/wasm-bindgen…）· **无 GPL/AGPL** · 无 vendor · 无 submodule | 换 Apache 2.0 逐字 |
| `lodestone-md` | MIT（`aa787199e0c1`） | 37 | 作者全为你本人 · **零第三方依赖**（Cargo.toml `[dependencies]` 为空）· 有一个 submodule，**其自带 Apache 2.0，不冲突** | 换 Apache 2.0 逐字 |
| `Helix-MCP-Learner` | **无** | 30 | 10 个提交全为你本人 · 无外来版权头 · 依赖全宽松 · 无 vendor/submodule | **新增** Apache 2.0 逐字 |

**⇒ 三个仓都无第三方许可需要保留、也无第三方归属需要搬运。** 换证不触碰任何他人权利。

**旁证（`Helix-MCP-Learner` 的一个真缺陷）**：它的 README 顶部本就有 `License: Apache-2.0`
徽章并**链接到 `LICENSE`** —— 而那个文件**并不存在**。**这次加证让那个声明第一次成真。**
（"声明指向不存在的文件"与本项目反复记录的那类缺陷同族。）

**⇒ LICENSE 层面 20/20 达成。**

### 🟠 B. NOTICE 缺失（17 个仓）

Apache 2.0 不强制 NOTICE，但**它是版权人声明的落点**，也是第三方归属的落点。
**⇒ 统一形状**（照 `commonintents/.github:NOTICE`）：`产品名 / Copyright <年> <版权人> / 许可声明 /（第三方的）归属段 + 免责`。
**⚠️ 版权人写在 NOTICE，不要写进 LICENSE** —— LICENSE 必须逐字不动（见 §3 的教训）。

### 🟡 C. 规范/白皮书缺 IP 头

已覆盖的仓见 §1；**9 个仓为 0**。至少这两份是明确的"对外文档"，**优先**：
- `FlowModus:docs/whitepaper-v1.7.md`
- `helix-tentacle:docs/vision/tentacle-whitepaper-v3.4.md`

**⇒ 头部长什么样**：`> © <年> <版权人>. Licensed under CC BY-ND 4.0 (https://creativecommons.org/licenses/by-nd/4.0/).`

---

## 3. 已做（2026-09-20）

**15 个仓的 LICENSE 归一到逐字原文**（`BIND-19` · `FlowModus` · `HelixECO-Glove` · `Tuck` ·
`commonintents/{.github, BIND-19, CAPABILITY-13, INTENT-7, INTENT-7-SECURE, PFP-xCF14, SAP-xCF14}` ·
`helix-tentacle` · `lodestone-spec` · `lumtract` · `phyt-DNA`）。**不动任何正文字句**，只：

1. 补回官方原文**开头的那一个空行**（此前缺失，导致逐字比对不通过；正文原本字节相同）；
2. `FlowModus`：它把 APPENDIX 的样板行 `Copyright [yyyy] [name of copyright owner]`
   **填成了实际版权人** —— 现还原。
3. `helix-tentacle`：整个 **APPENDIX（26 行）被删过** —— 现补回。

### ⚠️ 教训：**占位符不是用来填的**

那个 APPENDIX 的括号**是给"附到源文件里的样板通知"用的**，原文自己写着
*"replaced with your own identifying information. (Don't include the brackets!)"* ——
改的是**你文件头里的那份样板**，**不是许可证正文**。**正文一动，就不再是 Apache 2.0 原文了。**
**⇒ 版权人写进 NOTICE 或文件头，永不动 LICENSE。**

### 顺带修的两处仓库配置

`HelixECO-Glove` 与 `lumtract` **没有 upstream**（收尾的 ahead/behind 检查一直测不到它们）；已设。
另：`BIND-19` 本地那一个 LICENSE 提交与远端**逐字相同**，属重复，已丢弃并采用远端（**未强推**）。

---

## 4. 可复跑的核验命令

```bash
# 取官方原文并算目标哈希
curl -sS https://www.apache.org/licenses/LICENSE-2.0.txt -o /tmp/apache2.txt
shasum -a 256 /tmp/apache2.txt
# 期望：cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30（202 行）

# 逐仓比对（输出必须全部是 ✅）
TARGET=cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
for d in $(find . -maxdepth 3 -name '.git' -type d | sed 's|/.git$||' | sed 's|^\./||' | sort); do
  if [ ! -f "$d/LICENSE" ]; then echo "$d ❌ 无 LICENSE"; continue; fi
  h=$(shasum -a 256 "$d/LICENSE" | cut -d' ' -f1)
  [ "$h" = "$TARGET" ] && echo "$d ✅" || echo "$d 🔴 非原文"
done
```

**⚠️ 取原文必须走能通的那条路**：本机 DNS 是**代理的 fake-IP 模式**（域名解析到 `198.18.0.0/15`），
所以 `web_fetch` 会按"非公网 IP"拒读；**`curl` / `git` 走代理是通的**，用它们。

---

## 5. 未做（按顺序）

1. `Cellrix` / `lodestone-md` / `Helix-MCP-Learner`：**先出第三方代码审计，再换证/新增**（缺口 A）
2. 17 个仓补 NOTICE（缺口 B）
3. 9 个仓的规范/白皮书补 CC BY-ND 头；两份白皮书优先（缺口 C）
4. 源文件许可头（**实测：全工作区 0 个源文件带 Apache 头**；Apache 不强制，但 APPENDIX 推荐）
5. 第三方代码 / 特有名词审计（规则：**仅灵感来源，不抄代码、不抄特有名词**）

---

## 6. 版权人映射（**NOTICE 那一步用，但需你确认**）

实测：**GitHub org → 正式版权人**，且已有先例可循。**我不自行发明**，先列出来。

| org | 仓 | NOTICE 里现用的写法 |
|---|---|---|
| `CommonIntents` | `BIND-19` · `commonintents/{.github, BIND-19, CAPABILITY-13, INTENT-7, INTENT-7-SECURE, PFP-xCF14, SAP-xCF14}`（8 个） | **有先例**：`Copyright 2026 CommonIntents Organization` |
| `Jasonmilk` | `Cellrix` · `FlowModus` · `Helix-MCP-Learner` · `HelixECO-Glove` · `Tuck` · `anaphase-helix` · `helix-mind` · `helix-tentacle` · `phyt-DNA`（9 个） | **有先例**：`Copyright 2026 Jason Milk` |
| `Lumtract` | `lumtract`（1 个） | **有先例**：`Copyright 2026 Lumtract Organization` |
| `lodestone-protocol` | `lodestone-md` · `lodestone-spec`（2 个） | ⚠️ **无先例** —— 该 org 下没有任何 © 行或 NOTICE。**需要你定写法** |

**⇒ 除 `lodestone-protocol` 外，其余 18 个仓都有先例可照。** 那一组我不编。

---

*本文件只记事实与判据。**旧状态一律留痕，不静默重写**；任何仓的改动前都先确认工作树状态，
不碰在飞文件。*
