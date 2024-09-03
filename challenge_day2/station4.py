def solution_station_4(observation):

    prime = True

    if observation > 1:
    
        # iterating from 2 to input // 2
        for i in range(2, (observation//2)+1):
        
            # checking if input is divisible by any number from 2 --> n/2, to determine whether it is prime or not
            if (observation % i) == 0:

                #setting variable to false if not prime
                prime = False
                break
    else:
        prime = False

    return prime