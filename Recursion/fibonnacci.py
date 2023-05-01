def fibonnacci(n):
    if n <= 1:
        return n
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

def printFibonacciSequence(n):
    for i in range(n):
        print(fibonnacci(i))

printFibonacciSequence(6)
