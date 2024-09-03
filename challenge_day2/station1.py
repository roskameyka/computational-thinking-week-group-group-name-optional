def solution_station_1(observation):

    fibs = [0, 1]
    for i in range(2, observation+1):
        fibs.append(fibs[-1] + fibs[-2])

    outputFibonacciNumber = fibs[-1]

    return outputFibonacciNumber