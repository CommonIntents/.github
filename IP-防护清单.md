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

| 仓 | LICENSE | NOTICE | 核心思想文档许可声明 |
|---|---|---|---|
| BIND-19 | ✅ Apache 2.0 逐字 | 有 | 5 |
| Cellrix | ✅ Apache 2.0 逐字（**2026-09-20 由 MIT 换证**） | 有 | 0 |
| FlowModus | ✅ Apache 2.0 逐字 | 有 | 1 |
| Helix-MCP-Learner | ✅ Apache 2.0 逐字（**2026-09-20 新增**） | 有 | 0 |
| HelixECO-Glove | ✅ Apache 2.0 逐字 | 有 | 0 |
| Tuck | ✅ Apache 2.0 逐字 | 有 | 0 |
| anaphase-helix | ✅ Apache 2.0 逐字 | 有 | 0 |
| commonintents/.github | ✅ Apache 2.0 逐字 | 有 | 2 |
| commonintents/BIND-19 | ✅ Apache 2.0 逐字 | 有 | 5 |
| commonintents/CAPABILITY-13 | ✅ Apache 2.0 逐字 | 有 | 3 |
| commonintents/INTENT-7 | ✅ Apache 2.0 逐字 | 有 | 3 |
| commonintents/INTENT-7-SECURE | ✅ Apache 2.0 逐字 | 有 | 3 |
| commonintents/PFP-xCF14 | ✅ Apache 2.0 逐字 | 有 | 1 |
| commonintents/SAP-xCF14 | ✅ Apache 2.0 逐字 | 有 | 1 |
| helix-mind | ✅ Apache 2.0 逐字 | 有 | 0 |
| helix-tentacle | ✅ Apache 2.0 逐字 | 有 | 0 |
| lodestone-md | ✅ Apache 2.0 逐字（**2026-09-20 由 MIT 换证**） | 有 | 0 |
| lodestone-spec | ✅ Apache 2.0 逐字 | 有 | 0 |
| lumtract | ✅ Apache 2.0 逐字 | 有 | 0 |
| phyt-DNA | ✅ Apache 2.0 逐字 | 有 | 1 |

**小计**：LICENSE 逐字 Apache 2.0 **20/20** ✅ ｜ NOTICE **20/20** ✅ ｜ 核心思想文档许可声明 **35/35** ✅（均 2026-09-20 达成）。

> ⚠️ **本表第 4 列原写作「带 CC BY-ND 的文档」，那个口径是错的**（2026-09-20 更正）：
> 它只数 **CC BY-ND**，于是把**已经声明 Apache 2.0 的文档**误记为 0 —— 而后者并不是缺口。
> 实测：只有 `commonintents/*/spec/*` 用 CC BY-ND 4.0；**其余仓的核心文档声明的是 Apache 2.0**
> （FlowModus 的 VISION 与白皮书、helix-tentacle 白皮书、lodestone-spec 的规范正文皆然）。
> **⇒ 判据应是「头部区域是否声明了许可（任一形式）」，不是「是否用了某一种许可」。**
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

### ✅ B. NOTICE —— **已关闭（2026-09-20）**

Apache 2.0 不强制 NOTICE，但**它是版权人声明的落点** —— 尤其因为 LICENSE 必须逐字不动，
版权人**只能**写在这里（或源文件头）。

**统一形状**（照 `commonintents/.github:NOTICE` 与 `FlowModus:NOTICE`）：
```
产品名
Copyright <年> <版权人>

This product includes software developed by the <产品名> Community
(https://github.com/<org>/<repo>).

Licensed under the Apache License, Version 2.0 (the "License");
… （Apache 2.0 样板通知）
```

**新增 17 份 + 归正 1 份**（`lumtract` 是唯一非标准形状：产品名占三行、版权人在第 4 行；
现补成标准形状，**原有三行一字保留**并下移为描述行）。

判据（可复跑）：每仓 `sed -n '2p' NOTICE` 必须匹配 `^Copyright`；覆盖率 20/20。

**⚠️ 版权人绝不写进 LICENSE** —— LICENSE 必须逐字不动（见 §3 的教训）。

### ✅ C. 核心思想文档缺许可声明 —— **已关闭（2026-09-20）**

**范围（用户界定）**：只补 **核心思想文档**；**源代码头部明确不做**（见 §5）。

**实测缺口**：`DNA.md` / `RNA.md` / `VISION.md` / `vision/*` 共 **32 份**无任何许可声明 ——
它们是复制与引用最广的文档，却缺一句「按什么许可发布」。

**改动**：在标题行之后插一行（**不动正文一个字**）：

```
> © 2026 <版权人> · Apache 2.0
```

- 许可取 **Apache 2.0**：取自本工作区既有先例（FlowModus 的 VISION 与白皮书均声明 Apache 2.0，
  代码仓亦为 Apache 2.0），**不是新立的规矩**。
