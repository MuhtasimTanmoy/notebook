- Github link
    - https://github.com/Clivern/Beaver

## Setup

- `cp config.yml config.dist.yml`

- Redis dependency check
    - `brew install redis`

- Certificate generate
    - `openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem`

## Run it
- go build beaver.go
- go run beaver.go
