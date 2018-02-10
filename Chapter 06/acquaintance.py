# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

acquaintance_0 = {
    'first_name': 'wenzurk',
    'last_name': 'ma',
    'age' : 21,
    'city': 'chengdu'
}
acquaintance_1 = {
    'first_name': 'zurk',
    'last_name': 'ma',
    'age' : 21,
    'city': 'chengdu'
}
acquaintance_2 = {
    'first_name': 'wen',
    'last_name': 'ma',
    'age' : 21,
    'city': 'chengdu'
}
acquaintances = [acquaintance_0, acquaintance_1, acquaintance_2]

for acquaintance in acquaintances:
    print(acquaintance['first_name'].title())
    print(acquaintance['last_name'].title())
    print(acquaintance['age'])
    print(acquaintance['city'].title())