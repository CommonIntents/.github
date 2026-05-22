> **CommonIntents** — the open protocol family for AI-native interaction.
> CIS defines *what* AI wants. CAP defines *what* AI can do.
> **Trust must be proven, not assumed.**

---

### 📖 Where to start?

| I want to... | Start here |
|:---|:---|
| Understand the big picture | [Constitution](#cis-cap-protocol-family-constitution) (scroll down) |
| Integrate CIS into my tool | [CIS Specification](https://github.com/CommonIntents/CIS) → [Mapping Guide](https://github.com/CommonIntents/CIS/blob/main/guides/mapping-guide.md) |
| Add HITL approval to my workflow | [CAP Specification](https://github.com/CommonIntents/CAP) |
| Understand how transport binding works | [CIB Specification](https://github.com/CommonIntents/CIB) |
| Set up secure mTLS transport | [CISS Specification](https://github.com/CommonIntents/CISS) |
| See a working reference implementation | [Cellrix](https://github.com/Jasonmilk/Cellrix) |
| Contribute to the protocols | [Contributing Guide](https://github.com/CommonIntents/.github/blob/main/CONTRIBUTING.md) |

---

# CIS/CAP Protocol Family Constitution

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Org](https://img.shields.io/badge/Org-CommonIntents-darkgray.svg)](https://github.com/CommonIntents)
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

### The Native Language of AI

The reasoning core of AI is non-linguistic. When a human thinks "bring that thing over," this intent, as it forms in the mind, is not Chinese, not English, not any language — it is a pure, pre-linguistic intent. The brain's language center then automatically translates it into the required form of expression.

CIS is the pre-linguistic intent layer for AI. AI does not need to choose among multiple languages, nor does it need to understand the syntax of the underlying backend. It only needs one language — CIS. The existence of all other languages is completely transparent to AI.

### The Water Philosophy

- **Formless**: Poured into CLI, it becomes command parameters; into GUI, click events; into TUI, panel operations. CIS itself has no shape until it falls into a backend and acquires a concrete form.
- **Non-competing**: It does not replace any existing infrastructure. It merely provides an extremely thin, unified semantic layer on top of all infrastructure.
- **Nourishing all things**: Compatible with everything. Swap out a static mapping table, and CIS remains untouched.
- **Ultimate energy efficiency**: Water flows downward, using gravity to do work. CIS uses compile-time deterministic code translation, consuming zero AI Tokens. Translated once, reused forever.

### A World Without Syntax Errors

In the world of CIS, syntax errors do not exist. Only logical errors and philosophical errors exist.

| Error Type | Who Errs | Layer |
|:---|:---|:---|
| Syntax Error | Does not exist | CIS parser directly rejects illegal intents |
| Logical Error | AI | Reasoning layer |
| Philosophical Error | Protocol designer | Protocol layer |

CIS removes syntax from AI's list of responsibilities. AI does not need to worry about "did I say this correctly?" — it only needs to focus on "did I think this correctly?"

---

## 3. Protocol Stack Architecture

```
┌─────────────────────────────────────────┐
│              CIS                         │
│  Common Intent Specification             │
│  · Pure intent semantic standard         │
│  · Transport-agnostic, crypto-agnostic   │
│  · Backend-agnostic                      │
└─────────────────────────────────────────┘
                    ▲ Semantic Binding
┌─────────────────────────────────────────┐
│              CIB                         │
│  CIS/Transport Binding Protocol          │
│  · Transport format negotiation          │
│  · Integrity check negotiation           │
│  · Version compatibility declaration     │
└─────────────────────────────────────────┘
                    ▲ Currently Bound To
┌─────────────────────────────────────────┐
│              CISS                        │
│  Secure Intent & Control Protocol        │
│  · mTLS end-to-end encrypted transport   │
│  · Client certificate identity proof     │
└─────────────────────────────────────────┘
                    ▲ Carried By
┌─────────────────────────────────────────┐
│              CAP                         │
│  Capability Authentication Protocol      │
│  · Capability declaration                │
│  · Asynchronous decision queue           │
│  · Lease extension                       │
│  · Audit extension                       │
└─────────────────────────────────────────┘
```

---

## 4. Layer Responsibilities

| Protocol | One-Line Definition | Analogy |
|:---|:---|:---|
| **CIS** | What AI wants to do | Soul |
| **CIB** | How the message is transmitted | Ligament |
| **CISS** | Who is speaking, and whether the channel is secure | Skeleton |
| **CAP** | What you can do, under what conditions, within what timeframe | Immune System |

---

## 5. Separation of Concerns

| Domain | Responsible Party |
|:---|:---|
| Intent semantics | CIS Protocol |
| Transport binding, format negotiation, integrity | CIB Protocol |
| Interaction standards and security semantics | CAP Protocol |
| Message queue infrastructure | Existing middleware |
| Identity infrastructure | Existing TLS/PKI ecosystem |
| Storage and persistence | Application decides |
| Business permission logic | Application implements |

**The protocol defines only interaction semantic standards. Anything that does not define semantics but only mandates implementation methods is not within the protocol's scope of responsibility.**

---

## 6. Design Principles

1. **Minimal Core, Optional Extensions**: CAP Core contains only irreducible atomic functions.
2. **Declarative Activation, On-Demand Execution**: Advanced features are activated only when explicitly declared; not declared means zero overhead.
3. **Separation of Concerns, Ecosystem Synergy**: Protocol defines semantic standards; infrastructure provides implementation pipelines.
4. **Zero-Dependency Ready, Progressive Enhancement**: Basic compatibility requires only HTTP + JSON.
5. **Maximum Embrace, Minimum Exclusion**: Define only "what is correct," not "how to do it."
6. **Semantically Pure, Transport-Agnostic, Backend-Agnostic**: CIS is an eternal intent language, isolating all changes through CIB and the static mapping layer.

---

## 7. Protocol Status

| Protocol | Status | Responsibility |
|:---|:---|:---|
| **CIS** | Existing, continuously evolving | Common intent semantic standard |
| **CIB** | Drafting in progress | Transport binding, format negotiation, integrity assurance |
| **CISS** | Current implementation based on CIB | mTLS secure transport |
| **CAP** | Drafting in progress | Capability authentication and HITL decisions |
| **CAPS** | Future phase | Decentralized swarm trust network |

| Reference Implementation | Status |
|:---|:---|
| **Cellrix** | Continuously evolving |

---

*This constitution is maintained by the CIS/CAP Protocol Working Group.*
