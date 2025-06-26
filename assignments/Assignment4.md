# Find Direction.

## Problem Statement
* A man is initially in the North(N) direction.
* You will be provided with an input string such as **'LLRLRR'**.
* L means, the person took a left turn.
* R means, the person took a right turn.
* You have to go through the every character in the string and find the final direction that main is in.

* You can use **N** for North, **S** for South, **E** for East, **W** for West.
* If a person is in N direction and if he takes left turn(**L**), the direction of the person is now West(**W**).
* Similarly, If a person is in N direction and if he takes right turn(**R**), the direction of the person is now West(**E**).


## Solution (Algorithm)
* You have an input string such as **LLRLRR** and the initial direction of the person is **N**.
* Use a for loop to iterate through the input string.
* for every iteration, based on the person's current direction and his current turn, update his direction.
* At the end, print in which direction does the person is travelling.

```py
path = 'LLRLRR'
direction = 'N'
for char in path:
    #write your logic(might be multiple if statements with multiple conditions in them.)
print(direction)
```