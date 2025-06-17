number = 9
#We know that, 1 and itself are the factors of any number.
#If we can find out one more factor, we can conclude that it is a composite number.
for i in range(2, number): #[2...8]
    print(i, number)
    if number%i == 0:  #If this condition returns true, we run code inside it.
        print('Composite number')
        exit()
print('Prime Number')