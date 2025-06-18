# Strings in python

## What is a string in python ?
*  A string is a sequence of characters used to represent text data.
* Strings are one of the fundamental data types in Python and are widely used for handling textual information.
* Strings are created by enclosing characters within single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Triple quotes allow for multi-line strings.

```py
single_quoted_string = 'Hello world single'
double_quoted_string = "Hello world double"
triple_quoted_string = '''Hello
world
triple
'''
```

## Immutability
* Python strings are immutable, meaning that once a string is created, its content cannot be changed.
* Any operation that appears to modify a string actually creates a new string with the desired changes.

```py
name = 'Johny'
print(name) #Output: Johny

name[0] = 'j' #Output: TypeError: 'str' object does not support item assignment 
```
* We have an error saying 'str' object does not support item assignment, meaning we cannot change a string after creation.

## Sequence of characters
* Strings are sequences, which means individual characters can be accessed using indexing
* Parts of the string can be extracted using slicing (e.g., my_string[1:4]).
```py
name = 'Johny'
print(name[0]) #Output: J

print(name[1]) #Output: o

print(name[-1]) #Output: y

print(name[0:2]) #Output: Jo

print(name[10]) #IndexError: string index out of range
```
* Here we are using index 10, trying to access 11th character of the string. The string has only 5 characters.
* If the index is more than 5, you will get IndexError as you can see above.

## Basic operations on strings
# 🧰 Basic String Operations in Python

| Operation           | Syntax / Example                      | Description                                             |
|---------------------|----------------------------------------|---------------------------------------------------------|
| Concatenation        | `"Hello" + " World"`                   | Combines two strings                                    |
| Repetition           | `"ha" * 3`                             | Repeats the string 3 times → `hahaha`                  |
| Length               | `len("Hello")`                         | Returns number of characters → `5`                     |
| Indexing             | `"Python"[0]`                          | Returns the first character → `'P'`                    |
| Slicing              | `"Python"[0:3]`                        | Returns a substring → `'Pyt'`                          |
| Membership           | `"a" in "apple"`                       | Checks if `"a"` is in the string → `True`              |
| Upper case           | `"hello".upper()`                      | Converts to uppercase → `'HELLO'`                      |
| Lower case           | `"HELLO".lower()`                      | Converts to lowercase → `'hello'`                      |
| Replace              | `"apple".replace("a", "o")`            | Replaces `'a'` with `'o'` → `'opple'`                  |
| Strip                | `" hello ".strip()`                    | Removes leading and trailing spaces → `'hello'`        |
| Split                | `"a,b,c".split(",")`                   | Splits string into list → `['a', 'b', 'c']`            |
| Join                 | `".".join(['a', 'b', 'c'])`            | Joins list into string → `'a.b.c'`                     |
| Find                 | `"banana".find("a")`                   | Finds first index of `'a'` → `1`                       |
| Count                | `"banana".count("a")`                  | Counts how many times `'a'` appears → `3`              |
| Startswith           | `"apple".startswith("a")`             | Checks if string starts with `'a'` → `True`            |
| Endswith             | `"apple".endswith("e")`               | Checks if string ends with `'e'` → `True`              |

