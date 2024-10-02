# Vault

Secrets
- User Password
- Token
- DB Credential
- TLS
- Secret Sprawl
- In Source Code, auth header, they end up everywhere
- Vault keeps it encrypted, and commutes TLS as well but the application is not good at keeping secrets
    - Log exception
    - Log export to the monitoring system
    - Diagnostic output
- Dynamic secrets make moving target
    - Ephemeral
    - Unique token to each one with trace
    - Revokation is isolated

Three main issues solved
- Fix secret sprawl
- Create moving target
- Application data access secured with a crypto offload, rotation, versioning, decommissioning


### Vault Course
- Vault secret store