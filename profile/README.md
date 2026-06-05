> **CommonIntents-144** — the open protocol family for AI-native interaction.
> INTENT-7 defines *what* AI wants. CAPABILITY-13 defines *what* AI can do.
> **Trust must be proven, not assumed.**

---

### 📖 Where to start?

| I want to... | Start here |
|:---|:---|
| Understand the big picture | [Constitution](#cin7-cic13-protocol-family-constitution) (scroll down) |
| Integrate INTENT-7 into my tool | [INTENT-7 Specification](https://github.com/CommonIntents/INTENT-7) → [Mapping Guide](https://github.com/CommonIntents/INTENT-7/blob/main/guides/mapping-guide.md) |
| Add HITL approval to my workflow | [CAPABILITY-13 Specification](https://github.com/CommonIntents/CAPABILITY-13) |
| Understand how transport binding works | [BIND-19 Specification](https://github.com/CommonIntents/BIND-19) |
| Set up secure mTLS transport | [INTENT-7-SECURE Specification](https://github.com/CommonIntents/INTENT-7-SECURE) |
| See a working reference implementation | [Cellrix](https://github.com/Jasonmilk/Cellrix) |
| Contribute to the protocols | [Contributing Guide](https://github.com/CommonIntents/.github/blob/main/CONTRIBUTING.md) |

---

# INTENT-7/CAPABILITY-13 Protocol Family Constitution

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Org](https://img.shields.io/badge/Org-CommonIntents--144-darkgray.svg)](https://github.com/CommonIntents)
[![简体中文](https://img.shields.io/badge/文档-简体中文-3671c9)](README.zh-CN.md)

**Version**: 1.0.0-draft
**Status**: Working Group Internal Draft
**Date**: 2026-05-22
**License**: Apache 2.0

---

## 1. Problem Statement

Existing AI agent interaction protocols suffer from the following structural deficiencies:

- **Centralized trust root**: Trust anchored in a single Host node; single point of failure leads to global collapse.
- **Static permission model**: Permissions have no time-bound constraints; once granted, held permanently.
- **Blocking human-machine collaboration**: HITL is a synchronous model; the human becomes the system bottleneck.
- **Abdication of security responsibility**: The protocol only handles connections; security implementation is pushed downstream.
- **Mandatory feature design**: All features are forced upon users; no on-demand activation mechanism.

---

## 2. Philosophical Foundation

### Core Belief

**Trust must be proven, not assumed.**

## 3. Protocol Stack Architecture

```
┌─────────────────────────────────────────┐
│              INTENT-7                         │
│  Common Intent Specification             │
│  · Pure intent semantic standard         │
│  · Transport-agnostic, crypto-agnostic   │
│  · Backend-agnostic                      │
└─────────────────────────────────────────┘
                    ▲ Semantic Binding
┌─────────────────────────────────────────┐
│              BIND-19                         │
│  INTENT-7/Transport Binding Protocol          │
│  · Transport format negotiation          │
│  · Integrity check negotiation           │
│  · Version compatibility declaration     │
└─────────────────────────────────────────┘
                    ▲ Currently Bound To
┌─────────────────────────────────────────┐
│              INTENT-7-SECURE                        │
│  Secure Intent & Control Protocol        │
│  · mTLS end-to-end encrypted transport   │
│  · Client certificate identity proof     │
└─────────────────────────────────────────┘
                    ▲ Carried By
┌─────────────────────────────────────────┐
│              CAPABILITY-13                         │
│  Capability Authentication Protocol      │
│  · Capability declaration                │
│  · Asynchronous decision queue           │
│  · Lease extension                       │
│  · Audit extension                       │
└─────────────────────────────────────────┘
```

---

## 5. Separation of Concerns

| Domain | Responsible Party |
|:---|:---|
| Intent semantics | INTENT-7 Protocol |
| Transport binding, format negotiation, integrity | BIND-19 Protocol |
| Interaction standards and security semantics | CAPABILITY-13 Protocol |
| Message queue infrastructure | Existing middleware |
| Identity infrastructure | Existing TLS/PKI ecosystem |
| Storage and persistence | Application decides |
| Business permission logic | Application implements |

**The protocol defines only interaction semantic standards. Anything that does not define semantics but only mandates implementation methods is not within the protocol's scope of responsibility.**

---

## 6. Design Principles

1. **Minimal Core, Optional Extensions**: CAPABILITY-13 Core contains only irreducible atomic functions.
2. **Declarative Activation, On-Demand Execution**: Advanced features are activated only when explicitly declared; not declared means zero overhead.
3. **Separation of Concerns, Ecosystem Synergy**: Protocol defines semantic standards; infrastructure provides implementation pipelines.
4. **Zero-Dependency Ready, Progressive Enhancement**: Basic compatibility requires only HTTP + JSON.
5. **Maximum Embrace, Minimum Exclusion**: Define only "what is correct," not "how to do it."
6. **Semantically Pure, Transport-Agnostic, Backend-Agnostic**: INTENT-7 is an eternal intent language, isolating all changes through BIND-19 and the static mapping layer.

---

## 7. Protocol Status

| Protocol | Status | Responsibility |
|:---|:---|:---|
| **INTENT-7** | Existing, continuously evolving | Common intent syntactic standard |
| **BIND-19** | Drafting in progress | Transport binding, format negotiation, integrity assurance |
| **INTENT-7-SECURE** | Current implementation based on BIND-19 | mTLS secure transport |
| **CAPABILITY-13** | Drafting in progress | Capability authentication and HITL decisions |
| **CAPS** | Future phase | Decentralized swarm trust network |

All protocol specifications are published via content addressing (CID). Their authoritative versions are identified by CID, independent of any specific platform or storage service.

| Reference Implementation | Status |
|:---|:---|
| **Cellrix** | Continuously evolving |

---

*This constitution is maintained by the INTENT-7/CAPABILITY-13 Protocol Working Group.*
