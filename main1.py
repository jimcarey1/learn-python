#Check if a string is palindrome or not.
x = 'racecar'
for i in range(len(x)): #[0,1, 2, 3, 4, 5, 6]
    print(i, len(x)-1-i)
    if x[i] != x[len(x)-1-i]: #i->0, len(x)-1-i -> 6
        print('Not a palindrome.')
        exit()
print('Palindrome')