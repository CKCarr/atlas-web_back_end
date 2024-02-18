# Python - Variable Annotations

# Learning Objectives

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

# Annotations
Python 3 introduced function annotations as a way to attach metadata to the parameters of a function and its return value. These annotations can be used for type hints, which help with static type checking, improving readability, and assisting IDEs in providing more accurate code completion and error detection.

Type annotations allow developers to document the types of variables, function parameters, and return values. They do not change the behavior of your code but serve as hints for developers and tools that can analyze code.

## Basic Syntax
```python

x: int = 5
```
In this example, x is annotated to be of type int, and it's initialized with the value 5.

## Specifying Function Signatures and Variable Types
Function signatures can be annotated to specify the types of parameters and the return type. This makes the intended use of the function clearer and can catch type-related errors early.

### Function Signature Annotations
```python

def add(a: int, b: int) -> int:
    return a + b
```
This function specifies that both a and b should be integers, and it will return an integer.

## Variable Annotations
Beyond local and global variables, annotations can also be applied to class attributes.

``` python

class MyClass:
    attr: int
```
## Duck Typing
"Duck typing" is a concept in Python and dynamic languages where an object's suitability for use is determined by the presence of certain methods and properties, rather than the actual type of the object. The term comes from the phrase, "If it looks like a duck and quacks like a duck, then it probably is a duck."

Type annotations work with duck typing by allowing developers to specify "protocols" or interfaces that an object should adhere to, rather than specifying exact types.

```python

from typing import Protocol

class Quackable(Protocol):
    def quack(self) -> None:
        ...

def make_it_quack(duck: Quackable) -> None:
    duck.quack()
```
Here, any object passed to make_it_quack must have a quack method, regardless of its actual type.

### Syntax:
 The syntax for annotations involves adding a colon : after the parameter name in the function definition, followed by the annotation. The return value annotation is denoted by an arrow -> followed by the annotation, before the colon ending the function signature.

```python

def greet(name: str) -> str:
    """
    Greet a person with their name.
    
    Parameters:
    - name: the name of the person to greet
    
    Returns:
    A greeting string.
    """
    return f"Hello, {name}!"
```
### Type Hints:
 While annotations can be used for various purposes, type hints are the most common use case. They indicate the expected type of function arguments and return values.

``` python

from typing import List, Dict

def process_data(data: List[Dict[str, int]]) -> None:
    """
    Process a list of dictionaries.
    
    Parameters:
    - data: A list of dictionaries with string keys and integer values
    """
    for item in data:
        print(item)
```
## Validating Your Code with Mypy
Mypy is a popular static type checker for Python that uses type annotations. It can catch type errors before runtime, improving the reliability of your code.

### Basic Usage
Install Mypy: First, install Mypy using pip.
```bash

pip install mypy
```
Annotate Your Code: Write your Python code with type annotations.

Run Mypy: To check your code for type errors, run Mypy from the command line.

``` bash

mypy your_script.py
```
Mypy will analyze your code and report any type inconsistencies or violations based on the annotations.

### Best Practices
- Use comments sparingly and wisely: Comments should explain "why" something is done, not "what" is done. Good code mostly speaks for itself.

- Write meaningful docstrings: Especially for public API functions, classes, and modules. Follow conventions like the Google style or reSt
ructuredText (reST) style.

- Leverage type hints: They make your code easier to understand and maintain. Tools like mypy can use them to catch type errors before runtime.

- Keep documentation up to date: As your code changes, ensure your comments, docstrings, and annotations reflect those changes.

- Start Small: Gradually introduce type annotations in your codebase, especially in critical components.
- Use typing Module: Python's typing module provides a wide range of type hints, including List, Dict, Optional, and more, which are essential for accurately annotating your code.
- Combine With Duck Typing: Use protocols from the typing module to leverage duck typing with type annotations.
- Regularly Run Mypy: Integrate Mypy into your development workflow to catch type errors early.
