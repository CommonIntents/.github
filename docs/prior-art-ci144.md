# Prior Art — CI-144 Protocol Family Defensive Publication (Four-Layer Protocol Stack)

> **Nature**: Defensive Publication. This document publicly discloses the core
> innovations of the CI-144 protocol family in a verifiable manner, establishing
> "prior art" evidence that prevents third parties from patenting the same or
> similar technical solutions and later asserting against them.
> **Publication date**: 2026-09-06 (GitHub commit timestamp is immutable evidence)
> **Normative basis**: phyt-DNA methodology `docs/PROTECTION.md` (Prior Art as Code spec)
> **Organization**: CommonIntents · all repositories Apache 2.0
>
> **Legal foundation**: 35 U.S.C. §102(a)(1) (US) / EPC Art. 54(2) (EU) / China's
> first-to-file Patent Law — technology publicly disclosed before a filing date
> cannot constitute novel patentable matter. This document together with the
> public history of each protocol repository constitutes disclosure evidence.

---

## 0. Family Overview

CI-144 is a four-layer decoupled protocol stack: **Semantics (INTENT-7) →
Capability (CAPABILITY-13) → Security (INTENT-7-SECURE) → Transport (BIND-19)**,
plus two extension protocols (PFP-xCF14 physical features, SAP-xCF14 security
assertions).

| Layer | Repository | spec status | Core innovation (claimed here) |
|---|---|---|---|
| Semantics | INTENT-7 | v0.7.0-draft | 7-core-field intent semantics + `x-` extension prefix + minimal syntax layer that does not define behavior |
| Capability | CAPABILITY-13 | v0.3.0-draft | HITL decision queue + node_type/status open enums + custom_scopes reserved region |
| Security | INTENT-7-SECURE | v0.3.0-draft | SO_PEERCRED zero-overhead local identity verification + optional mTLS 1.3 + credential isolation |
| Transport | BIND-19 | v2.0-alpha | 8-byte fixed frame header + 256-channel multiplexing + 0-RTT version negotiation + heartbeat |
| Extension | PFP-xCF14 | v1.0 frozen | 4-byte fixed-offset physical context header (<100ns hard real-time) |
| Extension | SAP-xCF14 | v1.0 | 28-byte security assertion layer (replay protection + dual signature) |

---

## 1. Architecture-Level Innovations

### PA-1: Four-Layer Decoupled Protocol Stack (semantics/capability/security/transport)

- **Content**: Human-AI interaction protocol is split into four independently
  governed layers, each evolving, versioning and freezing independently; the
  semantics layer describes only "what the intent is", capability only "who may
  do what", security only "how identity is proven", transport only "how frames
  travel". Layers connect via open enums and extension reserved regions, never
  depending on each other's frozen fields.
- **Innovation**: ① the responsibility-boundary split of the stack (vs. monolithic
  or only 2-3 layer protocols); ② independent versioning and independent freeze
  policy per layer, allowing draft and frozen states to coexist within one family.
- **Evidence**: `commonintents/{INTENT-7,CAPABILITY-13,INTENT-7-SECURE,BIND-19}/spec/`
  + `.github/CONTRIBUTING.md` (extension reserved regions).

### PA-2: Extension Reserved Region Mechanism (`x-` prefix + open enums + custom_scopes)

- **Content**: The family reserves three channels for application-side extensions
  before spec freeze — INTENT-7 verb `x-*` prefix, CAPABILITY-13 `node_type`/`status`
  open enums (unknown → lenient degradation), and the `custom_scopes` segment.
  Extensions land first as "local extensions" (MVP), then are contributed back
  to the spec once mature.
- **Innovation**: extensions cannot break protocol evolution while the spec is
  unfrozen — local extensions are naturally upgrade-compatible, no breaking-change
  channel required.
- **Evidence**: `.github/CONTRIBUTING.md` reserved-region table + open enum
  definitions in each protocol spec.

### PA-3: W3C Trace Context End-to-End Audit (cross-layer unified observability)

- **Content**: All layers share one trace context semantics (W3C-compatible), so
  a call can be traced end-to-end from the UI interaction surface to internal
  organ invocation, providing a unified observability baseline for audit and
  white-box inspection.
- **Evidence**: trace field definitions in each protocol spec.

---

## 2. Transport-Layer Innovations (BIND-19)

### PB-1: 8-Byte Fixed Frame Header + 256-Channel Multiplexing

- **Content**: Fixed 8-byte frame header (magic + channel + length + flags);
  256 logical channels multiplexed within one physical stream; frame delimiting
  with zero ambiguity.
- **Innovation**: fixed-offset frame header design (no variable-length parsing
  state machine), O(1) parse complexity, suited to embedded and low-latency
  scenarios.
- **Evidence**: `commonintents/BIND-19/spec/` frame format + parser in the BIND-19
  implementation repository.

### PB-2: 0-RTT Version Negotiation

- **Content**: version negotiation completes on the first frame with no extra
  handshake round-trip (0-RTT), coexisting old/new versions.
- **Evidence**: `commonintents/BIND-19/spec/`.

### PB-3: Pluggable PFP/SAP Security Extensions

- **Content**: transport does not embed security; optional extension headers
  (PFP physical features, SAP security assertions) stack on demand — transport
  and security are decoupled.
- **Evidence**: `commonintents/BIND-19/spec/` + standalone `PFP-xCF14`/`SAP-xCF14`
  specs.

---

