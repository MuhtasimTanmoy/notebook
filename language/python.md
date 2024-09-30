# Python

- Just In Time compilation is a method to convert, at runtime, the execution of data structures into machine code. 
- This can be a lot faster than interpreting the data structures, as you are dealing directly with the processor and can apply optimizations that aren't usually possible in the source language.


### Django Project Setup Code Snippet
- `virtualenv` activate

```sh

pip3 list -v
pip3 install -r requirements.txt

# Check for foreign keys.
python manage.py make migrations user
python manage.py make migrations ad server

python manage.py migrate 

# Create user
python manage.py createsuperuser

# login

```

### References
- [Jit Compilation](https://www.youtube.com/watch?v=sQTOIkOMDIw)
- [How Do Python Coroutines Work?](https://www.youtube.com/watch?v=idLtMISlgy8) - Explains