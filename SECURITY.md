# SECURITY.md

[![简体中文](https://img.shields.io/badge/文档-简体中文-3671c9)](SECURITY.zh-CN.md)

## Ecosystem Security Policy

**Version**: v0.3.2
**Status**: Active, long-term enforcement
**Last Updated**: 2026-05-23

---

## 1. Security Philosophy

The CommonIntents ecosystem adheres to the principle of **trust minimization**.

- **Do not trust the submitter's claims.** Every adapter entering the shared knowledge tree must undergo automated review and cryptographic signing.
- **Do not rely on manual review.** Security is programmatic. AI reviews AI, programs review programs, and Tuck serves as the final safety net. Humans intervene only in appeals — as the supreme court, not the daily police.
- **Do not bind to any platform.** The shared knowledge tree is based on IPLD DAG with CID content addressing. GitHub can perish, Cloudflare can perish, any single service provider can perish. CIDs endure. The entry point to the knowledge tree is the content hash, not a domain name.
- **Do not depend on external infrastructure.** Dependence is always passive. The ecosystem must strengthen itself: any node can become a distribution node for the knowledge tree, and anyone can independently verify the signature and integrity of an adapter without trusting any third party.
- **On-demand activation.** Users choose which knowledge tree to load from based on their own security requirements. Security policy is a runtime choice, not a protocol mandate.

**Ecosystem autonomy, flowing smoothly. The task of humans is to continuously improve the review procedures; improving review procedures is to reduce human review.**

---

## 2. Security Grade Definitions

Adapters are classified into four grades based on technical capability boundaries:

| Grade | Definition | Capability Boundary | Runtime Environment Constraint |
|:---|:---|:---|:---|
| **Grade 0** | Pure Function | Data format transformation and schema mapping only. I/O, network, and system calls strictly prohibited. | WASM sandbox, all system interfaces disabled |
| **Grade 1** | Restricted Local I/O | Allowed to read/write specified restricted directories or configuration files. Network access prohibited. | Virtual filesystem mapping sandbox |
| **Grade 2** | Restricted Network Access | Allowed HTTPS access to whitelisted API endpoints. Arbitrary network connections prohibited. | Network whitelist gateway filtering |
| **Grade 3** | System-level Calls | Allowed to execute CLI commands, operate databases, and perform complex network interactions. | Physically isolated container; user bears ultimate risk |

---

## 3. Autonomous Review Pipeline

All adapters submitted to the shared knowledge tree pass through five automated review stages sequentially:

```
Submit (Source Code) → AI Semantic Review → Static AST Review (Source Code) → Trusted Environment Compilation (WASM) → Sandbox Dynamic Review (WASM) → Tuck Automatic Grading & Signing → Enter Knowledge Tree
                                                                                                                      ↘ Cannot Determine → Appeal Queue
```

**Layer 1: AI Semantic Review**

- Analyzes the code structure and CIS/CAP declarations of the adapter
- Detects semantic inconsistencies, over-declaration, and hidden behaviors
- **Only analyzes code structure and protocol declarations; does not read comments, docstrings, or any natural language descriptions**
- AI review results serve only as classification suggestions and reference weights; they must not be the sole basis for admission. The results of Layer 2 (AST) and Layer 3 (Sandbox) hold higher adjudication priority

**Layer 2: Static AST Review**

- Parses the AST, detecting system calls, network access, and file operations
- Network domain whitelist verification
- File path boundary detection
- **Credential and sensitive information scanning**: Detects hardcoded high-entropy strings (suspected keys, passwords, tokens) and non-secure local area network IPs. Submissions are rejected immediately upon discovery of information leakage risks
- Pass or flag as suspicious

**Layer 3: Trusted Environment Compilation**

- Compiles the reviewed source code into WASM bytecode within a TEE or official build pipeline
- The compilation process is reproducible; any third party can independently verify the consistency between the compilation result and the source code
- Pre-compiled binaries submitted locally by the submitter are not accepted
- **Resource Protection**: The build pipeline enforces strict size and complexity limits on submitted source code and implements dynamic rate limiting based on the submitter's CISS certificate to prevent malicious high-frequency submissions from exhausting public compilation resources

**Layer 4: Sandbox Dynamic Review**

- Runs the compiled WASM bytecode in an isolated environment
- Primarily monitors sequences of system calls and network access patterns, rather than complete business logic:
  - Whether undeclared local files are read
  - Whether network connections outside the whitelist are attempted
  - Whether unexpected subprocesses are executed
- Calls to external APIs use restricted behavioral observation, not full functional integration testing
- Compares observed behavior against the Manifest declaration to detect deviations
- Pass or flag as suspicious

**Layer 5: Tuck Final Adjudication**

- Aggregates review results from the previous four layers
- Automatically assigns a grade (Grade 0-3) based on ecosystem security policy
- Cryptographically signs and enters the adapter into the shared knowledge tree
- Only when automatic determination is impossible, the submission is sent to the appeal queue

---

## 4. Appeal Mechanism

When a submitter disagrees with the automatic grading, they may initiate an appeal. Appeals are the only entry point for human intervention.

- The submitter files an appeal request with evidence
- Human reviewers conduct a peer review
- The review result updates the adapter's grading
- Review conclusions form precedents that feed back into the optimization of review rules

---

## 5. Layered Trust and Knowledge Trees

The ecosystem provides multiple layers of knowledge trees; users choose their trust level on demand:

| Knowledge Tree | Maintainer | Trust Level | Entry Characteristics |
|:---|:---|:---|:---|
| **Official Tree** | CommonIntents Maintainers | Highest | Passes complete five-layer review + signature |
| **Community Tree** | All Users | Popularity-driven | Auto-submitted, sorted by popularity; trust weight accumulated by usage frequency and cross-validation |
| **Project Tree** | Project Maintainers | Higher than Community | Verified and signed by the project itself, serving specific scenarios |

Users choose a loading strategy based on their own security requirements:

- **Strict Mode**: Load only officially signed entries
- **Balanced Mode**: Official entries first + community entries sorted by popularity
- **Open Mode**: All entries, sorted by popularity

Security policy is a runtime choice. The protocol does not mandate; users decide for themselves.

---

## 6. Vulnerability Feedback and Ecosystem Self-Healing

Any user (human or AI) can submit a vulnerability report, marking a specific adapter CID as "at risk."

- The weight of a marking action is determined by the identity trustworthiness of the initiator:
  - Officially signed nodes (CommonIntents maintainers): highest weight, effective immediately
  - Verified long-term contributors (CISS mTLS certificate holders): medium weight
  - Anonymous or newly registered nodes: lowest weight, serves only as a reference signal
- There is an upper limit on the number of negative markings a single CISS certificate holder can initiate per unit of time. If a high-weight node exhibits high-frequency, large-scale abnormal marking behavior, its feedback weight is automatically frozen, the relevant adapters are protected with a flag, and the case is forcibly sent to the appeal queue
- When the accumulation of negative markings of varying weights exceeds a dynamic threshold, the adapter is automatically downgraded or marked as unavailable
- The threshold is dynamically adjusted by the security policy, not fixed to a single value
- The AI review program continuously learns from feedback to improve review accuracy
- Human maintainers periodically audit feedback data to optimize review rules

**The ecosystem self-heals. The faster vulnerabilities are discovered, the stronger the protection.**

---

## 7. Relationship with the Protocol Family

| Protocol | How This System References It |
|:---|:---|
| **CIS** | The intent types declared by adapters serve as the comparison baseline for AI semantic review |
| **CAP** | The adapter's Manifest declares business risk level (`securityClass`), complementing the technical security level (Grade) |
| **CISS** | mTLS identity verification ensures traceability of the submitter's identity |
| **CIB** | Format negotiation ensures communication protocol consistency between review tools and adapters |

**Grade is the technical security level** (determined automatically by the review process): what this adapter is technically capable of doing.  
**`securityClass` is the business risk level** (declared by the adapter author in the Manifest): how dangerous this operation is in a business context.  
Together, they form the complete risk profile of an adapter.

---

## 8. Knowledge Tree Independence

The mapping table knowledge tree is an independent public asset of the CommonIntents ecosystem. It is physically isolated and logically independent from the internal knowledge trees of any specific implementation.

- The mapping table knowledge tree stores only translation rules from CIS intents to native operations
- It does not store any private memories, experiential principles, social relationships, or user profiles of any implementation
- The review, signing, and distribution of the knowledge tree are defined by this security policy and do not depend on any external system
- Any CIS/CAP-compatible implementation can load entries from the mapping table knowledge tree; the management of its own internal knowledge tree is completely independent

---

## 9. Platform Independence and Content Addressing

The authoritative source of the shared knowledge tree is the content hash, not the domain name or storage system of any specific service provider.

- Each adapter, after passing review and being signed, is assigned a unique CID. The CID is the adapter's eternal identifier within the ecosystem
- The authoritative entry point to the knowledge tree is a dynamic pointer based on IPNS or DNSLink, which ultimately resolves to the latest, cryptographically verified Root CID. When DNS is available, DNSLink provides a human-readable entry point. When DNS is unavailable, IPNS provides a purely decentralized alternative path. The two serve as mutual backups, ensuring the entry point never breaks
- Any IPFS-compatible gateway, or any node holding a copy of the CID, can provide download and verification services for the adapter
- Users load adapters by CID, unconcerned with where the file is hosted. As long as a single node holds a copy, the knowledge tree persists
- The ecosystem does not depend on any single platform. Service providers may perish; CIDs endure
- The genesis public key used to verify the officially signed knowledge tree is hardcoded and pinned within the client's binary distribution. Key rotation and revocation are enforced through on-chain multisig declarations or mandatory client version upgrades, ensuring the trust root does not rely on any external network request

---

## 10. Known Limitations

This security policy defines the technical security levels and review standards for individual adapters.

- In a multi-adapter orchestration environment, data flowing between nodes can create composite risks (e.g., Grade 1 reads a sensitive file, Grade 2 sends data over the network). This policy does not cover cross-adapter information flow control.
- The detection and mitigation of composite risks are the responsibility of the orchestration engine (e.g., FlowModus) and fall outside the scope of individual adapter security review.

---

## 11. Current Phase and Long-Term Vision

**Current Phase**:

- Human maintainers review all PRs (manual audit)
- Humans sign the review results
- Mapping table files are hosted on multiple independent nodes, with CID serving as the authoritative identifier
- Cryptographic signatures are verified before loading mapping tables

**Long-Term Vision**:

- The full five-layer automated review pipeline is operational
- Tuck performs automatic grading and signing
- The IPLD shared knowledge tree is distributed over the IPFS network, addressed by CID
- The shared knowledge tree does not accept user-locally-compiled binary files. Users submit source code; the official build pipeline compiles and signs it within a trusted environment, achieving reproducible builds
- Signing keys are hosted in Hardware Security Modules (HSM) or Trusted Execution Environments (TEE); the signing process is protected by multi-signature or threshold signature mechanisms
- The dynamic review environment hides virtualization features to prevent sandbox sniffing. The sandbox supports accelerated timeline simulation to detect time-locked delayed backdoors
- The host interpreter process is hardened through operating system-level security mechanisms, ensuring that even if the WASM engine itself has vulnerabilities, they cannot penetrate the host system
- Humans only handle appeals and rule optimization

---

*This document is an ecosystem rule and evolves with the ecosystem. It does not define interaction semantics and is not a protocol specification.*
