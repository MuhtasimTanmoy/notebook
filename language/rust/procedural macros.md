# Procedural Macro

- In compile time, given the stream of rust tokens it will replace those with expanded new ones. In short, given a piece of code, it returns some other code to run instead.
    - `Function like macro` `vec![1, 2, 3];`
    - `Derive Macro` (TokenStream) -> (TokenStream)
    - `Attribute Macro`
        - In case you have defined lots of macros and commonly used macros are duplicated, it is needed
> A lexer is a software program that performs lexical analysis. Lexical analysis is the process of separating a stream of characters into different words, which in computer science we call 'tokens'. When you read my answer you are performing the lexical operation of breaking the string of text at the space characters into multiple words

> A parser goes one level further than the lexer takes the tokens produced by the lexer and tries to determine if proper sentences have been formed. Parsers work at the grammatical level, lexers work at the word level.

- Procedural Macros are macros defined with `procedural code`

- `cargo-expand` can be used to see generated code. Get one level of expansion
- `syn` token stream parser
- `quote` ast to tokenstream
- `cargo t` to test

```rust

// `macro_rules` lets you write other macros.

// Example serde, derive macro
#[derive(Serialize, Deserialize)]
struct Foo {
 bar: usize,
}

//It will generate something like
impl Serialize for Foo {
    ...
}

```
### Implementation
- `cargo check` to check if compiles without building
- `cargo build` to build the actual project
- `cargo expand --test test derive_new`
- [Sample Codebase](https://github.com/azriel91/proc_macro_rules)