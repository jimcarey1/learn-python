# Week 3: Algorithmic Approaches

Below are the algorithmic steps for each problem in one consolidated file.

---

## Problem 1: Check Palindrome
**Approach (Algorithmic Steps):**
1. Initialize two pointers: `left = 0` and `right = len(x) - 1`.
2. While `left < right`:
   - Compare `x[left]` and `x[right]`.
   - If they are not equal, conclude the string is *not* a palindrome and stop.
   - Otherwise, increment `left` by 1 and decrement `right` by 1.
3. If the loop completes without mismatches, conclude the string *is* a palindrome.

---

## Problem 2: Fibonacci Sequence
**Approach (Algorithmic Steps):**
1. If `n <= 2`, the Fibonacci number is 1.
2. Initialize two variables: `a = 1`, `b = 1`.
3. For each `i` from 3 to `n` (inclusive):
   - Compute `next = a + b`.
   - Update `a = b` and `b = next`.
4. After the loop, `b` holds the `n`th Fibonacci number.
5. (To get the whole sequence, collect each `b` as you iterate.)

---

## Problem 3: Count Vowels in a String
**Approach (Algorithmic Steps):**
1. Define a set of vowels: `vowels = {'a','e','i','o','u'}`.
2. Initialize `count = 0`.
3. For each character `ch` in the string:
   - Convert `ch` to lowercase.
   - If `ch` is in `vowels`, increment `count`.
4. After the loop, `count` is the total number of vowels.

---

## Problem 4: Reverse a Word
**Approach (Algorithmic Steps):**
1. Initialize an empty string `rev = ""`.
2. For index `i` from `len(w)-1` down to `0`:
   - Append `w[i]` to `rev`.
3. After the loop, `rev` is the reversed word.

---

## Problem 5: Find the Largest Number in a List
**Approach (Algorithmic Steps):**
1. Assume the first element is largest: `max_val = nums[0]`.
2. For each element `x` in `nums`:
   - If `x > max_val`, update `max_val = x`.
3. After the loop, `max_val` is the largest number.

---

## Problem 6: Sum of Numbers from 1 to N
**Approach (Algorithmic Steps):**
1. Initialize `total = 0`.
2. For `i` from `1` to `N` (inclusive):
   - Add `i` to `total`.
3. After the loop, `total` is the sum `1 + 2 + ... + N`.

---

## Problem 7: Swap Two Numbers Using a Third Variable
**Approach (Algorithmic Steps):**
1. Store the value of `a` in `temp`.
2. Assign `b` to `a`.
3. Assign `temp` to `b`.
4. Now `a` and `b` have swapped values.

---

## Problem 8: Convert Celsius to Fahrenheit
**Approach (Algorithmic Steps):**
1. Read the Celsius value into `c`.
2. Compute `f = c * 9/5 + 32`.
3. `f` is the temperature in Fahrenheit.

---

## Problem 9: Calculate the Factorial of a Number
**Approach (Algorithmic Steps):**
1. Initialize `fact = 1`.
2. For `i` from `1` to `n` (inclusive):
   - Update `fact = fact * i`.
3. After the loop, `fact` is `n!`.

---

## Problem 10: Count Down from 100 to 0
**Approach (Algorithmic Steps):**
1. For `i` from `100` down to `0` (step -1):
   - Print `i`.
2. Stop when `i` reaches `0`.

---

## Problem 11: Find the Average of a List of Numbers
**Approach (Algorithmic Steps):**
1. Initialize `total = 0`.
2. For each number `x` in `nums`:
   - Add `x` to `total`.
3. Compute `average = total / len(nums)`.
4. `average` is the result.

---

## Problem 12: Count Letters in a Sequence
**Approach (Algorithmic Steps):**
1. Initialize an empty dictionary `counts = {}`.
2. For each character `ch` in the string:
   - If `ch` is in `counts`, increment `counts[ch]` by 1.
   - Otherwise, set `counts[ch] = 1`.
3. After the loop, `counts` maps each letter to its frequency.

---

## Problem 13: Isogram Checker
**Approach (Algorithmic Steps):**
1. Initialize an empty set `seen = set()`.
2. For each character `ch` in the word:
   - If `ch` is in `seen`, conclude it's *not* an isogram and stop.
   - Otherwise, add `ch` to `seen`.
3. If the loop completes without repeats, conclude it *is* an isogram.

---

## Problem 14: Common Elements in Two Lists
**Approach (Algorithmic Steps):**
1. Convert the first list to a set: `set1 = set(list1)`.
2. Initialize empty list `common = []`.
3. For each element `x` in `list2`:
   - If `x` in `set1` and not already in `common`, append `x` to `common`.
4. `common` contains all shared elements.
