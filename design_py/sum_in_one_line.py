# print("\n#1. one line in sum with user input value :- \n")
# print("Ans is : ",int(input("Enter 1st Value : ")) + int(input("Enter 2nd Value : ")))


# print("\n #2. Area and Circumference Calculate :- \n")
# import math
# r=float(input("Enter radius : "))
# print("Area is = ",math.pi*math.pow(r,2))
# print("Circumference is = ",math.tau*r)


print("\n #3. get name, age, print name, and display 100 years in the year 2090:- \n")

import datetime

x = eval('print("hellow")')
today = datetime.date.today()
y = today.year
name = str(input("What is your name? \n"))
age = int(input("What is your age? \n"))
print("Hello ", name)
year = y - age + 100
print("You will be of 100 years in the year : ", year)
