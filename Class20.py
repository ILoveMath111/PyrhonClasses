"""Current date and time
Outline:
Write a program to check the current date and time?"""

from datetime import date,time,datetime
today=date.today()
now=datetime.now()
print("Today's date is", today)
print("Current date and time is", now)
print("Actual date",today.year,"-",today.month,"-",today.day)



"""Random date and time
Outline:
Write a program to generate a random date and time from the given start and end dates"""

import random
import time
def getRandomDate(startDate,endDate):
    print("Printing random date between",startDate,"and",endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'
    startTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate,dateFormat))
    randomTime=startTime+randomGenerator*(endTime-startTime)
    randomDate=time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate
print("Random date =",getRandomDate("1/7/2016","12/12/2018"))



"""Trip expenditure
Outline:
Write a program to calculate the total trip
expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip"""

def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "Skibidi"==city:
        return 6767
    elif "Tampa"==city:
        return 220
    elif "Pittsburgh"==city:
        return 222
    elif "Cairo"==city:
        return 1745
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("Cost of car rental:",rental_car_cost(9))
print("Cost of plane ride:",plane_ride_cost("Skibidi"))
print("Cost of hotel room:",hotel_cost(12))
print("Total cost of the trip:",trip_cost("Skibidi",12,500))
print("If you want to go to some other place like cairo then this will be your cost:",trip_cost("Cairo",8,500))