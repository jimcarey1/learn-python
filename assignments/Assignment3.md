# Assignment3

## Problem Statement
**Write a program to reverse a number**
* You have an input number say **x = 123**
* You have to write a python program to reverse the number i.e., the output should be 321.
* Create a new variable called **result** to store the output of the program and set it's initial value to zero.
* Use a while loop that runs as long as n is not zero.
* Get the last digit of the number(divide it by 10.) --> n%10
* Multiply the **result**(variable you created to store the output.) by 10 (to shift digits left), then add the last digit.
* remove the last digit from the number. **(you have to use (n//10) integer division to remove the last digit.)** --> n = n//10
* print the result variable.(print it outside the **while loop**).

```py
x = 123
#create the result variable.
while condition: #condition for while loop
    #write your logic
print(result) #It should print 321.
```