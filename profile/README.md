# CommonIntents-144 (CI-144)
**The Sovereign Constitution for Trustless Silicon-Native Networks.**  

[![Status](https://img.shields.io/badge/Status-Official_Release-2ea44f)](https://github.com/CommonIntents)
[![Version](https://img.shields.io/badge/Version-1.0.0--RFC--4-blue)](https://github.com/CommonIntents)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

---

## 1. Constitution & Vision
**Core Belief**:  
**"Trust must be proven, not assumed."**  

CI-144 is a **decentralized, open protocol family** designed for:
- AI-native interaction and semantic communication
- Capability-based security and zero-trust access control
- Encrypted transport and credential isolation

It establishes the foundational "law of interaction" for autonomous agents, cognitive architectures, and distributed execution runtimes—**without binding to any specific implementation**.

---

## 📖 Where to Start?
| I want to... | Start here |
| :--- | :--- |
| Understand the big picture | [Constitution (scroll down)](#1-constitution--vision) |
| Integrate INTENT-7 into my tool | [INTENT-7 Specification → Mapping Guide](https://github.com/CommonIntents/INTENT-7) |
| Add HITL approval to my workflow | [CAPABILITY-13 Specification](https://github.com/CommonIntents/CAPABILITY-13) |
| Understand how transport binding works | [BIND-19 Specification](https://github.com/CommonIntents/BIND-19) |
| Set up secure mTLS transport | [INTENT-7-SECURE Specification](https://github.com/CommonIntents/INTENT-7-SECURE) |
| See a working reference implementation | [Cellrix](https://github.com/CommonIntents/Cellrix) |
| Contribute to the protocols | [Contributing Guide](CONTRIBUTING.md) |

---

## 2. Protocol Stack Architecture (4-Layer Closed-Loop)
CI-144 implements a strictly decoupled 4-layer architecture. Each layer delegates specific responsibilities downwards, ensuring purity and no cross-contamination of concerns.
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

## 3. Protocol Status Matrix
All four core specifications have passed final technical audit and are officially frozen as of **2026-06-26**.

| Protocol | Status | Primary Responsibility | Key Standards | Version |
| :--- | :---: | :--- | :--- | :---: |
| **BIND-19** | ✅ **Finalized** | Transport Framing & Multiplexing | HTTP/2 Framing, QUIC Multiplexing, IANA Registry | `v1.0.0-RFC-4` |
| **CAPABILITY-13** | ✅ **Finalized** | Capability Authentication & HITL | OAuth2 Capabilities, DNSSEC Signing, GPG Rotation | `v1.0.0-RFC-4` |
| **INTENT-7** | ✅ **Finalized** | Structured Intent & Memory Alignment | W3C Trace Context, JSON Schema | `v1.0.0-RFC-4` |
| **INTENT-7-SECURE** | ✅ **Finalized** | Mutual TLS & Edge Security | TLS 1.3 (RFC 8446), PKCS#11, TPM | `v1.0.0-RFC-4` |

---

## 4. Design Philosophy: Milk Zen
CI-144 is strictly built upon the **Milk Zen** engineering philosophy, ensuring extreme robustness and theoretical purity:

| Principle | Implementation in CI-144 |
| :--- | :--- |
| **1. Theoretical Support, No Guessing** | All protocols based on industrial standards (TLS 1.3, W3C, IANA). No proprietary "inventions" without theoretical grounding. |
| **2. Do It Right, Not Fast** | Security takes absolute precedence. mTLS is mandatory; TLS 1.2 is forbidden; Key rotation is atomic. |
| **3. Thorough Decoupling, On-Demand Growth** | Each layer is independent. BIND-19 does not parse intent; INTENT-7 does not handle encryption. Extensions via reserved ranges. |
| **4. Extreme Energy Efficiency** | Local UDS uses `SO_PEERCRED` (0ms overhead). HXR ↔ L3 memory is zero-copy. Summary-first retrieval saves context window. |
| **5. Local Obeys Global** | Version negotiation chooses highest intersection. Security boundary protects the entire stack. Error pipeline is unified. |

---

## 5. Closed-Loop Data Flow
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

## 6. Error Code Architecture
All errors across the protocol family are propagated uniformly via BIND-19 Error Frame (`0x06`).

| Protocol | Code Range | Example Errors |
| :--- | :--- | :--- |
| **BIND-19** | `0x0400 - 0x05FF` | `INVALID_FRAME_HEADER` (0x0400), `VERSION_MISMATCH` (0x0460) |
| **CAPABILITY-13** | `0x0580 - 0x05FF` | `PERMISSION_DENIED` (0x0580), `INVALID_CONFIGURATION_SIGNATURE` (0x05FA) |
| **INTENT-7** | `0x0640 - 0x06FF` | `INVALID_PAYLOAD_SCHEMA` (0x0640), `UNKNOWN_INTENT_VERB` (0x064A) |
| **INTENT-7-SECURE** | `0x07D0 - 0x07FF` | `MTLS_HANDSHAKE_FAILED` (0x07D0), `UNTRUSTED_PEER_UID` (0x07DA) |

---

## 7. Traceability & Audit
Every transaction in CI-144 is fully traceable via the W3C Trace Context standard:
```
traceparent: 00-<trace-id>-<span-id>-01
             │    │          │        └─ trace-flags
             │    │          └────────── 64-bit Span ID
             │    └───────────────────── 128-bit Trace ID
             └────────────────────────── version
```
- The `traceparent` originates in INTENT-7 `metadata`.
- It is bound to the TLS Session ID in INTENT-7-SECURE.
- It is embedded in the HXR record for L3 memory.
- Enables full causal chain auditing across process/network boundaries.

---

## 8. Quick Start
1. **Read the Specs**: Start with [BIND-19](https://github.com/CommonIntents/BIND-19) to understand the transport framing.
2. **Implement a Client**: Use the 8-byte header structure to encode/decode frames.
3. **Secure Your Channel**: Implement `mTLS` or `SO_PEERCRED` as defined in INTENT-7-SECURE.
4. **Declare Intents**: Use INTENT-7 verbs (FETCH, WRITE_NODE, TENTACLE) to build semantic flows.

---

## 9. Contributing
We adhere to a strict RFC (Request for Comments) process.  
Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting proposals.

## 10. Security
Security is the foundation of CI-144.  
For vulnerability reporting, see [SECURITY.md](SECURITY.md).

---

**CommonIntents-144 © 2026 - Present**  
**Licensed under Apache 2.0**
