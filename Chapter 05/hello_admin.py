# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/7

admins = []


if admins:
    for admin in admins:
        if admin == 'admin':
            print("Hello " + admin + ", would you like to see a status report?")
        else:
            print("Hello " + admin + ", thank you for logging in again.")
else:
    print("We need to find some users!")