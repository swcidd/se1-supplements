##Write a function named calculate_parking_fee(hours) that takes the number of hours parked (as a float). The garage charges a flat rate of $5.00 for the first 2 hours. After that, it charges an additional $2.50 per hour (or fraction of an hour). The function should return the total fee.
##Hint: You may want to use math.ceil() to handle partial hours after the first 2 hours)

import math

def calculate_parking_fee(hours):
    if hours <= 2.0:
        return 5.0
    else:
        rounded_hours = math.ceil(hours - 2)
        return 5.0 + (rounded_hours * 2.5)

print(calculate_parking_fee(1.5)) 
print(calculate_parking_fee(3.0))  
print(calculate_parking_fee(3.1))