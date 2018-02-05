# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/5

pizza_list = ['meat', 'meat2', 'meat3', 'meat4']
friend_pizzas = pizza_list[:]

pizza_list.append('meat5')
friend_pizzas.append('meat6')

print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)
    # print("I like " + pizza + " pizza.")

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)