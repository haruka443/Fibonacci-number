amountOfNumbers = int(input('How many numbers of Fibonacci number do you want to list? '))
previousNumber = 1
currentNumber = 1
i = 0
FibonacciNumbers = [i, previousNumber, currentNumber]
if amountOfNumbers > 3:
    while i < amountOfNumbers - 3:
        nextNumber = currentNumber + previousNumber
        previousNumber = currentNumber
        currentNumber = nextNumber
        i += 1
        FibonacciNumbers.append(nextNumber)
elif amountOfNumbers == 3:
    pass
elif amountOfNumbers == 2:
    FibonacciNumbers.remove(FibonacciNumbers[-1])
elif amountOfNumbers == 1:
    del(FibonacciNumbers[1:3])
print(FibonacciNumbers)


# amountOfNumbers = float(input('How many numbers of Fibonacci number do you want to list? '))
# lst = [0, 1, 1]
# while len(lst) < amountOfNumbers:
#    newNumber = lst[len(lst) - 1] + lst[len(lst) - 2]
#    newNumber = lst[-1] + lst[-2]
#    lst.append(newNumber)
# i = 1
# for number in lst:
#    print("%d, %d." % (i, number), end = ' ')
#    i += 1
