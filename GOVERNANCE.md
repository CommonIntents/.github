# CommonIntents-144 治理宪章（GOVERNANCE）
> v1.1 | 2026-08-29 | CI-144 协议家族由「项目 DNA 自生长方法论」治理（参考 Helix-Mind DNA.md v2.0）。此为防腐化基线锁定，变更走 RFC / 审查流程。

## 方法论文档体系（组织级，必读）

| 文档 | 位置 | 作用 |
|---|---|---|
| **GOVERNANCE.md** | 本文件 | 治理宪章，防腐化基线 |
| **DNA.md** | `.github/DNA.md` | 不可变原则（6 条公理），协议家族最高裁判 |
| **RNA.md** | `.github/RNA.md` | AI 协作铁律 + 三层加载协议 |

> **强制要求**：任何 AI 在参与 CI-144 协议家族任务前，必须按 RNA.md 的三层加载协议完整读取上述文档。未读取的 AI 输出直接拒绝。

## 治理分层（三层自纠偏）
- **N 层（愿景）**：门面 README / VISION —— 极少变更。
- **D 层（决策）**：ADR —— 两态（Draft / Active）；Active 后不可覆写，仅可 Superseded。存放于各协议仓库的 `docs/decisions/` 目录（首次 ADR 时创建）。
- **A 层（实现）**：spec + 代码 —— 物理事实优先。

## 防腐化铁律
1. 版本以 spec 正文为源真相，README / 门面标注必须对齐（防版本漂移）。
2. 协议语义冻结（v1.0.0-RFC-4）不可静默修改；扩展走 Append-Only / reserved 预留。
3. 每次变更先 ADR（D 层冻结）→ 再改 spec / 代码 → 最后同步门面。
4. 生长记录（GROWTH）保留近 3 条，超则归档至 archive，永不删除。
5. 提交前必须人工确认。

## 适用范围
CommonIntents 全部协议仓库（INTENT-7 / BIND-19 / INTENT-7-SECURE / CAPABILITY-13 / .github），独立演进、共用此宪章。
