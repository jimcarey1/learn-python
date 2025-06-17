# Output Even numbers in the list(only if they are in even indices.)

## Problem Statement
I am giving you an input list called **numbers**, You should write a program that prints the element in the list only If they
accept below conditions.
* It should be an even number.
* It should be in even indices.

## Solution(Algorithm):
* You have a list called **numbers**.
* Use for loop with the range to iterate over numbers list.
* Check if the index is an even number(i is even ?)
* Check if the element at that particular index is even number(basically nested if condition).
* If the two conditions return true, print that particular number.

```py
numbers = [21, 34, 56, 87, 99]
length_of_numbers = len(numbers)
for i in range(length_of_numbers):
    #implement your logic here, (Understand the algorithm carefully)
    print(numbers[i])
```