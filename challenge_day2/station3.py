def solution_station_3(number):
    #convert the number to a string and sum the digits
    number_sum = sum(int(digit) for digit in str(number))
    
    #check if the sum is divisible by 3
    if number_sum % 3 == 0:
        return True
    else:
        return False
#print(solution_station_3())