# System Design Interview

### Chapter 1
- Relational Database

- Non-relational Database
    - key-value stores 
    - graph stores
    - column stores
    - document stores

- Why non-relational
    - Your application requires super-low latency.
    - Your data are unstructured, or you do not have any relational data.
    - You only need to serialize and deserialize data (JSON, XML, YAML, etc.). 
    - You need to store a massive amount of data.

- Vertical Scaling
    - Vertical scaling has a hard limit. It is impossible to add unlimited CPU and memory to a single server.
    -  Vertical scaling does not have failover and redundancy. If one server goes down, the website/app goes down with it completely.

- Load balancer with private IP to support webtier
- Data tier
    - Master slave
- Cache tier
    - Read through cache
- CDN
    - Cache static assets
- Stateless web tier
    - NoSQl to handle session data
- Data centers
    - geo-DNS routed
- Message Queue
- Logging, metrics, automation
- Database shrad
    - Celebrity problem
    - Join and de-normalization

• Keep web tier stateless
• Build redundancy at every tier
• Cache data as much as you can
• Support multiple data centers
• Host static assets in CDN
• Scale your data tier by sharding
• Split tiers into individual services
• Monitor your system and use automation tools

### Chapter 2

### Chapter 14
- Design Youtube
- Familiar model
- Apple, Xiaomi device codec error

### Chapter 15
- Google Drive
- Familiar model