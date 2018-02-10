# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/10

favorite_places = {
    'jen': ['chengdu', 'lijiang'],
    'sarah': ['dali'],
    'edward': ['lasa', 'chongqing'],
    'phil': ['guangzhou', 'shanghai'],
}

for name,places in favorite_places.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for place in places:
        print("\t" + place.title())