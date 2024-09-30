# Elixir

Elixir is among the most practical functional languages to date. It cherry-picked some of the best.

- Clojure Features.
— Efficient, Immutable Data Structures.
- Optional lazy evaluation.
- Protocols and records/structs. 
- Functional languages promote decoupling data from code.
    - Instead of class, we have modules which are collections of functions.
    - Instead of calling a method on an object call 

Contrary to Clojure it also enjoys true tail call optimization and the pipeline operator.

Finally, it has a pleasant, modern, Ruby-like syntax, a rare gem among functional languages.

- Atom
    - Maintains atom table.
    - String value is kept in table.
    - Atom holds a reference
    - The `&` sign is the capture operator. It turns function into lambda.

- Higher order function
    - Functions in Elixir are first-class citizens. 
    - This means that functions can be passed along as arguments to other functions. This also means that functions can return other functions as values.

- List comprehension
    - See python
        - new_list = [expression for a member in iterable (if conditional)]

    - Being an FP language, Elixir has no loops

    - In fact, all of Elixir’s data structures are immutable

    - {[head | tail], {:atom, msg}} = {[1, 2, 3], {:atom, "PATTERN MATCHING FTW!"}}

    - [1, [2], [[3, 4], 5]] |> List.flatten |> Enum.map(fn x -> x * x * x end)

    - In object-oriented languages, we create objects. In Elixir, we spawn processes

    - Each process can communicate with other processes via message passing. The receiver of the message can choose to act upon the message if it understands it.

    - It is important to note that Elixir processes are not the same as operating system processes or threads. Elixir processes are very lightweight and are managed by the VM.

    - Message passing in process.

- Tail Call Optimization
    - Instead of stack-based recursion, perform it like go to or jump instruction 

```elixir
defmodule Playground do
 for x <- [1, 2, 3] do
 x * x
 end

 for x <- [1, 2, 3], y <- [1, 2, 3], do: {x, y, x * y}

 table =
 for x <- 1..9, y <- 1..9, into: %{} do
 {{x, y}, x * y}
 end

 table =
 for x <- 1..9, y <- 1..9, x < y, into: %{} do
 {{x, y}, x * y}
 end
end

# defmodule Playground do
# Enum.map([1, 2, 3], fn x -> x * 2 end)
# [2, 4, 6]

# Enum.filter(
#  [1, 2, 3],
#  fn x -> rem(x, 2) == 1 end
#  )
# [1, 3]

#   Enum.reduce([1,2,3,4,5], 0, fn x, y -> x + y end)
#   Enum.reduce([1,2,3,4,5], 10, fn x, y -> x + y end)
# end

### x = 0, y = 1 => 1
### x = 1, y = 2 => 3
### x = 3, y = 3 => 6
### x = 6, y = 4 => 10
### x = 10, y = 5 => 15

### x = 10, y = 1 => 11
### x = 11, y = 2 => 13
### x = 13, y = 3 => 16
### x = 16, y = 4 => 20
### x = 20, y = 5 => 25

# defmodule Playground do
#   def start(n) do
#     start = :os.system_time(:seconds)
#     fib = getNumber(n)
#     finish = :os.system_time(:seconds)
#     diff = finish - start
#     IO.puts("Fib is #{fib}")
#     IO.puts("took: #{diff}")
#   end

#   def getNumber(n) when n < 0, do: :error
#   def getNumber(n), do: getNumber(n, 1, 0)
#   defp getNumber(0, _, result), do: result
#   defp getNumber(n, next, result), do: getNumber(n - 1, next + result, next)
# end

### getNumber(10) -> getNumber(10, 1, 0)
### getNumber(9, 1, 1) -> getNumber(8, 2, 1)
### getNumber(7, 3, 2) -> getNumber(6, 5, 3)
### getNumber(5, 8, 5) -> getNumber(4, 13, 8)
### getNumber(3, 21, 13) -> getNumber(2, 34, 21)
### getNumber(1, 55, 34) -> getNumber(0, _, 55) => 55

### getNumber(5) -> getNumber(4) + getNumber(3)
### (getNumber(3) + getNumber(2)) + (getNumber(2) + getNumber(1) [1])
### (1 + 0 + 1) + (1 + 0)  + (1 + 0) + 1 = 5
### getNumber(6) -> getNumber(5) [5] + getNumber(4)

# defmodule Playground do
#   def sum([]), do: 0

#   def sum([h | t]) do
#     h + sum(t)
#   end
# end

# def loop_forever do
#   loop_forever()
# end

### sum([1, 2, 3, 4, 5]) => h = 1, t = [2, 3, 4, 5]
### 1 + sum([2, 3, 4, 5]) => h = 2, t = [3, 4, 5]
### 1 + 2 + sum([3, 4, 5]) => h = 3, t = [4, 5]
### 1 + 2 + 3 + sum([4, 5]) => h = 4, t = [5]
### 1 + 2 + 3 + 4 + sum([5]) => h = 5, t = []
### 1 + 2 + 3 + 4 + 5 + sum([])

# defmodule Playground do
#   def print(0), do: :ok

#   def print(n) do
#     print(n - 1)
#     IO.puts(n)
#   end
# end

### print(10) => 10 -> print(9)
### print(9) => 9 -> print(8)
### ...
### print(2) => 2 -> print(1)
### print(1) => 1 -> print(0)
### print(0) => :ok
```