# Vault

Secrets
- User Password
- Token
- DB Credential
- TLS
- Secret Sprawl
- In Source Code, auth header, they end up everywhere
- Vault keeps it encrypted, commute TLS as well but application is not good at keeping secrets
    - Log exception
    - Log export to monitoring system
    - Diagnostic output
- Dynamic secrets make moving target
    - Ephimeral
    - Unique token to each one with trace
    - Revokation is isolated

Three main issue solved
- Fix secret sprawl
- Create moving target
- Application data access secured with crypto offload, rotation, versioning, decomissioning


### Vault Course
- Vault secret store