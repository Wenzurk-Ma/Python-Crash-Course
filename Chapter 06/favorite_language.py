# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

# favorite_languages = {
#     'jen': 'Python',
#     'sarah': 'C',
#     'edward': 'ruby',
#     'phil': 'Python',
# }

# friends = ['phil', 'sarah']
# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# for name,language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")

# for name in favorite_languages.keys():
#     print(name.title())
#
#     if name in friends:
#         print(" Hi " + name.title() + ", I see you favorite language is " + favorite_languages[name].title() + "!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# print("The following languages have been mentioned: ")
# for language in favorite_languages.values():
# for language in set(favorite_languages.values()):
#     print(language.title())
# name_list = ['jen', 'sarah', 'alex', 'wenzurk']
# for name in name_list:
#     if name in favorite_languages.keys():
#         print("Thank you very much!")
#     else:
#         print("Would you like this?")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())