## 3. Capability-Layer Innovations (CAPABILITY-13)

### PC-1: HITL Decision Queue (human-in-the-loop approval gate)

- **Content**: high-risk intents are not executed directly; they enter a human
  decision queue where a human releases or rejects by button press; unreleased
  intents are physically unreachable to the executor.
- **Innovation**: raising "human approval" from application logic to protocol-level
  capability — any CAPABILITY-13 executor gains an identical human supervision
  gate, enforced physically by queue deadlock (not a soft flag).
- **Evidence**: HITL section of `commonintents/CAPABILITY-13/spec/`.

### PC-2: SemanticSnapshot + view_hash Consensus Anchor

- **Content**: UI state is published as SemanticSnapshot (node_type open enum +
  status open enum + view_hash signature baseline); consumers confirm by
  "what you see is what you sign".
- **Innovation**: UI state becomes signable, verifiable and degradable (unknown
  lenient rendering) — a protocol-level foundation for human-machine consensus.
- **Evidence**: `commonintents/CAPABILITY-13/spec/` + Cellrix reference implementation.

---

## 4. Security-Layer Innovations (INTENT-7-SECURE)

### PS-1: SO_PEERCRED Zero-Overhead Local Identity Verification

- **Content**: in local UDS scenarios, the kernel SO_PEERCRED socket option
  yields the peer process's real identity (PID/UID) with zero network overhead
  and zero extra handshake.
- **Innovation**: identity verification sinks into a kernel socket option,
  introducing no certificate/key-exchange cost — local and remote security use
  different mechanisms, selected by scenario.
- **Evidence**: `commonintents/INTENT-7-SECURE/spec/`.

### PS-2: Credential Isolation (labels travel, credentials do not)

- **Content**: cross-component calls carry only identity labels
  (identity_labels); raw credentials (OAuth token/API key) stay locked in the
  authorizer's vault; consumers never obtain raw credentials.
- **Innovation**: "zero-trust credentials" as a protocol-level constraint —
  credential exposure surface converges to a single custodian.
- **Evidence**: `commonintents/INTENT-7-SECURE/spec/` + Anaphase/Tuck implementations.

### PS-3: Optional mTLS 1.3 Channel

- **Content**: remote scenarios may opt into mTLS 1.3, dual-track with local
  SO_PEERCRED.
- **Evidence**: `commonintents/INTENT-7-SECURE/spec/`.

---

## 5. Semantics-Layer Innovations (INTENT-7)

### PI-1: Minimal Syntax Layer + No Behavior Definition

- **Content**: the intent protocol defines only the syntactic shape of intents
  (7 core fields) and explicitly does not define behavioral semantics; behavior
  adaptation is left to downstream orchestrators. Syntax stays minimal to avoid
  semantic bloat.
- **Innovation**: syntax/semantics separation — the protocol constrains expression
  structure, not execution results; implementers adapt freely.
- **Evidence**: `commonintents/INTENT-7/spec/`.

### PI-2: AI-Native Intent Description (distinct from UI actions)

- **Content**: intent fields target AI-native expression (x-fetch-memory /
  x-write-l3 / x-enter-dream, etc.), not serialized mouse/keyboard actions —
  intent is semantics; actions are implementation details.
- **Evidence**: verb table in `commonintents/INTENT-7/spec/`.

---

## 6. Extension Protocol Innovations

### PX-1: PFP-xCF14 Physical Feature Header

- **Content**: 4-byte fixed-offset physical context header (magic 0xCF14)
  carrying physical context features, aimed at <100ns hard real-time, stacked
  independently of the transport layer.
- **Evidence**: `commonintents/PFP-xCF14/spec/` (v1.0 frozen).

### PX-2: SAP-xCF14 Security Assertion Layer

- **Content**: 28-byte security assertion layer; replay protection (nonce time
  window) + dual signature (content signature + session signature), pluggable
  on transport frames.
- **Evidence**: `commonintents/SAP-xCF14/spec/` (v1.0).

---

## 7. Reference Implementations and Ecosystem Evidence

| Reference implementation | Repository | Relationship to CI-144 |
|---|---|---|
| Cellrix | Jasonmilk/Cellrix | INTENT-7 spec §15 legal reference implementation + testbed (semantics/capability consumer) |
| Tuck | Jasonmilk/Tuck | CI-144 four-layer control executor (security SO_PEERCRED verification + capability HITL/tokens) |
| Anaphase | Jasonmilk/Anaphase-Helix | orchestrator + intent producer (`x-` prefixed intents) |
| BIND-19 | CommonIntents/BIND-19 | transport implementation (v2.0-alpha, 140+ tests, 33 test vectors) |
| Helix-Mind | Jasonmilk/Helix-Mind | subconscious consumer (UDS Daemon reuse) |

Ecosystem application (ADR-0023) proves: the four-layer stack plus reserved-region
mechanism already supports "driving/partner/survival" three-mode control (Tuck
issues Capability Scopes per mode, physically blocking illegal intents at the
channel layer).

---

## 8. Disclosure Scope and Boundary

- **Disclosed**: descriptive innovations of protocol structure and mechanism
  (as above).
- **Not disclosed**: implementation-level trade secrets (e.g., internal parameters
  of specific algorithms, unpublished process details) — defensive publication
  protects only public innovations that could be scooped, never implementation
  secrets.
- **Update policy**: when protocol evolution produces new mechanisms, this
  document is appended under the same spec (modular append, never rewrite history).
