# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

alien_0 = {'color': 'green', 'point': 5}

# print(alien_0['color'])
# print(alien_0['point'])

# new_points = alien_0['point']
# print("You just earned " + str(new_points) + " points.")

print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

# print("This alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yellow'
#
# print("This alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 根据外星人的速度决定将其移动多远
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("Now x-position: " + str(alien_0['x_position']))

del alien_0['point']
print(alien_0)