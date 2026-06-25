# CommonIntents-144 (CI-144)
**面向无信任硅基原生网络的主权宪章**

[![发布状态](https://img.shields.io/badge/Status-Official_Release-2ea44f)](https://github.com/CommonIntents)
[![版本号](https://img.shields.io/badge/Version-1.0.0--RFC--4-blue)](https://github.com/CommonIntents)
[![开源协议](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## 1. 宪章与设计愿景
**核心信念**：  
**「信任必须被证明，而非被假设。」**

CI-144 是一套**去中心化开放协议族**，设计目标覆盖：
- AI原生交互与语义通信
- 基于能力的安全体系与零信任访问控制
- 加密传输与凭证隔离

它为自主智能体、认知架构、分布式执行运行时建立了底层的「交互法则」——**不绑定任何具体实现**。

---

## 📖 快速入门导航
| 我想要... | 从这里开始 |
| :--- | :--- |
| 了解整体设计蓝图 | [宪章（向下滚动）](#1-宪章与设计愿景) |
| 将 INTENT-7 集成到我的工具中 | [INTENT-7 规范 → 映射指南](https://github.com/CommonIntents/INTENT-7) |
| 为工作流添加人机审批机制 | [CAPABILITY-13 规范](https://github.com/CommonIntents/CAPABILITY-13) |
| 理解传输绑定的工作原理 | [BIND-19 规范](https://github.com/CommonIntents/BIND-19) |
| 搭建安全的双向 TLS 传输 | [INTENT-7-SECURE 规范](https://github.com/CommonIntents/INTENT-7-SECURE) |
| 查看可运行的参考实现 | [Cellrix](https://github.com/CommonIntents/Cellrix) |
| 参与协议共建 | [贡献指南](CONTRIBUTING.md) |

---

## 2. 协议栈架构（四层闭环）
CI-144 采用严格解耦的四层架构，每层向下委托专属职责，保证语义纯净、职责无交叉污染。
```
┌─────────────────────────────────────────────────────────────┐
│                 INTENT-7 (Semantic Layer)                   │
│                                                             │
│  • Structured Intent Declaration (FETCH/WRITE_NODE/TENTACLE)│
│  • W3C Trace Context Integration (traceparent)              │
│  • HXR Execution Record ↔ L3 Memory Zero-Copy Alignment    │
│  • Pure JSON Payload, Transport-Agnostic                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ JSON Payload via BIND-19 Data Frame (0x01)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              CAPABILITY-13 (Capability Layer)               │
│                                                             │
│  • Dynamic Permission Mapping (capability_mapping.toml)     │
│  • Ed25519 Signature Verification (DNSSEC-style)            │
│  • Asynchronous Non-Blocking HITL Consensus                 │
│  • GPG-style Key Rotation & Revocation                      │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Capability Validation via BIND-19 Control Frame (0x03)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                BIND-19 (Transport Layer)                    │
│                                                             │
│  • 8-Byte Fixed Frame Header (Version, Type, Channel, Seq)  │
│  • 256-Channel Multiplexing (Priority Queues)               │
│  • 0-RTT Version Negotiation (UDS Implicit Handshake)       │
│  • IANA-style Frame Type Governance (0x00-0x0F Standard)    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Binary Frames (Encrypted)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│             INTENT-7-SECURE (Security Layer)                │
│                                                             │
│  • Mandatory mTLS 1.3 (Public Networks)                     │
│  • 0ms Overhead SO_PEERCRED Verification (Local UDS)        │
│  • Edge Gateway + KMS Credential Isolation Boundary         │
│  • Certificate Pinning & Rotation (L0 Gene Lock)            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Encrypted Byte Stream
                           ▼
                  Physical Network (TCP/IP / UDS)
```

---

## 3. 协议状态矩阵
四项核心规范均已通过最终技术评审，于 **2026-06-26** 正式冻结定稿。

| 协议名称 | 状态 | 核心职责 | 遵循标准 | 版本 |
| :--- | :---: | :--- | :--- | :---: |
| **BIND-19** | ✅ **正式定稿** | 传输成帧与多路复用 | HTTP/2 成帧、QUIC 多路复用、IANA 注册表 | `v1.0.0-RFC-4` |
| **CAPABILITY-13** | ✅ **正式定稿** | 能力认证与人机共识 | OAuth2 能力体系、DNSSEC 签名、GPG 密钥轮换 | `v1.0.0-RFC-4` |
| **INTENT-7** | ✅ **正式定稿** | 结构化意图与内存对齐 | W3C 追踪上下文、JSON Schema | `v1.0.0-RFC-4` |
| **INTENT-7-SECURE** | ✅ **正式定稿** | 双向 TLS 与边缘安全 | TLS 1.3 (RFC 8446)、PKCS#11、TPM | `v1.0.0-RFC-4` |

---

## 4. 设计哲学：Milk Zen 工程准则
CI-144 严格遵循 **Milk Zen** 工程哲学，保障极致健壮性与理论纯净度：

| 设计原则 | 在 CI-144 中的落地 |
| :--- | :--- |
| **1. 必有理论依据，绝不凭空臆造** | 所有协议均基于工业标准（TLS 1.3、W3C、IANA），无无理论支撑的自研「黑科技」。 |
| **2. 求正确而非求快速** | 安全拥有绝对优先级：强制双向 TLS、禁用 TLS 1.2、密钥轮换原子执行。 |
| **3. 彻底解耦，按需生长** | 各层独立自治：BIND-19 不解析意图语义，INTENT-7 不处理加密逻辑，扩展通过保留区间实现。 |
| **4. 极致能效优先** | 本地 UDS 采用 `SO_PEERCRED` 校验（0 毫秒开销）；HXR 与 L3 内存零拷贝；摘要优先检索节省上下文窗口。 |
| **5. 局部服从全局** | 版本协商取双方支持的最高交集；安全边界保护整栈；错误链路统一出口。 |

---

## 5. 闭环数据流
```
User Intent (INTENT-7 JSON)
    │
    ├─ metadata.traceparent: Global Trace ID (W3C Standard)
    ├─ action: FETCH / WRITE_NODE / TENTACLE / FINISH / CANCEL
    └─ params: Business parameters
    │
    ▼
Capability Validation (CAPABILITY-13)
    │
    ├─ Check required_permissions against capability_mapping.toml
    ├─ Ed25519 signature verification (Creator L0 Key)
    └─ Trigger HITL consensus if high-risk (async, non-blocking)
    │
    ▼
Frame Encapsulation (BIND-19)
    │
    ├─ FrameType: Data (0x01) / Control (0x03) / Error (0x06)
    ├─ ChannelID: 0x00 (Control) / 0x01-0xFF (Data)
    └─ Flags: FIN (0x01) / CON (0x02) / SEC (0x04)
    │
    ▼
Secure Transmission (INTENT-7-SECURE)
    │
    ├─ Public Network: mTLS 1.3 (AES_256_GCM / CHACHA20_POLY1305)
    ├─ Local UDS: SO_PEERCRED (UID/GID verification, 0ms overhead)
    └─ Credential Injection: Edge Gateway + KMS (Zero-Knowledge to Sandbox)
    │
    ▼
Physical Network (TCP/IP / UDS)
    │
    ▼
Receiver (Memory Node / Execution Runtime)
    │
    └─ HXR Record written to L3 Episodic Memory (Zero-Copy)
```

---

## 6. 错误码体系
协议族内所有错误统一通过 BIND-19 错误帧（`0x06`）向上传递。

| 所属协议 | 码值范围 | 典型错误 |
| :--- | :--- | :--- |
| **BIND-19** | `0x0400 - 0x05FF` | `INVALID_FRAME_HEADER` (0x0400)、`VERSION_MISMATCH` (0x0460) |
| **CAPABILITY-13** | `0x0580 - 0x05FF` | `PERMISSION_DENIED` (0x0580)、`INVALID_CONFIGURATION_SIGNATURE` (0x05FA) |
| **INTENT-7** | `0x0640 - 0x06FF` | `INVALID_PAYLOAD_SCHEMA` (0x0640)、`UNKNOWN_INTENT_VERB` (0x064A) |
| **INTENT-7-SECURE** | `0x07D0 - 0x07FF` | `MTLS_HANDSHAKE_FAILED` (0x07D0)、`UNTRUSTED_PEER_UID` (0x07DA) |

---

## 7. 可追溯性与审计
CI-144 中每一笔事务都可通过 W3C 追踪上下文标准实现全链路溯源：
```
traceparent: 00-<trace-id>-<span-id>-01
             │    │          │        └─ trace-flags
             │    │          └────────── 64-bit Span ID
             │    └───────────────────── 128-bit Trace ID
             └────────────────────────── version
```
- `traceparent` 起源于 INTENT-7 的元数据
- 在 INTENT-7-SECURE 中与 TLS 会话 ID 绑定
- 嵌入 L3 内存的 HXR 执行记录中
- 支持跨进程、跨网络的完整因果链审计

---

## 8. 快速开始
1. **阅读规范**：从 [BIND-19](https://github.com/CommonIntents/BIND-19) 开始，理解传输成帧机制。
2. **实现客户端**：基于 8 字节固定头部结构进行帧的编码与解码。
3. **加固通道**：按照 INTENT-7-SECURE 规范实现 `双向 TLS` 或 `SO_PEERCRED` 本地校验。
4. **声明意图**：使用 INTENT-7 动词（FETCH、WRITE_NODE、TENTACLE）构建语义流程。

---

## 9. 贡献指南
我们遵循严格的 RFC（意见征集）流程。  
提交提案前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 10. 安全说明
安全是 CI-144 的基石。  
漏洞反馈请查看 [SECURITY.md](SECURITY.md)。

---

**CommonIntents-144 © 2026 - Present**  

---

## 开源协议与归属声明

CI-144 基于 **Apache License 2.0** 协议开源，完整协议文本请查看 [LICENSE](LICENSE)。

### 归属声明
本项目的设计参考了 HTTP/2、TLS 1.3、OAuth 2.0、JSON-RPC、W3C Trace Context 等多项开放标准。详细归属说明请查看 [NOTICE](NOTICE)。

### 技术溯源
与现有协议的详细技术对比，请参阅 [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md)。
