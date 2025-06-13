# **Introduction to Python**

## Table of contents
1. Variables
2. Data types(int, float, bool, str)
    * Type checking
    * Type casting(changing str to int)
    * Some basic examples.
3. Conditional Statements(Decision making)
4. Range function(In detail)
5. Loops(Repititive Tasks)
6. Sequences (ordered collections of items)
    * Different types of sequences(List, Str, Tuple, Range)
    * Mutable vs Immutable sequences
    * Different operations on them.(Indexing, Concatenation, Length, Iteration)
    * List vs Tuples

## 1. Variables
**What is a variable ?**
variables are used to store data that can be <mark>referenced and manipulated during program execution.</mark> A variable is essentially a name that is assigned to a value.
```py
a = 5 #We created a variable called a and assigned it the value 5.
a = 6 #We can manipulate the value of a anytime, anywhere in our program.

name = 'johny' #we gave a textual value to our variable this time.
name = 56      #not only can we change the value but also datatype.
```

**print function in detail**
```py
for i in range(5):
    print(i)   #Output: prints 0 to 4 in newline.

for i in range(5):
    print(i, end=' ') #Output: print 0 to 4 in sameline.

for i in range(5):
    print(i, i+1, sep='-', end=' ') #Output: You observe the output.
```


## 2. Data types
**What are data types in python ?**
Python Data types are the <mark>classification or categorization of data items.</mark> It represents the kind of value that tells what operations can be performed on a particular data.

*In python, there is a built-in function called **type**, which it returns the data type of the variable.*
```py
x = 10
print(type(x))   #int

x = 10.0
print(type(x))   #float

name = 'johny'
print(type(name)) #str

is_correct = False
print(type(is_correct)) #bool
```

**Type casting**
Type casting, also known as type conversion, <mark>is the process of changing the data type of a variable to another data type.</mark>

```py
x = 10
float_x = float(x) 
print(float_x)  #output: 10.0

str_x = str(x)
print(str_x)

y = 12.5
int_y = int(y)
print(int_y)    #output: 12.0

text = '10.55'
float_text = float(text)
print(float_text)       #output: 10.55

int_text = int(text)
print(int_text)         #ValueError: invalid literal for int() with base 10: '10.55'
```

## 3. Conditional Statements
**What are conditional statements ?**
Conditional statements in Python are used to <mark>control the flow of a program</mark> based on whether a <mark>condition is true or false</mark>.
*<mark>These statements allow you to execute different blocks of code depending on the outcome of a condition.</mark>*

**simple if statement**
```py
n = 9
if(n > 0):
    print('Positive number')
```

**if else statement**
```py
n = -2
if(n > 0):
    print('Positive number')
else:
    print('Negative number')
```

**if elif else statement**
```py
n = 0
if(n > 0):
    print('positive number')
elif (n < 0):
    print('negative number')
else:
    print('zero')
```

**Nested if statement**
```py
n = -4
if(n%2 == 0):
    if(n > 0):
        print('Positive even number')
    else:
        print('Negative even number')
```

## 4. Range Function

**What is range function() ?**
* The range() function in Python is a built-in function that generates a sequence of numbers.
* It is commonly used with for loops to iterate a specific number of times or to access elements in a sequence using their indices.
* The range() function can take one, two, or three arguments.

**range() with one argument**
* range(stop): Generates a sequence of numbers starting from 0 up to (but not including) the stop value, with a default step of 1.

```py
numbers = list(range(100))
print(numbers)   #Output: [0, 1, 2, 3..., 98, 99]
```

**range() with two arguments**
range(start, stop): Generates a sequence of numbers starting from start up to (but not including) the stop value, with a default step of 1.

```py
numbers = list(range(50, 100))
print(numbers)  #Output: [50, 51, 52, ..., 98, 99]
```

**range() with three arguments**
range(start, stop, step): Generates a sequence of numbers starting from start up to (but not including) the stop value, with a step of step.

```py
numbers = list(range(0, 100, 2))
print(numbers)  #Output: [0, 2, 4, 6, 8, ..., 96, 98]
```

