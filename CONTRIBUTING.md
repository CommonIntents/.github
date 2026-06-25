# Contributing to CommonIntents-144
Thank you for your interest in contributing to CI-144!  
This document outlines the governance model and contribution process.

---

## 1. Governance Model
CI-144 follows a **Meritocratic Governance Model** with clearly defined roles:

| Role | Responsibilities | Requirements |
| :--- | :--- | :--- |
| **Protocol Maintainer** | Final approval on RFCs, version releases, breaking changes | Deep understanding of all 4 protocols; 2+ years contribution history |
| **Working Group Member** | RFC voting, technical review, standard proposal evaluation | Demonstrated expertise in specific protocol layer |
| **Community Contributor** | Bug reports, documentation improvements, implementation feedback | Active participation in discussions |

---

## 2. RFC (Request for Comments) Process
**All changes to core specifications MUST go through the RFC process.**

This ensures:
- Backward compatibility
- Theoretical soundness
- Cross-layer consistency
- No breaking changes without consensus

### 2.1 RFC Submission Workflow
```
┌─────────────────────────────────────────────────────────┐
│  Step 1: Draft RFC                                      │
│  • Create markdown file in spec/drafts/                 │
│  • Use RFC Template (see Section 3)                     │
│  • Include: Motivation, Impact, Security Analysis       │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Step 2: Submit Pull Request                            │
│  • Title prefix: [RFC] Protocol-Name: Brief Title       │
│  • Link to related Issues                               │
│  • Mark as "Draft" initially                            │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Step 3: Community Discussion (14 days minimum)         │
│  • Public comment period on GitHub                      │
│  • Working Group reviews impact on:                     │
│    - Backward compatibility                             │
│    - Security boundaries                                │
│    - Milk Zen philosophy alignment                      │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Step 4: Consensus Vote                                 │
│  • Minor Changes: 2 Maintainer approvals                │
│  • Major Changes: 3 Maintainer approvals                │
│  • Breaking Changes: 3-of-3 Multi-signature from Seeds  │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│  Step 5: Merge & Publish                                │
│  • Update protocol version (SemVer)                     │
│  • Update status matrix in README                       │
│  • Publish to IANA registry (if applicable)             │
└─────────────────────────────────────────────────────────┘
```

### 2.2 RFC Classification

| Classification | Definition | Approval Requirement |
| :--- | :--- | :--- |
| **Minor** | Clarifications, typos, non-normative text | 1 Maintainer |
| **Standard** | New optional fields, error codes, extensions | 2 Maintainers |
| **Major** | New frame types, new verbs, protocol behavior changes | 3 Maintainers |
| **Breaking** | Changes incompatible with existing implementations | 3-of-3 Multi-sig |

---

## 3. RFC Template
When submitting an RFC, use the following structure:

```markdown
# RFC-[NUMBER]: [Title]

## Status
[ ] Draft
[ ] Under Review
[ ] Accepted
[ ] Rejected

## Motivation
Why is this change necessary?

## Proposed Change
Detailed technical specification of the change.

## Impact Analysis

### Backward Compatibility
[ ] Fully Compatible
[ ] Partially Compatible (requires version negotiation)
[ ] Breaking Change

### Security Implications
Describe any security considerations.

### Performance Impact
Describe any performance implications.

## Implementation Notes
Guidance for implementers.

## References
- Related RFCs
- External standards

## Changelog

| Date | Author | Change |
| :--- | :--- | :--- |
| YYYY-MM-DD | Name | Initial draft |
```

---

## 4. Code Contribution Guidelines

### 4.1 Repository Structure
```
CommonIntents/
├── BIND-19/
│   ├── spec/
│   │   └── BIND-19.md          # Protocol Specification
│   └── examples/               # Implementation examples
├── CAPABILITY-13/
│   ├── spec/
│   │   └── CAPABILITY-13.md
│   └── config/
│       └── capability_mapping.toml.example
├── INTENT-7/
│   ├── spec/
│   │   └── INTENT-7.md
│   └── schemas/                # JSON Schemas
├── INTENT-7-SECURE/
│   ├── spec/
│   │   └── INTENT-7-SECURE.md
│   └── certificates/           # Example certificates (self-signed)
└── .github/
    ├── profile/
    │   └── README.md           # Organization Profile
    ├── CONTRIBUTING.md         # This file
    └── SECURITY.md             # Security Policy
```

### 4.2 Code Standards

| Category | Standard |
| :--- | :--- |
| **Specification Language** | English (US), Markdown format |
| **Code Examples** | Rust (preferred), Python, TypeScript |
| **Naming Convention** | snake_case for files, CamelCase for types |
| **Documentation** | All public APIs must have doc comments |

### 4.3 Testing Requirements
- **Unit Tests**: Required for all validation logic
- **Integration Tests**: Required for cross-protocol interactions
- **Compatibility Tests**: Must pass against previous minor version

---

## 5. Extension Guidelines
CI-144 reserves extension ranges for custom implementations:

| Protocol | Reserved Range | Usage |
| :--- | :--- | :--- |
| BIND-19 Frame Type | `0x0F - 0xEF` | Experimental frames |
| CAPABILITY-13 Scopes | `custom_scopes` section | Application-specific permissions |
| INTENT-7 Verbs | `x-*` prefix | Experimental actions |
| INTENT-7-SECURE Error Codes | `0x07F0 - 0x07FF` | Implementation-specific errors |

**Important**: Extensions using reserved ranges MUST NOT conflict with future standard allocations.

---

## 6. Versioning Policy
CI-144 follows **Semantic Versioning 2.0.0**:

| Version Change | Meaning | Example |
| :--- | :--- | :--- |
| **Major (X.0.0)** | Breaking changes | Frame format change, mandatory field removal |
| **Minor (0.X.0)** | New features, backward compatible | New frame type, new verb |
| **Patch (0.0.X)** | Bug fixes, clarifications | Typo fix, documentation update |

**Version Negotiation**: BIND-19 handles version compatibility via 0-RTT handshake. Implementations MUST support all patch versions within a minor version.

---

## 7. Code of Conduct

### 7.1 Our Standards
- **Be respectful**: Treat all contributors with respect and professionalism.
- **Be constructive**: Critique ideas, not people.
- **Be disciplined**: Follow the RFC process; no shortcuts.
- **Be global**: Write in clear English; avoid idioms and slang.

### 7.2 Unacceptable Behavior
- Harassment, discrimination, or offensive language
- Bypassing the RFC process for personal convenience
- Introducing intentional vulnerabilities or backdoors
- Misrepresenting the protocol in external communications

### 7.3 Enforcement
Violations may result in:
- Warning and request to correct behavior
- Temporary ban from contributing
- Permanent ban for severe or repeated violations

---

## 8. Getting Help
- **GitHub Issues**: For bug reports and feature requests
- **GitHub Discussions**: For questions and general discussion
- **RFC Comments**: For technical debates on specific proposals

---

## 9. Acknowledgments
By contributing to CI-144, you agree that your contributions will be licensed under the Apache 2.0 License.

Thank you for helping build the foundation for trustless silicon-native networks.

---

**"Trust must be proven, not assumed."**
