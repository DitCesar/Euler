'''
Project Fibonacci
Problem 1

*--> fibonacciSumLimit:

Will add up the values in the sequence 
until the total is the maximum before 
the limit is reached.

In other words, the sum of the values
will not exceed the limit

*--> fibonacciSumEvenNumbers: 

Will add up the values found in the
sequence if they are even-numbers and
lower than the established limit.

'''

def fibonacciSumLimit (limit):
    frstNum = 0
    scndNum = 1
    finlNum = 0
    sum = 0

    while sum < limit:
        finlNum = frstNum + scndNum
        sum = sum + finlNum

        if sum > limit:
            sum = sum - finlNum
            break

        frstNum = scndNum
        scndNum = finlNum

    print ("Bigger sum possible before reach limit: ", sum)

def fibonacciSumEvenNumbers (limit):
    frstNum = 0
    scndNum = 1
    finlNum = 0
    sum = 0

    while finlNum < limit:
        finlNum = frstNum + scndNum

        if finlNum > limit:
            finlNum = finlNum - frstNum
            break
        
        if finlNum % 2 == 0:
            sum = sum + finlNum
        
        frstNum = scndNum
        scndNum = finlNum

    print ("Sum of the even-values before the limit: ", sum)

if __name__ == "__main__":
    fibonacciSumLimit(4000000)
    fibonacciSumEvenNumbers(4000000)