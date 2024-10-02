# Translation lookaside Buffer

- A process address space is divided into pages
- Main memory is divided into frames
- Page table maps the above two
    - Pages to Frame
- Page Table is big enough is also divided into pages residing in main memory
    - Multi-level pages
- CPU generates logical address
    - Page Number + Page Offset
- Now accessing the page table and then getting the frame can be skipped
- TLB caches this mapping which is faster than ram

### Reference
- [Translation Lookaside Buffer(TLB) in Operating System](https://www.youtube.com/watch?v=Z2T2vnyZl0o)