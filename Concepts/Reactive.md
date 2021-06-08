# Reactive

- With `rxSwift`, variable types should always be defined with let. You don't want to ever replace a Variable, you just want to push new data into one.

- When using Rx fully, you will usually find that your view models consist of a bunch of let's and a single constructor. It's unusual to have any other methods or even computed properties.

