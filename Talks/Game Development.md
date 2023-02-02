# Game Development

- Entity Component System
    - OOP not suitable for game development
    - Think about data structures rather than functions that operate on it
    - Self mutating struct or internal mutability usage for entity object
    - Object indexing
    - Put objects in vector and use index. But on delete of object `use after free` occurs
    - Generational Indexing
        - Using index with a generation field
        - Need type registry to know only about the relevant in global system in anymap.
    - In ECS System an entity is collection of traits
    - Registry Pattern
    - Resource Pattern

# Reference
- [ECS System Design](https://www.youtube.com/watch?v=aKLntZcp27M)