**range() with negative step**
```py
numbers = list(range(100, 0, -2))
print(numbers)  #Output: [100, 98, 96, ...., 8, 6, 4, 2]

numbers = list(range(0, 100, -2))
print(numbers)  #Ouput: [] (range will not produce any numbers in this case.)
```


## 5. Loops

**what are loops in python ?**
* In Python, loops are control flow structures that allow you to repeatedly execute a block of code.
* They are essential for automating repetitive tasks and iterating over collections of data.
* Python primarily offers two types of loops: for loops and while loops.

### **For loop**
* **Iteration over sequences:** for loops are primarily used to iterate over a sequence of items, such as lists, tuples, strings, or ranges.
```py
fruits = ['apple', 'banana', 'mango', 'grape']
for fruit in fruits:
    print(fruit)
```
* **Range Function:** The range() function is often used with for loops to iterate a specific number of times.
```py
for i in range(10):
    print(i)
```

### **While Loop**
* **Condition-based execution**: while loops continue to execute a block of code as long as a specified condition is true.
```py
count = 0
while count < 5:
    print(count)
    count = count + 1 #This code will print numbers from 0 to 4.
```

### **Continue in loops**
* The continue statement in Python returns the control to the beginning of the loop.
```py
for letter in 'india':
    if letter == 'i':  #It checks if the letter is i and goes to the next iteration of the loop(if the condition is true.)
        continue
    print(letter, end='')
```

### **Break in loops**
* The break statement in Python brings control out of the loop.
```py
for letter in 'india':
    if letter == 'i':
        break
    print(letter, end='')
```

## 5. Sequences

**What are sequences in python ?**
* An ordered collection of things.
* Sequences' primary characteristic is their indexed elements, which allow you to recover any item by using a number that indicates where it is in the sequence. 
* Lists, tuples, strings, and ranges are among the sequence types available in Python.
* The most common examples of sequences are List, Tuple, String.

```py
fruits = ['apple', 'mango', 'grapes']
print(type(fruits))

fruits = ('apple', 'mango', 'grape')
print(type(fruits))

fruit = 'apple'
print(type(fruit)) 
```

**Accessing sequences using indexing**
*  Indexing refers to accessing elements within a sequence (like strings, lists, or tuples) using their position or index.
*  It's a fundamental concept for manipulating and extracting data from these structures.
*  Python uses zero-based indexing, meaning the first element in a sequence has an index of 0, the second has an index of 1, and so on.
*  You can also use negative indices to access elements from the end of the sequence.

```py
fruits = ['apple', 'banana', 'carrot', 'guava']

print(fruits[0])  #Output: apple
print(fruits[1])  #Output: banana

print(fruits[-1]) #Output: guava
```

**Modifying sequences**
* Modifying refers to changing the value of the sequences.

```py
#Changing the elements inside the list.
fruits = ['apple', 'banana', 'carrot', 'guava']
print(fruits) #Output: ['apple', 'banana', 'carrot', 'guava']

fruits[0] = 'mango'
print(fruits) #Output: ['mango', 'banana', 'carrot', 'guava']

#Changing the elements inside the tuple.
fruits = ('apple', 'banana', 'carrot', 'guava')
print(fruits)  #Output: ('apple', 'banana', 'carrot', 'guava')

fruits[0] = 'mango'
print(fruits)  #Output: TypeError: 'tuple' object does not support item assignment
```
* As you can see from this example, we can modify lists but tuples cannot be modified.

**Mutable vs Immutable sequences**
* Mutable sequences are data structures that can be modified after they are created.(List)
* This means you can add, remove, or change elements within the sequence without creating a new object.
* Immutable sequences (e.g., tuples, strings) cannot be changed after creation.

```py
fruit = 'apple'
print(fruit)  #Output: fruit

print(fruit[0]) #Output: a

fruit[0] = 'A'
print(fruit)  #Output: TypeError: 'str' object does not support item assignment
```

**Some Common List Operations**

