# Conflux
At the heart of Conflux is the `Tree-Graph ledger` structure and the `GHAST` chain selection rule.

- Tree-Graph Consensus Algorithm
    - Paper: https://arxiv.org/pdf/1805.03870.pdf
- GHAST
    - Paper: https://arxiv.org/pdf/2006.01072.pdf

### Webinars
- [Conflux Tree Graph](https://youtu.be/zX-bVTEKOiQ)
    - Nakamoto consensus fork problem is solved with Tree graph consensus
    - TPS is not the deciding factor
    - As ethereum is more decentralized, not unlike Tron with fewer nodes, it attracts more high-value application
    - Uses cases
        - Supply chain finance
        - Valuable information exchange

- [USENIX ATC '20 - A Decentralized Blockchain with High Throughput and Fast Confirmation](https://youtu.be/mZvSIVNHTRk)
    - Larger block size/ faster block generation rate causes more forks
    - Forks waste network/ processing resources
    - Ghost consensus
        - Iteratively advance to child block to the largest subtree
        - Liveness attack mitigated with weighted block
    - Optimization
        - Link cut tree
            - Efficiently maintain weights in Tree Graph
        - Deferred execution
            - Redundant execution rollback

- [Conflux PoW-based GHAST blockchain](https://youtu.be/8rxMrvhzk8Y)
    - Ghost protocol selects the chain with the heaviest subtree rule, whereas Nakamoto consensus does that with the longest chain