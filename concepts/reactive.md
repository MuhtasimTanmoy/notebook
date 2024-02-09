# Reactive

- Operator
- Subject

- With `rxSwift`, variable types should always be defined with let. You don't want to ever replace a Variable, you just want to push new data into one.

- When using Rx fully, you will usually find that your view models consist of a bunch of let's and a single constructor. It's unusual to have any other methods or even computed properties.

- Avoid any UI-related code in your viewModel. It includes RxCocoa extensions and drivers. ViewModel should focus specifically on business logic. Drivers are meant to be used to drive UI, so leave them for ViewControllers

- Try to avoid Variables and Subjects if possible. AKA try to make everything "flowing". Function into function, into function and so on and, eventually, in UI. But be afraid of subjects overuse - otherwise your project will become hard to maintain and scale in no time.


## Resources
- [RX Example](https://github.dev/JussiSuojanen/friends/tree/RxSwift/Friends)