***Length of the sequence***
```py
fruits = ['apple', 'banana', 'carrot', 'guava']
print(len(fruits)) #Output: 4
print(len(fruits[-1]))  #Output: 5

fruits = ('apple', 'banana', 'carrot', 'guava')
print(len(fruits)) #Output: 4

fruit = 'apple'
print(len(fruit))  #Output: 5
```

***Inserting element at the end of the list***
```py
fruits = ['apple', 'banana', 'carrot', 'guava']
print(fruits) #Output: ['apple', 'banana', 'carrot', 'guava']

fruits.append('mango')
print(fruits) #Output: ['apple', 'banana', 'carrot', guava', 'mango']
```

***Removing Last element from the list***
```py
fruits = ['apple', 'banana', 'carrot', 'guava']
print(fruits) #Output: ['apple', 'banana', 'carrot', 'guava']

fruits.pop()
print(fruits) #Output: ['apple', 'banana', 'carrot']
```

***Removing a value from the list***
```py
fruits = ['apple', 'banana', 'carrot', 'guava']
print(fruits) #Output: ['apple', 'banana', 'carrot', 'guava']

fruits.remove('apple')
print(fruits) #Output: ['banana', 'carrot', 'guava']
```

***Inserting an element at a certain position***
```py
fruits = ['apple', 'banana', 'carrot']
print(fruits) #Output: ['apple', 'banana', 'carrot']

fruits.insert(1, 'guava')
print(fruits) #Output: ['apple', 'guava', 'banana', 'carrot']
```

***Deleting every element in a list***
```py
fruits = ['apple', 'banana', 'carrot']
print(fruits) #Output: ['apple', 'banana', 'carrot']

fruits.clear()
print(fruits)  #Output: []
```

**Using for loop on a list**
```py
fruits = ['apple', 'banana', 'carrot']

for fruit in fruits:
    print(fruit)
```

### List vs Tuple
| Feature                     | Tuple                          | List                          |
|----------------------------|--------------------------------|-------------------------------|
| **Mutability**             | Immutable                      | Mutable                       |
| **Syntax**                 | `(1, 2, 3)`                    | `[1, 2, 3]`                   |
| **Performance**            | Faster than lists              | Slightly slower               |
| **Use Case**               | Fixed data                     | Dynamic data                  |
| **Memory Consumption**     | Less memory                    | More memory                   |
| **Methods Available**      | Few (e.g., `count()`, `index()`) | Many (e.g., `append()`, `extend()`, `pop()`) |
| **Hashable (can be key)**  | Yes (if all elements are hashable) | No                            |
| **Can be Nested**          | Yes                            | Yes                           |
| **Supports Iteration**     | Yes                            | Yes                           |
| **Used in**                | Dictionary keys, fixed data structures | General-purpose collections  |


## Operations supported by list and tuple
| Operation                          | Tuple | List |
|-----------------------------------|:-----:|:----:|
| Indexing (`obj[i]`)               |  ✅   | ✅   |
| Slicing (`obj[start:stop]`)       |  ✅   | ✅   |
| Iteration (`for x in obj`)        |  ✅   | ✅   |
| Length (`len(obj)`)               |  ✅   | ✅   |
| Membership Test (`x in obj`)      |  ✅   | ✅   |
| Concatenation (`obj1 + obj2`)     |  ✅   | ✅   |
| Repetition (`obj * n`)            |  ✅   | ✅   |
| Min/Max (`min(obj)`, `max(obj)`)  |  ✅   | ✅   |
| Count (`obj.count(x)`)            |  ✅   | ✅   |
| Index (`obj.index(x)`)            |  ✅   | ✅   |
| Append (`obj.append(x)`)          |  ❌   | ✅   |
| Extend (`obj.extend([...])`)      |  ❌   | ✅   |
| Insert (`obj.insert(i, x)`)       |  ❌   | ✅   |
| Remove (`obj.remove(x)`)          |  ❌   | ✅   |
| Pop (`obj.pop()`)                 |  ❌   | ✅   |
| Clear (`obj.clear()`)             |  ❌   | ✅   |
| Sort (`obj.sort()`)               |  ❌   | ✅   |
| Reverse (`obj.reverse()`)         |  ❌   | ✅   |
| Immutability                      |  ✅   | ❌   |
