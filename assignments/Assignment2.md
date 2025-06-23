# Assignment 2

## Problem1
### 1. Write a program to check if a string is palindrome or not.
* You have an input string x='racecar'.
* A palindrome is a word that spells the same from the reverse order, so you reverse the word and if the reversed word is equal to the input string x, then it is a palindrome.
* First, we need to check the first character and last character(in our case 1st char is **r** and last char is **r**).
    * If first and last character are equal, then we have to check the 2nd char and 2nd char from the right side.(**a**) recursively we have to do this if the two characters are equal for every character in the string.
    * If they are not equal, then we know that the string is not a palindrome(exit from the program at this point).
* If you cannot prove it is not a palindrome, consider it as a palindrome.

```py
#Note: There are some syntax errors in the program.(Observe carefully.)
x = 'racecar'
length_of_x = len(x)
for i in range(length_of_x)
    if condition: #You have to figure out the logic to check two characters in left and right.
        print('It is not a palindrome.')
        #Exit from the program.
print('It is a palindrome.')
```