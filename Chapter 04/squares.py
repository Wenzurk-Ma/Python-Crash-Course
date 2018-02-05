# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/5

# squares = []
# for value in range(1,11):
#     # square = value**2
#     # squares.append(square)
#     squares.append(value**2)
squares = [value**2 for value in range(1,11)]
print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))