- 版权人取既有映射（GitHub org → 版权人），不新造。

**判据（可复跑）**：核心思想文档（`*whitepaper*` / `VISION*` / `vision/*` / `DNA.md` / `RNA.md`）
**前 10 行内**含 `©` / `Apache` / `CC BY` / `许可证` 之一。

> **为什么是「前 10 行」而不是「第 2 行」**：有 **3 份**文档原本就在第 4 / 6 / 9 行声明了许可
> （FlowModus 的 VISION 与白皮书、helix-tentacle 白皮书）。**不为了判据整齐去搬动它们已有的行** ——
> 那属于回改既有内容。**判据该适应事实，而不是反过来。**

**⇒ 覆盖 35/35。**

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
2. ✅ 已做：NOTICE 20/20（缺口 B 关闭）
3. 9 个仓的规范/白皮书补 CC BY-ND 头；两份白皮书优先（缺口 C）
4. ~~源文件许可头~~ —— **❌ 按用户指示撤销，不做**（2026-09-20）。
   用户原话：「改一下许可证和核心思想文档就完全足够了，你不会在源代码头部做文章吧？！」
   **⇒ 本条从目标中移除。** 理由成立：Apache 2.0 **不要求**逐文件头部；
   根目录 `LICENSE` + `NOTICE` 已构成完整的许可声明，逐文件头部是"看起来更严谨"而非义务。
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

---

## 7. 防护形状（**结论，不需要再勘察**）

四层，各挡一种风险。**都不是我发明的** —— 前三层在本工作区已存在，本节只是把它写清。

### 第 1 层｜代码用 Apache 2.0 —— 挡"专利埋伏"，同时允许商用

Apache 2.0 §3 含**明示专利授权**：贡献者不能一边贡献一边拿专利告你。
同时它**允许**商用、修改、闭源再分发 —— 这正是"通用项目"要的。
**⇒ 不用 MIT/BSD 的原因不是"更严"，是它们没有专利条款。**

### 第 2 层｜规范用 CC BY-ND 4.0 —— 挡"改头换面"

`commonintents/*/spec/*` 的规范正文用 **CC BY-ND**（署名 · **禁演绎**）：
任何人可读、可引用、可原样分发，**不能改一版冒充原规范**。
**⇒ 协议要能互通，就必须只有一个权威文本。** 代码可以各自实现，规范不能各自改。

> 注意：**这一条只用于规范正文**。其余仓的核心文档声明 Apache 2.0 即可
> （见 §1 的口径更正）—— 别把"禁演绎"套到工程文档上，那会挡住正常演进。

### 第 3 层｜防御性公开 / 先有技术 —— 挡"抢注专利"，**这是最容易被漏掉的一层**

**它解决的问题**：你想让所有人免费使用你的机制，但不想被某家公司拿去申请专利再反过来告你。
**做法**：把创新点 + 代码证据路径 + 首次提交 SHA 公开记录下来，公开渠道 = 公开 git 仓库。
**效果**：公开日之后即为现有技术，可用于**新颖性抗辩与无效宣告**（中国"先申请制"下尤其重要）。
**性质**：**不限制任何人使用**，只冻结"谁先公开"。

**现状**：只有 **2/20** 个仓有（`FlowModus` 与 `commonintents/.github` 的 CI-144 各一份）。
**⇒ 建议**：**凡含"自成一体的机制"的仓都补一份**，形状照现有两份。
不需要为纯实现/纯文档仓补 —— 那一层没有可抢注的东西。

### 第 4 层｜归属声明 —— 挡"无意侵占他人"

`NOTICE` 里的归属段（`commonintents/.github` 那份是样板）：
逐条列出**灵感来源**（标准/论文）· 来源链接 · 采用了什么概念 · 对方的许可，
并在末尾写明 **"本项目不包含上述项目的代码或文本，全部为原创；列出仅为归属与透明"**。

**⇒ 这条的意义是把"借鉴"与"抄袭"在文件层面分开**，而且它同时是一份**免责证据**。

### 边界：**什么没有被保护，以及不该去碰什么**

| | |
|---|---|
| **名字/术语** | 像功能名、界面名这类**描述性标签通常不是商标**；本工作区也**未注册任何商标**。⇒ 不要指望名字受保护，也不要依赖名字建立壁垒 |
| **不该做的** | **不并排复制他人产品的多个界面**（那正是"商业外观 / trade dress"的硬红线，与代码许可无关）；**不抄代码、不搬特有名词**（用户规则） |
| **该做的** | 借鉴**思路**（不受版权保护）；引用时**写明来源**；实现**自己写** |

### 一句话

> **代码可被人拿去用（第 1 层），规范不可以被人改（第 2 层），
> 机制不可以被人抢注（第 3 层），借鉴必须留下出处（第 4 层）。**
