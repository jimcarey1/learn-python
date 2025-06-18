# Common Python mistakes I observed

## Print statement
* You should know how and why inverted commas are used.
* You should study errors and try to understand them.

```py
print('My name is john') #Output: My name is john.

print('My name is john) #Output: SyntaxError: unterminated string literal (detected at line 1)
#When you get this error, python basically saying, you forgot to open or close a string literal.
#The starting inverted comma is the starting point and the last inverted comma is the ending point of the string.

print('x') #Output: x

print(x)  #Output: NameError: name 'x' is not defined
#Whenever you see a NameError, it means you are trying to access a variable that is not defined.
#I am trying to print the value of x, but I have not declared the variable x.
```

## Syntax error in block of codes(Control structures, Functions, Classes)
* whenever you want to write a block of code, you should end it with :
* You will get a syntax error if you omit it.

```py
if 4%2 == 0:
    print('The program is working.') #Output: The program is working

if 4%2 == 0
    print('The program is not working.') #Output: SyntaxError: expected ':'
#The : symbol is missing and you are getting syntax error.

for i in range(10)
    print(i, end=' ') #Output: SyntaxError: expected ':'
#The : symbol is missing and you are getting syntax error.
```

## Case-sensitive nature of python
* Python is case sensitive meaning it treats uppercase and lowercase letters as different.
* Age and age are two different entities in python.
* Once you created a variable you should exactly use the same spelling.

```py
age = 12
print(age) #Output: 12

print(Age) #Output: NameError: name 'Age' is not defined.
#got a NameError, saying Age is not defined. python treats age and Age as two different things.
```