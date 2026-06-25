# Acknowledgments & Technical Heritage

This document provides detailed attribution and technical comparison for 
CommonIntents-144 (CI-144) protocol family.

---

## 1. Inspirations and Prior Art

CI-144 stands on the shoulders of giants. We gratefully acknowledge the 
following open standards and projects that inspired our design.

### 1.1 Transport Layer Inspiration

| Standard | What We Learned | Our Innovation |
| :--- | :--- | :--- |
| **HTTP/2 (RFC 7540)** | Frame-based multiplexing, stream prioritization | • Simplified 8-byte frame header (vs 9-byte)<br>• 256 channels with 4 priority queues<br>• 0-RTT UDS implicit negotiation |
| **QUIC (RFC 9000)** | Connection migration, independent streams | • Local-first design with UDS optimization<br>• Binary frame multiplexing without HTTP semantics |

### 1.2 Security Layer Inspiration

| Standard | What We Learned | Our Innovation |
| :--- | :--- | :--- |
| **TLS 1.3 (RFC 8446)** | Mutual authentication, modern cipher suites | • Mandatory mTLS (no optional client auth)<br>• Only 2 strongest cipher suites allowed<br>• L0 Gene Lock certificate pinning |
| **SO_PEERCRED (POSIX)** | Local process identity verification | • 0ms overhead verification for UDS<br>• UID/GID strict matching enforcement |
| **PKCS#11 / TPM** | Hardware security module integration | • Standardized KMS interface support<br>• Credential isolation boundary design |

### 1.3 Capability Layer Inspiration

| Standard | What We Learned | Our Innovation |
| :--- | :--- | :--- |
| **OAuth 2.0 (RFC 6749)** | Capability-based access tokens | • Ed25519 signatures (vs HMAC-SHA256)<br>• TOML configuration (vs Scope strings)<br>• Built-in HITL consensus mechanism |
| **DNSSEC (RFC 4033)** | Signature chain verification | • Gene Lock signature hierarchy<br>• GPG-style key rotation protocol |
| **OPA / Casbin** | Policy-as-code, attribute-based access | • Declarative permission mapping<br>• Dynamic TOML configuration with signatures |

### 1.4 Semantic Layer Inspiration

| Standard | What We Learned | Our Innovation |
| :--- | :--- | :--- |
| **JSON-RPC 2.0** | Remote procedure call pattern | • AI-native verbs (FETCH/WRITE_NODE/TENTACLE)<br>• Mandatory W3C Trace Context integration<br>• HXR-L3 zero-copy memory alignment |
| **W3C Trace Context** | Distributed tracing standard | • Native binding to TLS session<br>• Causal chain across protocol boundaries |
| **OpenAPI** | API specification format | • Intent-first design for AI agents<br>• Execution record ↔ Memory mapping |

---

## 2. Technical Comparison Matrix

### 2.1 BIND-19 vs HTTP/2 vs WebSocket

| Feature | BIND-19 | HTTP/2 | WebSocket | Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Frame Header** | 8 bytes fixed | 9 bytes fixed | 2-14 bytes variable | Simpler parsing, deterministic size |
| **Multiplexing** | 256 channels, 4 queues | Streams, no priority queues | None | Fine-grained AI task scheduling |
| **Version Negotiation** | 0-RTT UDS implicit | ALPN explicit | None | Faster local handshake |
| **Error Handling** | Unified error codes | Separate error frames | Close frames only | Consistent error pipeline |
| **Governance** | IANA-style registry | HTTP/2 working group | W3C | Open, standardized extensions |

### 2.2 CAPABILITY-13 vs OAuth 2.0 vs OPA

| Feature | CAPABILITY-13 | OAuth 2.0 | OPA (Rego) | Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Token Format** | Ed25519 signed | JWT (HMAC/RS256) | N/A (policy engine) | Post-quantum ready, stronger security |
| **Configuration** | TOML + signature | JSON Scope strings | Rego language | Human-readable, cryptographically signed |
| **Consensus** | Built-in HITL | External system | External system | Native human-in-the-loop |
| **Key Rotation** | Built-in GPG-style | External system | N/A | Secure, atomic key transition |
| **Revocation** | Atomic transaction | CRL/OCSP | N/A | Immediate effect, no polling |

### 2.3 INTENT-7 vs JSON-RPC vs GraphQL

| Feature | INTENT-7 | JSON-RPC 2.0 | GraphQL | Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Intent Expression** | AI-native verbs | Method names | Query/Mutation | Closer to AI cognitive model |
| **Tracing** | Native W3C Trace Context | None | None | Full causal chain tracking |
| **Memory Alignment** | HXR ↔ L3 zero-copy | N/A | N/A | Direct execution-to-memory mapping |
| **Validation** | Mandatory JSON Schema | Optional | Schema definition | Strict validation by default |
| **Error Handling** | BIND-19 error codes | JSON-RPC errors | GraphQL errors | Unified error pipeline |

### 2.4 INTENT-7-SECURE vs TLS 1.3 vs SPIFFE

| Feature | INTENT-7-SECURE | TLS 1.3 (mTLS) | SPIFFE/SPIRE | Advantage |
| :--- | :--- | :--- | :--- | :--- |
| **Cipher Suites** | Only 2 strongest | Multiple options | N/A | No weak crypto, simpler audit |
| **Certificate Pinning** | Mandatory (Gene Lock) | Optional | SVID rotation | Prevents CA compromise attack |
| **Local Security** | SO_PEERCRED (0ms) | mTLS on UDS | Unix socket + mTLS | Zero overhead for local trust |
| **Credential Isolation** | Edge Gateway + KMS | Application handles | Secret store | Application never sees credentials |
| **Session Binding** | Traceparent bound to TLS | Session ID only | N/A | Business context in crypto layer |

---

## 3. Standards Compliance

CI-144 is built on industry standards:

| Category | Standard | Compliance Level | Reference |
| :--- | :--- | :--- | :--- |
| **Encryption** | TLS 1.3 (RFC 8446) | Full compliance | Section 2.1 of INTENT-7-SECURE |
| **Signatures** | Ed25519 (RFC 8032) | Full compliance | CAPABILITY-13 key management |
| **Tracing** | W3C Trace Context | Full compliance | INTENT-7 metadata format |
| **Encoding** | JSON (RFC 8259) | Full compliance | INTENT-7 payload format |
| **Certificate Format** | X.509 v3 (RFC 5280) | Full compliance | INTENT-7-SECURE mTLS |
| **Local Identity** | POSIX.1-2001 SO_PEERCRED | Full compliance | INTENT-7-SECURE local transport |

---

## 4. Original Contributions

CI-144 introduces the following novel concepts:

1. **AI-Native Intent Language**: Verbs (FETCH/WRITE_NODE/TENTACLE) designed for AI cognitive patterns
2. **Zero-Copy Memory Alignment**: HXR execution records directly mapped to L3 episodic memory
3. **Local Zero-Trust Verification**: SO_PEERCRED providing 0ms overhead UID/GID verification
4. **Built-in HITL Consensus**: Human-in-the-loop mechanism integrated into capability layer
5. **Unified Error Pipeline**: All protocol errors funneled through BIND-19 error frames
6. **Gene Lock Signature Hierarchy**: DNSSEC-style signature chain for capability mappings

---

## 5. Community and Ecosystem

We welcome contributions from the community. For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

For security concerns, see [SECURITY.md](SECURITY.md).

---

## 6. License

CI-144 is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

---

**"Trust must be proven, not assumed."**
