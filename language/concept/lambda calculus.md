# Lambda Calculus

### JavaScript Lambda

expression :: = variable
              | expression expression
              | lambda variable expression
              | (expression)

```js
const I = a => a

// function are curried. beta reduction. beta normal form.
// ~ = lambda
// ~M f = ff
// M(I) == II = I ( beta normal form )
// M(M) == Infinite ( omega combinator )
```

### Resources
- [Lambda Calculus](https://www.youtube.com/watch?v=3VQ382QG-y4 )
- [What is Y combinator](https://stackoverflow.com/questions/93526/what-is-a-y-combinator)
- [How to succeed at recursion without really recursing](https://mvanier.livejournal.com/2897.html)