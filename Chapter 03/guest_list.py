# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/3

# 3-4 create
guest_list = ['Alice', 'Alex', 'Dream']

print(guest_list[0] + ", would you like have a dinner together? ")
print(guest_list[1] + ", would you like have a dinner together? ")
print(guest_list[2] + ", would you like have a dinner together? ")

# 3-5 change
print("I'm sorry, Mr." + guest_list[2] + " could not come here.")
guest_list[2] = 'Money'
print(guest_list[0] + ", would you like have a dinner together? ")
print(guest_list[1] + ", would you like have a dinner together? ")
print(guest_list[2] + ", would you like have a dinner together? ")

# 3-6 append
print("It's lucky for me to find a bigger table for dinner.")
guest_list.insert(0,'Dream')
guest_list.insert(2,'Time')
guest_list.append('Live')
print(guest_list[0] + ", would you like have a dinner together? ")
print(guest_list[1] + ", would you like have a dinner together? ")
print(guest_list[2] + ", would you like have a dinner together? ")
print(guest_list[3] + ", would you like have a dinner together? ")
print(guest_list[4] + ", would you like have a dinner together? ")
print(guest_list[5] + ", would you like have a dinner together? ")

# 3-9 length
print("You have " + str(len(guest_list)) + " guests.")

# 3-7 del
print("I'm very sorry that the table cannot be sent on time, so I just have two guests.")
print(guest_list.pop(0) + ", you are out.")
print(guest_list.pop(1) + ", you are out.")
print(guest_list.pop(1) + ", you are out.")
print(guest_list.pop(2) + ", you are out.")
print(guest_list[0] + ", you are still here.")
print(guest_list[1] + ", you are still here.")
del guest_list[0]
del guest_list[0]
# 删除数据时注意位置变化！！！
print(guest_list)