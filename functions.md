# Functions in python

## What is a Function?
A **function** is a reusable block of code that performs a specific task. Functions help us organize code, avoid repetition, and make programs easier to understand.

---

## Defining a Function
Use the `def` keyword followed by the function name and parentheses:
```python
def greet():
    print("Hello, world!")
```
- **`def`**: keyword to define a function  
- **`greet`**: function name  
- **`()`**: parentheses for parameters (empty if none)  
- **`:`** indicates the start of the function body  

---

## Calling a Function
To run the code inside a function, **call** it by its name with parentheses:
```python
greet()
# Output: Hello, world!
```

---

## Parameters and Arguments
Functions can accept inputs called **parameters**:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output: Hello, Alice!
```
- **Parameter**: the variable listed in the function definition (`name`)  
- **Argument**: the actual value passed (`"Alice"`)

You can have multiple parameters:
```python
def add(a, b):
    return a + b

print(add(3, 5))
# Output: 8
```

---

## Return Values
Use `return` to send back a value from a function:
```python
def square(x):
    return x * x

result = square(4)
print(result)
# Output: 16
```
- After `return`, the function stops running.

---

## Docstrings
A **docstring** is a short description of what the function does, placed right after the `def` line:
```python
def multiply(a, b):
    """Return the product of a and b."""
    return a * b
```
View a function's docstring:
```python
print(multiply.__doc__)
# Output: Return the product of a and b.
```

---

## Function Scope
- **Local variables**: defined inside a function, only exist there.
- **Global variables**: defined outside functions, accessible inside if not overridden.
```python
x = 10  # global

def show_x():
    x = 5  # local
    print(x)  # prints 5

show_x()
print(x)      # prints 10
```

---

## Built-in Functions
Python provides many helpful functions:
- `print()`
- `len()`
- `max()`, `min()`
- `sum()`
- `type()`

Try them in your programs!

---

## Good Practices
- Use meaningful function names (e.g., `calculate_average`).
- Keep functions small and focused.
- Add docstrings for clarity.
- Avoid side effects (unexpected changes outside the function).

---

## Examples to Try
1. Write a function `is_even(n)` that returns `True` if `n` is even.  
2. Create `fahrenheit_to_celsius(f)` to convert temperatures.  
3. Define `factorial(n)` to compute the factorial of `n`.

Happy coding!
