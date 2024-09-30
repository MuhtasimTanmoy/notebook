# Zero Knowledge Proof

Ethereum layer 2 scaling has needs for running expensive compute offchain with efficient verification on chain.

- Zero knowledge
    - Polynomial Commitment Scheme
        - KZG Polynomial Commitment Scheme
        - FRI
        - Binius
    - Interactive oracle proof
        - Fiat shamir transformation makes it non-interactive
    - Arithmatic Circuits and Constrains System
        - R1CS
    - PLONK, Groth16
    - Proof composition
        - Sum check protocol
        - GKR Protocol
    - Optimize
        - Prover efficiency
        - Prover succintness
        - Verifier efficiency
        - Trusted setup
        - Recursive SNARK

- Rollup
    - Optimistic rollup
        - Post data to layer 1 and assume it's correct
        - Use fraud proofs
        - Withdrawal time long, so liquidity exits are given by hop protocol and connext
    - ZK Rollup
        - Should be validity rollup, as ZK property noy used in general, succintness is used
        - Use validity proofs
        - ZK-SNARK - validity proof
        - zkSync
        - Computational extensive

- Rollups
    - Sidechain
    - All transactions are handled in the sidechain
    - SNARK
        - ZK Rollups
            - Loopring
            - Deversifi
            - zkSync
        - Optimistic rollups
            - Optimism

- Channels
    - State channels
        - Raeden
        - Lightening
    - Payment Channels

- Plasma 
    - child chain
    - OMG
    - Polygon Matic

- Sidechains
    - xDai


- [What are Zero-Knowledge Rollups?](https://pixelplex.io/blog/overview-of-zk-rollups/)
- [Rollups and Data Availability - Building a Modular Blockchain Stack](https://youtu.be/PaSa6vvbeRk)

- Projects
    - Polygon Hermez
    - Polygon Nightfall
    - Polygon Miden zkEVM
    - Polygon Zero
    - zkSync Era
    - StarkNet
    - Scroll
    - 

### ZKEVM

- [SNARK / zk SNARK](https://youtu.be/h-94UhJLeck?list=PLj80z0cJm8QErn3akRcqvxUsyXWC81OGq)
    - A succinct proof that something is true
    - Private transactions on the public blockchain
    - Compliance
    - Online both party
    - Maintaining confidentiality
- [Building a SNARK](https://youtu.be/J4pVTamUBvU?list=PLj80z0cJm8QErn3akRcqvxUsyXWC81OGq)
- [ZKEVM](https://pixelplex.io/blog/zkevm-explained)
- [ZKSync](https://era.zksync.io/docs/reference/concepts/zkSync.html#the-state-of-zksync)

### References
- [Modern Zero Knowledge Cryptography](https://zkiap.com)
- [Introduction to ZK](https://learn.0xparc.org/materials/circom/learning-group-1/intro-zkp)
- [Zero Knowledge Proofs MOOC](https://zk-learning.org)
- [Awesome zero-knowledge proofs (zkp)](https://github.com/matter-labs/awesome-zero-knowledge-proofs)