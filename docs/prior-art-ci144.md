# Prior Art — CI-144 协议家族防御性公开（四层协议栈）

> **性质**：防御性公开（Defensive Publication）。本文档将 CI-144 协议家族的核心创新点
> 以可验证方式公开披露，构成"先有技术"（prior art）证据，防止第三方就相同或近似
> 技术方案申请专利后反向主张。
> **公开日期**：2026-09-06（GitHub 提交时间戳为不可变证据）
> **规范依据**：phyt-DNA 方法论 `docs/PROTECTION.md`（Prior Art as Code 规范）
> **组织**：CommonIntents · 所有仓库 Apache 2.0
>
> **法律基础**：35 U.S.C. §102(a)(1)（美国）/ EPC Art. 54(2)（欧洲）/ 中国《专利法》
> 先申请制——申请日前已公开披露的技术不构成可授权的新颖技术。本文档与各协议仓库
> 的公开历史共同构成披露证据。

---

## 零、家族总览

CI-144 是四层解耦协议栈：**语义层（INTENT-7）→ 能力层（CAPABILITY-13）→ 安全层
（INTENT-7-SECURE）→ 传输层（BIND-19）**，外加两个扩展协议（PFP-xCF14 物理特征、
SAP-xCF14 安全证明）。

| 层 | 仓库 | spec 状态 | 核心创新点（本文件主张） |
|---|---|---|---|
| 语义 | INTENT-7 | v0.7.0-draft | 7 核心字段意图语义 + `x-` 扩展前缀 + 最小语法层不定义行为 |
| 能力 | CAPABILITY-13 | v0.3.0-draft | HITL 决策队列 + node_type/status 开放枚举 + custom_scopes 保留区 |
| 安全 | INTENT-7-SECURE | v0.3.0-draft | SO_PEERCRED 零开销本地身份验证 + mTLS 1.3 可选 + 凭证隔离 |
| 传输 | BIND-19 | v2.0-alpha | 8 字节固定帧头 + 256 通道多路复用 + 0-RTT 版本协商 + 心跳 |
| 扩展 | PFP-xCF14 | v1.0 冻结 | 4 字节固定偏移物理上下文头（<100ns 硬实时） |
| 扩展 | SAP-xCF14 | v1.0 | 28 字节安全证明层（防重放 + 双层签名） |

---

## 一、架构级创新点

### PA-1：四层解耦协议栈（语义/能力/安全/传输）

- **内容**：人机交互协议按职责拆分为四独立层，各层独立演进、独立版本、独立冻结；
  语义层只描述"意图是什么"，能力层只描述"谁能做什么"，安全层只描述"如何证明身份"，
  传输层只描述"如何传输帧"。层间通过开放枚举与扩展保留区衔接，不互相依赖冻结字段。
- **创新点**：①协议栈分层的**职责边界划分**（区别于单体协议或仅二/三层分层）；
  ②各层独立版本号与独立冻结策略，允许 draft 与 frozen 共存于同一家族。
- **证据**：`commonintents/{INTENT-7,CAPABILITY-13,INTENT-7-SECURE,BIND-19}/spec/` +
  `.github/CONTRIBUTING.md`（扩展保留区定义）。

### PA-2：扩展保留区机制（`x-` 前缀 + 开放枚举 + custom_scopes）

- **内容**：协议家族为未冻结阶段的应用侧扩展预留三条通道——INTENT-7 动词 `x-*`
  前缀、CAPABILITY-13 `node_type`/`status` 开放枚举（unknown → 宽容降级）、
  `custom_scopes` 段。扩展先以"本地扩展"形态落地（MVP），成熟后贡献回 spec。
- **创新点**：在 spec 未冻结时即保证扩展不破坏协议演进——扩展天然兼容升级，
  不需要 breaking change 通道。
- **证据**：`.github/CONTRIBUTING.md` 扩展保留区表 + 各协议 spec 开放枚举定义。

### PA-3：W3C Trace Context 全链路审计（跨层统一可观测性）

- **内容**：协议家族所有层共享同一 trace context 语义（W3C 兼容），从 UI 交互
  表面到内部器官调用可全链路追踪，为审计与白盒提供统一可观测基线。
- **证据**：各协议 spec 的 trace 字段定义。

---

## 二、传输层创新点（BIND-19）

### PB-1：8 字节固定帧头 + 256 通道多路复用

- **内容**：固定 8 字节帧头（魔数 + 通道号 + 长度 + 标志），单通道内可承载
  256 路逻辑通道多路复用，帧定界零歧义。
- **创新点**：固定偏移帧头设计（无变长解析状态机），解析复杂度 O(1)，
  适合嵌入式与低延迟场景。
- **证据**：`commonintents/BIND-19/spec/` 帧格式定义 + `BIND-19` 实现仓库解析器。

### PB-2：0-RTT 版本协商

- **内容**：版本协商在首帧完成，不增加握手往返（0-RTT），兼容新旧版本共存。
- **证据**：`commonintents/BIND-19/spec/`。

### PB-3：PFP/SAP 可插拔安全扩展

- **内容**：传输层不内置安全，通过可插拔扩展头（PFP 物理特征、SAP 安全证明）
  按需叠加，实现"传输与安全解耦"。
- **证据**：`commonintents/BIND-19/spec/` + `PFP-xCF14`/`SAP-xCF14` 独立规范。

