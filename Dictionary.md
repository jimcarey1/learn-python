# 📘 Dictionaries in Python

## What is a Dictionary?

A **dictionary** in Python is an **unordered**, **mutable** collection of key-value pairs.

- Each value is accessed by a **key**, not by an index.
- Think of it like a real-life dictionary where a **word** (key) maps to a **definition** (value).

```py
# Example:
student = {
    "name": "Jhony",
    "age": 13,
    "grade": "7"
}
```

---

## Key Points

- Dictionaries are defined using **curly braces `{}`**.
- Keys must be **unique** and **immutable** (e.g., strings, numbers, tuples).
- Values can be of any data type.

---

## Common Dictionary Operations

### 1. Accessing values
```py
print(student["name"])  # Output: Alice
```

### 2. Adding a new key-value pair
```py
student["school"] = "Greenwood High"
```

### 3. Updating a value
```py
student["age"] = 14
```

### 4. Removing a key
```py
del student["grade"]
```

### 5. Getting all keys and values
```py
print(student.keys())    # Output: dict_keys(['name', 'age', 'school'])
print(student.values())  # Output: dict_values(['Alice', 14, 'Greenwood High'])
print(student.items())   # Output: dict_items([('name', 'Alice'), ('age', 14), ('school', 'Greenwood High')])
```

### 6. Checking if a key exists
```py
if "name" in student:
    print("Yes, 'name' exists.")
```

### 7. Looping through a dictionary
```py
for key, value in student.items():
    print(key, ":", value)
```

---

## List vs Dictionary in Python

| Feature                  | List                             | Dictionary                        |
|--------------------------|----------------------------------|-----------------------------------|
| **Definition**           | Ordered collection of items      | Unordered collection of key-value pairs |
| **Access by**            | Index (e.g., `my_list[0]`)        | Key (e.g., `my_dict["key"]`)      |
| **Syntax**               | `[]` (square brackets)           | `{}` (curly braces)               |
| **Keys or Indices**      | Automatically assigned (0,1,2...)| User-defined keys                 |
| **Mutable**              | Yes                              | Yes                               |
| **Best Used For**        | Storing ordered items            | Storing related data using keys   |
| **Example**              | `["apple", "banana", "grape"]`   | `{"fruit": "apple", "color": "red"}` |

---

## Summary

- Use **lists** when order matters and you only care about the values.
- Use **dictionaries** when you want to **label** your data with custom **keys** for easier and more meaningful access.