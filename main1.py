def fibonacci(n:int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    i, j = 0, 1
    for i in range(n-2):
        i, j = j, i + j
    return j

print(fibonacci(50))