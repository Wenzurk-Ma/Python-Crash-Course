# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

current_users = ['alice', 'alex', 'wenzurk', 'admin', 'bill']
new_users = ['john', 'mario', 'alex', 'bill', 'zurk']

for user in new_users:
    if user.lower() in current_users:
        print("'" + user + "' has been used.")
        print("Please enter another.")
    else:
        print("'" + user + "' is ok!")