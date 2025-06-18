
# 📚 Tuples in Python - Grade 7 Notes

## 🧠 What is a Tuple?

A **tuple** is a collection of items that are:
- **Ordered** (items have a specific position)
- **Immutable** (cannot be changed after creation)
- Can store **different types of data** (like numbers, text, etc.)

It is similar to a **list**, but you **cannot change, add, or remove** items from a tuple.

---

## 🏷️ How to Create a Tuple

### ✅ Syntax:

```python
my_tuple = (1, 2, 3)
```

- Tuples use **round brackets `()`**
- Items are separated by **commas**

### 🧪 Examples:

```python
# A tuple of numbers
numbers = (10, 20, 30)

# A tuple of strings
fruits = ("apple", "banana", "cherry")

# A mixed tuple
mixed = ("John", 25, True)
```

---

## 🪧 Real-Life Use Cases of Tuples

### 📌 Use Case 1: GPS Coordinates
```python
location = (17.3850, 78.4867)  # (latitude, longitude)
```

We use a tuple here because the coordinates shouldn’t change accidentally.

---

### 📌 Use Case 2: Days of the Week
```python
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
```
Days don’t change, so a tuple is better than a list.

---

### 📌 Use Case 3: RGB Color Values
```python
color = (255, 0, 128)  # (Red, Green, Blue)
```
We use tuples to pass colors in games or design tools.

---

## 🧪 Code Examples & Explanations

### 🔍 Accessing Tuple Items

```python
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
```

- Tuples use **indexing** like lists.
- Indexing starts from **0**

---

### 🚫 Trying to Change a Tuple

```python
colors = ("red", "green", "blue")
colors[0] = "yellow"  # ❌ Error!
```

- This gives an **error** because **tuples are immutable**.

---

### 🔄 Looping Through a Tuple

```python
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)
```

✅ Output:
```
apple
banana
cherry
```

---

### 📏 Length of a Tuple

```python
animals = ("cat", "dog", "cow")
print(len(animals))  # Output: 3
```

---

### 🔎 Check if Item Exists

```python
colors = ("red", "green", "blue")

if "green" in colors:
    print("Green is in the list!")
```

---

## 🧠 Quick Facts

| Feature         | Tuple           | List             |
|-----------------|------------------|------------------|
| Mutable         | ❌ No            | ✅ Yes            |
| Uses Brackets   | `()`             | `[]`             |
| Faster          | ✅ Yes           | ❌ No             |
| Can change?     | ❌ No            | ✅ Yes            |

---

## ✅ Practice Time

1. Create a tuple called `favourite_books` with 3 book names.
2. Print the second book using index.
3. Try to change one book name — what happens?
4. Loop through the tuple and print each book.

---

## 🎯 Summary

- Tuples are **unchangeable** groups of items.
- Use `()` to create them.
- Great for **fixed data** like coordinates, days, or colors.
- You can **read** from tuples, but can’t **edit** them.

---
