# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/10

dog = {
    'name': 'yellow',
    'color': 'yellow',
    'age': 7,
}
cat = {
    'name': 'maruko',
    'color': 'colorful',
    'age': 2,
}
pig = {
    'name': 'piko',
    'color': 'pink',
    'age': 1,
}
pets = [dog, cat, pig]

for pet in pets:
    for key,value in pet.items():
        print(key)
        print("\t" + str(value))