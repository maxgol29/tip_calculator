import math as m
print("Welcome to the tip calculator!")

total = float(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))


def calculation(total, tip, number_of_people):
    if tip not in [10, 12, 15]:
        tip = 12
        print("Unfortunately, we only receive 10, 12, or 15 percent of total bill, so we would get 12%!")
    print(f"Each person should pay: ${round((total+total*tip/100) / number_of_people, 2)}")

calculation(total, tip, number_of_people)
