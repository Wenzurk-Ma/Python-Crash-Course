# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/6

age = 12

if age < 4:
    price = 0
    # print("Your admission cost is $0.")
elif age < 18:
    price = 5
    # print("Your admission cost is $1.")
elif age < 65:
    price = 10
else:
    price = 5
    # print("Your admission cost is $10.")

print("Your admission cost is $" + str(price) +".")