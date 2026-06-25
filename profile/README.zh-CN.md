# CommonIntents-144 (CI-144)
**去信任化硅基网络的至高主权宪法。**

[![状态](https://img.shields.io/badge/状态-正式发布-2ea44f)](https://github.com/CommonIntents)
[![版本](https://img.shields.io/badge/版本-1.0.0--RFC--4-blue)](https://github.com/CommonIntents)
[![许可证](https://img.shields.io/badge/许可证-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**[English Version](./README.md)**

---

## 1. 宪法与愿景
**核心信条**：  
**"信任必须被证明，而非被假定。"**

CI-144 是一个**去中心化、开放协议家族**，专为以下目标设计：
- AI 原生交互与语义通信
- 基于能力的零信任访问控制
- 加密传输与凭证隔离

它为自主代理、认知架构和分布式执行运行时建立了基础的“交互法则”——**不绑定任何具体实现**。

---

## 2. 协议栈架构（四层闭环）
CI-144 实现了严格解耦的四层架构。每一层向下委托特定职责，确保纯粹性且无交叉污染。

```
┌─────────────────────────────────────────────────────────────┐
│                 INTENT-7 (语义层)                           │
│                                                             │
│  • 结构化意图声明 (FETCH/WRITE_NODE/TENTACLE)              │
│  • W3C Trace Context 集成                  │
│  • HXR 执行记录 ↔ L3 记忆零拷贝对齐                        │
│  • 纯 JSON 载荷，传输无关                                  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ JSON Payload via BIND-19 Data Frame (0x01)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              CAPABILITY-13 (能力层)                         │
│                                                             │
│  • 动态权限映射 (capability_mapping.toml)                   │
│  • Ed25519 签名验证 (DNSSEC 风格)                          │
│  • 异步非阻塞 HITL 共识                                    │
│  • GPG 风格密钥轮转与撤销                                  │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Capability Validation via BIND-19 Control Frame (0x03)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                BIND-19 (传输层)                             │
│                                                             │
│  • 8 字节固定帧头 (Version, Type, Channel, Seq)           │
│  • 256 通道多路复用（优先级队列）                          │
│  • 0-RTT 版本协商（UDS 隐式握手）                         │
│  • IANA 风格帧类型治理 (0x00-0x0F 标准)                    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Binary Frames (Encrypted)
                           ▼
┌─────────────────────────────────────────────────────────────┐
│             INTENT-7-SECURE (安全层)                        │
│                                                             │
│  • 强制 mTLS 1.3 (公共网络)                                │
│  • 0ms 开销 SO_PEERCRED 验证 (本地 UDS)                   │
│  • 边缘网关 + KMS 凭证隔离边界                            │
│  • 证书固定与轮转 (L0 基因锁)                              │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           │ Encrypted Byte Stream
                           ▼
                  物理网络 (TCP/IP / UDS)
```

---

## 3. 协议状态矩阵
四大核心规范均已通过最终技术审计，并于 **2026-06-26** 正式冻结。

| 协议 | 状态 | 主要职责 | 关键标准 | 版本 |
| :--- | :---: | :--- | :--- | :---: |
| **BIND-19** | ✅ **已定稿** | 传输成帧与多路复用 | HTTP/2 Framing, QUIC Multiplexing, IANA Registry | `v1.0.0-RFC-4` |
| **CAPABILITY-13** | ✅ **已定稿** | 能力鉴权与 HITL | OAuth2 Capabilities, DNSSEC Signing, GPG Rotation | `v1.0.0-RFC-4` |
| **INTENT-7** | ✅ **已定稿** | 结构化意图与记忆对齐 | W3C Trace Context, JSON Schema | `v1.0.0-RFC-4` |
| **INTENT-7-SECURE** | ✅ **已定稿** | 双向 TLS 与边缘安全 | TLS 1.3 (RFC 8446), PKCS#11, TPM | `v1.0.0-RFC-4` |

---

## 4. 设计哲学：Milk Zen
CI-144 严格遵循 **Milk Zen** 工程哲学，确保极致的健壮性与理论纯粹性：

| 原则 | CI-144 中的实现 |
| :--- | :--- |
| **1. 理论支撑，拒盲猜测** | 所有协议基于工业标准 (TLS 1.3, W3C, IANA)。无无理论依据的“发明”。 |
| **2. 做对的，不做快的** | 安全绝对优先。强制 mTLS；禁用 TLS 1.2；密钥轮转原子化。 |
| **3. 彻底解耦，按需生长** | 每一层独立。BIND-19 不解析意图；INTENT-7 不处理加密。通过保留范围扩展。 |
| **4. 极致节能** | 本地 UDS 使用 `SO_PEERCRED` (0ms 开销)。HXR ↔ L3 记忆零拷贝。摘要优先检索节省上下文窗口。 |
| **5. 局部服从全局** | 版本协商选择最高交集。安全边界保护整个栈。错误管道统一。 |

---

## 5. 闭环数据流
```
用户意图 (INTENT-7 JSON)
    │
    ├─ metadata.traceparent: 全局追踪 ID (W3C 标准)
    ├─ action: FETCH / WRITE_NODE / TENTACLE / FINISH / CANCEL
    └─ params: 业务参数
    │
    ▼
能力验证 (CAPABILITY-13)
    │
    ├─ 检查 required_permissions 对照 capability_mapping.toml
    ├─ Ed25519 签名验证 (Creator L0 Key)
    └─ 若高风险则触发 HITL 共识（异步、非阻塞）
    │
    ▼
帧封装 (BIND-19)
    │
    ├─ FrameType: Data (0x01) / Control (0x03) / Error (0x06)
    ├─ ChannelID: 0x00 (Control) / 0x01-0xFF (Data)
    └─ Flags: FIN (0x01) / CON (0x02) / SEC (0x04)
    │
    ▼
安全传输 (INTENT-7-SECURE)
    │
    ├─ 公共网络: mTLS 1.3 (AES_256_GCM / CHACHA20_POLY1305)
    ├─ 本地 UDS: SO_PEERCRED (UID/GID 验证, 0ms 开销)
    └─ 凭证注入: 边缘网关 + KMS (对沙箱零知识)
    │
    ▼
物理网络 (TCP/IP / UDS)
    │
    ▼
接收者 (记忆节点 / 执行运行时)
    │
    └─ HXR 记录写入 L3 情景记忆 (零拷贝)
```

---

## 6. 错误码架构
协议族中的所有错误均通过 BIND-19 错误帧 (`0x06`) 统一传播。

| 协议 | 代码范围 | 示例错误 |
| :--- | :--- | :--- |
| **BIND-19** | `0x0400 - 0x05FF` | `INVALID_FRAME_HEADER` (0x0400), `VERSION_MISMATCH` (0x0460) |
| **CAPABILITY-13** | `0x0580 - 0x05FF` | `PERMISSION_DENIED` (0x0580), `INVALID_CONFIGURATION_SIGNATURE` (0x05FA) |
| **INTENT-7** | `0x0640 - 0x06FF` | `INVALID_PAYLOAD_SCHEMA` (0x0640), `UNKNOWN_INTENT_VERB` (0x064A) |
| **INTENT-7-SECURE** | `0x07D0 - 0x07FF` | `MTLS_HANDSHAKE_FAILED` (0x07D0), `UNTRUSTED_PEER_UID` (0x07DA) |

---

## 7. 可追溯性与审计
CI-144 中的每笔交易均可通过 W3C Trace Context 标准完全追溯：
```
traceparent: 00-<trace-id>-<span-id>-01
             │    │          │        └─ trace-flags
             │    │          └────────── 64 位 Span ID
             │    └───────────────────── 128 位 Trace ID
             └────────────────────────── version
```
- `traceparent` 源于 INTENT-7 `metadata`。
- 它与 INTENT-7-SECURE 中的 TLS Session ID 绑定。
- 它被嵌入 L3 记忆的 HXR 记录中。
- 实现跨进程/网络边界的完整因果链审计。

---

## 8. 快速开始
1. **阅读规范**：从 [BIND-19](https://github.com/CommonIntents/BIND-19) 开始，了解传输成帧。
2. **实现客户端**：使用 8 字节帧头结构来编码/解码帧。
3. **保护通道**：实现 INTENT-7-SECURE 中定义的 `mTLS` 或 `SO_PEERCRED`。
4. **声明意图**：使用 INTENT-7 动词 (FETCH, WRITE_NODE, TENTACLE) 构建语义流。

---

## 9. 贡献
我们遵循严格的 RFC (Request for Comments) 流程。  
提交提案前请阅读 [CONTRIBUTING.zh-CN.md](../CONTRIBUTING.zh-CN.md)。

## 10. 安全
安全是 CI-144 的基石。  
漏洞报告请查看 [SECURITY.zh-CN.md](../SECURITY.zh-CN.md)。

---

## 11. 许可证与归属
CI-144 基于 **Apache License 2.0** 授权。详见 [LICENSE](../LICENSE)。

### 归属声明
本项目受 HTTP/2、TLS 1.3、OAuth 2.0、JSON-RPC 和 W3C Trace Context 等开放标准启发。详见 [NOTICE](../NOTICE)。

### 技术传承
与现有协议的详细技术对比，请参阅 [ACKNOWLEDGMENTS.zh-CN.md](../ACKNOWLEDGMENTS.zh-CN.md)。

---

**CommonIntents-144 © 2026 - 至今**  
**基于 Apache 2.0 授权**
