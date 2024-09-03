
# fibonacci number function using recursion, found from https://www.geeksforgeeks.org/python-program-to-print-the-fibonacci-sequence/
def fibonacci(n):

    # if input is < 0 error is thrown
    if n < 0:
        raise Exception("Inputs < 0 do not work with Fibonacci")

    # if input is 0, 0 is returned
    elif n == 0:
        return 0

    # if input is 1 or 2, 1 is returned
    if n == 1 or n == 2:
        return 1

    # in all other cases, recursion is used to find number
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def solution_station_1(observation):

    #using fibonacci recursion function to get number
    outputFibonacciNumber = fibonacci(observation)

    return outputFibonacciNumber
