# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

favorite_numbers = {
    'jen': [5,6],
    'sarah': [6,7],
    'edward': [1,2],
    'phil': [2],
    'wenzurk': [0,1],
}
# print("Jen favorite number is " + str(favorite_language['jen']) + ".")
# print("Sarah favorite number is " + str(favorite_language['sarah']) + ".")
# print("Edward favorite number is " + str(favorite_language['edward']) + ".")
# print("Phil favorite number is " + str(favorite_language['phil']) + ".")
# print("Wenzurk favorite number is " + str(favorite_language['wenzurk']) + ".")

for name,numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + str(number))