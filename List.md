
# Lists in Python

## What is a List?

A **list** is a collection of items that are:
- **Ordered** (items have a specific position)
- **Mutable** (you can change, add, or remove items)
- Can store **different types of data** (numbers, text, etc.)

Lists are one of the most important and flexible data structures in Python.

---

## How to Create a List

### Syntax:

```python
my_list = [1, 2, 3]
```

- Lists use **square brackets `[]`**
- Items are separated by **commas**

### Examples:

```python
# A list of numbers
numbers = [10, 20, 30]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A mixed list
mixed = ["John", 25, True]
```

---

## Real-Life Use Cases of Lists

### Use Case 1: Shopping List
```python
shopping = ["milk", "eggs", "bread"]
```

You can add or remove items easily.

---

### Use Case 2: Student Marks
```python
marks = [89, 76, 92, 85]
```

We can calculate average, highest and lowest marks.

---

### Use Case 3: Tasks in a To-Do List
```python
tasks = ["homework", "clean room", "practice coding"]
```

Tasks can be checked off, added or removed.

---

## Code Examples & Explanations

### Accessing List Items

```python
colors = ["red", "green", "blue"]
print(colors[1])  # Output: green
```

- Indexing starts from **0**

---

### Changing List Items

```python
colors = ["red", "green", "blue"]
colors[0] = "yellow"
print(colors)  # Output: ['yellow', 'green', 'blue']
```

---

### Adding Items

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

---

### Removing Items

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
```

---

### Looping Through a List

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

---

### Length of a List

```python
animals = ["cat", "dog", "cow"]
print(len(animals))  # Output: 3
```

---

### Check if Item Exists

```python
colors = ["red", "green", "blue"]

if "green" in colors:
    print("Green is in the list!")
```

---

## Practice Time

1. Create a list called `favourite_games` with 3 game names.
2. Print the last game using index.
3. Add a new game using `append()`.
4. Remove one game using `remove()`.
5. Print the total number of games.

---

## Summary

- Lists are **changeable** and **ordered** groups of items.
- Use `[]` to create them.
- You can add, remove, and change items.
- Lists are perfect for tasks, items, scores, and more.

---

# List vs Tuple: Supported Operations in Python

| Operation                        | List (`[]`) | Tuple (`()`) | Description                                                                 |
|----------------------------------|-------------|--------------|-----------------------------------------------------------------------------|
| Create                           | ✅          | ✅           | Both can be created with literals.                                          |
| Indexing (`obj[index]`)          | ✅          | ✅           | Access elements using index.                                                |
| Slicing (`obj[start:end]`)       | ✅          | ✅           | Extract a sub-part using slicing.                                           |
| Iteration (`for x in obj`)       | ✅          | ✅           | Loop through elements.                                                      |
| `len()`                          | ✅          | ✅           | Get number of elements.                                                     |
| `in` / `not in`                  | ✅          | ✅           | Check if item exists.                                                       |
| Concatenation (`+`)              | ✅          | ✅           | Join two lists or tuples.                                                   |
| Repetition (`*`)                 | ✅          | ✅           | Repeat items.                                                               |
| Immutability                     | ❌          | ✅           | Tuples are immutable; lists are not.                                        |
| Item assignment (`obj[i] = x`)   | ✅          | ❌           | Only lists support changing values.                                         |
| `append(x)`                      | ✅          | ❌           | Only lists can add new items.                                               |
| `extend(iterable)`               | ✅          | ❌           | Extend list with items from another iterable.                               |
| `insert(index, value)`           | ✅          | ❌           | Insert item at a specific position.                                         |
| `remove(value)`                  | ✅          | ❌           | Remove first matching value.                                                |
| `pop(index)`                     | ✅          | ❌           | Remove and return item at index.                                            |
| `clear()`                        | ✅          | ❌           | Remove all items.                                                           |
| `reverse()`                      | ✅          | ❌           | Reverse the list in place.                                                  |
| `sort()`                         | ✅          | ❌           | Sort the list in place.                                                     |
| `count(value)`                   | ✅          | ✅           | Count number of occurrences.                                                |
| `index(value)`                   | ✅          | ✅           | Return index of first occurrence.                                           |
| Can be used as dict key          | ❌          | ✅           | Tuples can be used as dictionary keys (only if all elements are hashable).  |
| Supports hashable property       | ❌          | ✅           | Tuples are hashable (if contents are hashable), lists are not.             |
| Memory usage                     | 🟥 Higher   | 🟩 Lower     | Tuples consume less memory than lists.                                      |
| Speed for iteration              | 🟥 Slower   | 🟩 Faster    | Tuples are faster to iterate due to immutability.                           |
| Nesting                          | ✅          | ✅           | You can nest both lists and tuples.                                         |
| Copy (`copy()` or slicing)       | ✅          | ✅           | Both support shallow copying (tuples via slicing only).                     |
| Used in function arguments       | ✅          | ✅           | Both are used, but tuples often represent fixed-size records.               |