---

## 三、能力层创新点（CAPABILITY-13）

### PC-1：HITL 决策队列（Human-In-The-Loop 审批闸门）

- **内容**：高风险意图不直接执行，进入人类决策队列，由人类按键放行或拒绝；
  未放行意图物理上不可达执行体。
- **创新点**：把"人类审批"从应用逻辑提升为协议级能力——任何实现 CAPABILITY-13
  的执行体都获得一致的人类监督闸门，且以**队列死锁**（非软标志）实现物理拦截。
- **证据**：`commonintents/CAPABILITY-13/spec/` HITL 部分。

### PC-2：SemanticSnapshot + view_hash 共识锚点

- **内容**：界面状态以 SemanticSnapshot 对外发布（node_type 开放枚举 +
  status 开放枚举 + view_hash 签名基准），消费方按"what you see is what you sign"
  共识确认。
- **创新点**：界面状态可签名、可校验、可降级（unknown 宽容渲染）——为
  "人机共识"提供协议级基座。
- **证据**：`commonintents/CAPABILITY-13/spec/` + Cellrix 参考实现。

---

## 四、安全层创新点（INTENT-7-SECURE）

### PS-1：SO_PEERCRED 零开销本地身份验证

- **内容**：本地 UDS 场景下用内核 SO_PEERCRED 获取对端进程真实身份（PID/UID），
  零网络开销、零额外握手完成进程级身份核验。
- **创新点**：身份验证下沉到内核套接字选项，不引入证书/密钥交换开销——
  本地安全与远程安全使用不同机制，按场景选择。
- **证据**：`commonintents/INTENT-7-SECURE/spec/`。

### PS-2：凭证隔离（只传标签不传凭证）

- **内容**：跨组件调用只传递身份标签（identity_labels），原始凭证
  （OAuth Token/API Key）锁在授权方保险柜，消费方永远拿不到原始凭证。
- **创新点**：把"零信任凭证"落地为协议级约束——凭证泄漏面收敛到单一保管方。
- **证据**：`commonintents/INTENT-7-SECURE/spec/` + Anaphase/Tuck 实现。

### PS-3：mTLS 1.3 可选通道

- **内容**：远程场景可选 mTLS 1.3，与本地 SO_PEERCRED 双轨并存。
- **证据**：`commonintents/INTENT-7-SECURE/spec/`。

---

## 五、语义层创新点（INTENT-7）

### PI-1：最小语法层 + 不定义行为

- **内容**：意图协议只定义"意图的语法形状"（7 核心字段），明确不定义行为语义；
  行为适配交给下游编排方。协议语法极简，避免语义膨胀。
- **创新点**：语法/语义分离——协议只约束表达结构，不约束执行结果，
  实现方自由裁量适配。
- **证据**：`commonintents/INTENT-7/spec/`。

### PI-2：AI 原生意图描述（区别于 UI 动作）

- **内容**：意图字段面向 AI 原生表达（x-fetch-memory / x-write-l3 /
  x-enter-dream 等），不是鼠标键盘动作的序列化——意图即语义，动作是实现的细节。
- **证据**：`commonintents/INTENT-7/spec/` 动词表。

---

## 六、扩展协议创新点

### PX-1：PFP-xCF14 物理特征头

- **内容**：4 字节固定偏移物理上下文头（魔数 0xCF14），承载物理上下文特征，
  面向 <100ns 硬实时场景，独立于传输层叠加。
- **证据**：`commonintents/PFP-xCF14/spec/`（v1.0 冻结）。

### PX-2：SAP-xCF14 安全证明层

- **内容**：28 字节安全证明层，防重放（nonce 时间窗）+ 双层签名（内容签名 +
  会话签名），可插拔叠加于传输帧。
- **证据**：`commonintents/SAP-xCF14/spec/`（v1.0）。

---

## 七、参考实现与生态证据

| 参考实现 | 仓库 | 与 CI-144 关系 |
|---|---|---|
| Cellrix | Jasonmilk/Cellrix | INTENT-7 spec §15 法定参考实现 + 测试床（语义/能力层消费） |
| Tuck | Jasonmilk/Tuck | CI-144 四层管控执行体（安全层 SO_PEERCRED 核验 + 能力层 HITL/令牌） |
| Anaphase | Jasonmilk/Anaphase-Helix | 编排方 + 意图生产者（x- 前缀意图） |
| BIND-19 | CommonIntents/BIND-19 | 传输层实现（v2.0-alpha，140+ 测试，33 组测试向量） |
| Helix-Mind | Jasonmilk/Helix-Mind | 潜意识层消费方（UDS Daemon 复用） |

生态应用（ADR-0023）证明：四层协议栈 + 扩展保留区机制已支撑"驾驶/伙伴/生存"
三模式管控（Tuck 按模式发放 Capability Scopes、物理通道层拦截非法意图）。

---

## 八、披露范围与边界

- **已披露**：协议结构与机制的描述性创新点（如上）。
- **未披露**：实现级商业秘密（如特定算法的内部参数、未公开的流程细节）——
  防御性公开只保护"可被抢注"的公共创新点，不暴露实现秘密。
- **更新策略**：协议演进产生新机制时，按同一规范追加本文档（模块化追加，不重写历史）。
