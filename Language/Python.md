# Python

Just In Time compilation is a method to convert, at runtime, the execution of datastructures into machine code. This can be a a lot faster than interpreting the datastructures, as you are dealing directly with the processor and can apply optimisations that aren't usually possible in the source language.



## Django Project Setup Code Snippet
- `virtualenv` activate


```sh

pip3 list -v
pip3 install -r requirements.txt

# Check for foriegn key.
python manage.py makemigrations user
python manage.py makemigrations adserver

python manage.py migrate 

# Create user
python manage.py createsuperuser

# login

```


# Reference
- [Jit Compilation](https://www.youtube.com/watch?v=sQTOIkOMDIw)
- [How Do Python Coroutines Work?](https://www.youtube.com/watch?v=idLtMISlgy8) - Explains