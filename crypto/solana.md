# Solana

- Stack Machine
    - In the stack machine, data is available at the top of the stack by default. 
    - The stack acts as a source and destination, push and pop instructions are used to access instructions and data from the stack.
    - There is no need to pass the source and destination address because the default address is top of the stack. 
    - In the stack machine, there is no need to pass explicit addresses in the instruction. 
    - Therefore the instruction format consists only of the `OPCODE (Operation Code)` field. 
    - This instruction format is known as Zero address instruction
    - Software stack machines re-emerge as blockchain and web streaming become popular
    - Stack machines boast better code density than register machines
    - Stack machine is much simpler than register machines
    - Examples: WebAssembly, TelegramVM, EthereumVM
    - Traditional stack machine codegens are `AST-based`
    - Missing aggressive optimizations
    - LLVM is missing some key infrastructures for stack machine codegen
    -  Repurposing LLVM to emit stack code is intuitively challenging (but doable)
    -  Public `WASM` backend is an attempt but its methodology is rudimentary and not canonical
    -  LLVM is not traditionally good with code size optimization -- need a lot of tunings.

- EVM ( Ethereum Virtual Machine )
    - Stack machine with 256-bit word length
    - Deterministic: no heap, gc, multithreading, floating point, external variables, dynamic jumps
    - Has blockchain-specific instructions
    - Executing each bytecode instruction costs “gas”

- Solidity and Vyper are the only two smart contract languages
    - Solidity is criticized for its bad and unsafe design, and its compiler is not-standardized
    - Vyper is simplistic and Python-based
    - After 5 years we are still not seeing other DSLs emerging. Mostly because the platform needs something like LLVM

-  Most stack machines are designed for size-sensitive scenarios: (eg. blockchain)

- Register allocation pass is replaced by Stackification pass
    - Register-based Instr
    - Stack-based Instr
    - Mapping - (reg -> stack)

- Neon EVM enables dApss to harness advantages from both blockchains 
- Ethereum in terms of tools used, and Solana in terms of low gas fees and high throughput
- Generating Stack Machine Code using LLVM

- [Type of Instructions](https://www.geeksforgeeks.org/computer-organization-instruction-formats-zero-one-two-three-address-instruction/)
    - A stack-based computer does not use the address field in the instruction. 
    - To evaluate an expression first it is converted to reverse Polish Notation i.e. Postfix Notation. 
    - Then instructions without any address used for operations

- Solana Funbdamentals
    - [Proof of history](https://medium.com/solana-labs/proof-of-history-a-clock-for-blockchain-cf47a61a9274)
    - [Proof of work](https://grisha.org/blog/2018/01/23/explaining-proof-of-work/)
    - [Tower BFT](https://medium.com/solana-labs/tower-bft-solanas-high-performance-implementation-of-pbft-464725911e79)
    - [Gulf Stream](https://medium.com/solana-labs/gulf-stream-solanas-mempool-less-transaction-forwarding-protocol-d342e72186ad)
    - [Sea Level VM](https://medium.com/solana-labs/sealevel-parallel-processing-thousands-of-smart-contracts-d814b378192)
    - [Solana Whitepaper](https://solana.com/solana-whitepaper.pdf)

#### References
- [Solana Bootcamp](https://www.soldev.app/library/playlist/solana-bootcamp-advanced)
- [Sea level VM](https://medium.com/solana-labs/sealevel-parallel-processing-thousands-of-smart-contracts-d814b378192)
- [Solana Improvement Proposal](https://github.com/solana-foundation/solana-improvement-documents/tree/main/proposals)