for i in range(5):
    print(i)   #Output: prints 0 to 4 in newline.

for i in range(5):
    print(i, end=' ') #Output: print 0 to 4 in sameline.
print()

for i in range(5):
    print(i, i+1,  sep='-', end=' ') #Output: You observe it