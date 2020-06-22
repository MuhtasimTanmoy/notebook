# Elixir

Meta programmable

- Higher order function
    - Functions in Elixir are first class citizens. This means that functions can be passed along as arguments to other functions. This also means that functions can return other functions as values
- List compreshension
    - See python > new_list = [expression for member in iterable (if conditional)]
    - Being a FP language, Elixir has no loops.
    - In fact, all of Elixir’s data structures are immutable.
    - {[head | tail], {:atom, msg}} = {[1, 2, 3], {:atom, "PATTERN MATCHING FTW!"}} 
    - [1, [2], [[3, 4], 5]] |> List.flatten |> Enum.map(fn x -> x * x * x end)
    - In object-oriented languages, we create objects. In Elixir, we spawn processes.
    - Each process can communicate with other processes via message passing. The receiver of the message can choose to act upon the message if it understands it.
    - It is important to note that Elixir processes are not the same as operating system processes or threads. Elixir processes are very light-weight and are managed by the VM.
    - Message passing in process

Elixir is among the most practical functional languages to date. It cherry-picked some of the best Clojure features — efficient, immutable data structures, optional lazy evaluation, protocols and records/structs. Contrary to Clojure it also enjoys true tail call optimization and the pipeline operator. Finally, it has a pleasant, modern, Ruby-like syntax, a rare gem among functional languages.