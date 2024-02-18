# python_async_comprehension

## Learning Objectives

How to write an asynchronous generator
How to use async comprehensions
How to type-annotate generators

# **Asynchronous Comprehensions**
---
(taken from peps-python.org on the subject)
___
We propose to allow using async for inside list, set and dict comprehensions. Pending PEP 525 approval, we can also allow creation of asynchronous generator expressions.

Examples:

set comprehension: {i async for i in agen()};

list comprehension: [i async for i in agen()];

dict comprehension: {i: i ** 2 async for i in agen()};

generator expression: (i ** 2 async for i in agen()).

It is allowed to use async for along with if and for clauses in asynchronous comprehensions and generator expressions:

```
dataset = {data for line in aiter()
                async for data in line
                if check(data)}
```
Asynchronous comprehensions are only allowed inside an async def function.

In principle, asynchronous generator expressions are allowed in any context.

However, in Python 3.6, due to async and await soft-keyword status, asynchronous generator expressions are only allowed in an async def function.

Once async and await become reserved keywords in Python 3.7, this restriction will be removed.


# **await in Comprehensions:**
---
(taken from peps-python.org on the subject)
___
We propose to allow the use of await expressions in both asynchronous and synchronous comprehensions:
```
result = [await fun() for fun in funcs]
result = {await fun() for fun in funcs}
result = {fun: await fun() for fun in funcs}

result = [await fun() for fun in funcs if await smth]
result = {await fun() for fun in funcs if await smth}
result = {fun: await fun() for fun in funcs if await smth}

result = [await fun() async for fun in funcs]
result = {await fun() async for fun in funcs}
result = {fun: await fun() async for fun in funcs}

result = [await fun() async for fun in funcs if await smth]
result = {await fun() async for fun in funcs if await smth}
result = {fun: await fun() async for fun in funcs if await smth}
```

This is only valid in async def function body.

# Typing module
In Python, the `typing module` provides a way to add type hints to your code, which can help improve code clarity and catch type-related errors early. Here are some common types available in the typing module:

1. Any: Represents a value of any type. Use this sparingly, as it weakens the type checking.

2. int: Represents an integer.

3. float: Represents a floating-point number.

4. str: Represents a string.

5. bool: Represents a boolean value (True or False).

6. List: Represents a list of elements. You can specify the type of elements in the list using square brackets, e.g., List[int] for a list of integers.

7. Tuple: Represents a fixed-size tuple of elements. You can specify the types of each element, e.g., Tuple[int, str] for a tuple containing an integer and a string.

8. Dict: Represents a dictionary (key-value pairs). You can specify the types of keys and values, e.g., Dict[str, int] for a dictionary with string keys and integer values.

9. Set: Represents a set of unique elements. You can specify the type of elements, e.g., Set[str] for a set of strings.

10. Union: Represents a value that can be one of several types. For example, Union[int, str] indicates a value that can be either an integer or a string.

11. Optional: Represents an optional value, typically used with None. For example, Optional[int] means an integer or None.

12. Callable: Represents a callable object, such as a function. You can specify the argument types and return type, e.g., Callable[[int, str], bool] for a function that takes an integer and a string as arguments and returns a boolean.

13. Iterable: Represents an iterable object, like a list or a generator. You can specify the type of elements, e.g., Iterable[int] for an iterable of integers.

14. Generator: Represents a generator function that yields values lazily. You can specify the types of values it yields, e.g., Generator[int, None, None] for a generator that yields integers.

15. AnyStr: Represents either str or bytes, depending on the Python version.

16. Sequence: Represents a sequence type (e.g., list, tuple). You can specify the type of elements, e.g., Sequence[int] for a sequence of integers.

17. Mapping: Represents a mapping type (e.g., dictionary). You can specify the types of keys and values, e.g., Mapping[str, int] for a mapping with string keys and integer values.

18. Type: Represents a Python type, e.g., Type[int] for the integer type.

19. NewType: Creates a new type with a specific name and base type, allowing you to define custom types, e.g., UserId = NewType('UserId', int).

These are some of the commonly used type hints available in the typing module. You can use them >> >> to annotate function signatures, variable declarations, and class attributes to provide type information and improve code readability and maintainability.

# How to type hint a generator in Python 3
```
from typing import Generator

def generate() -> Generator[int, None, None]:
    for i in range(10):
        yield i

for i in generate():
    print(i)
```
