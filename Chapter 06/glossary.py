# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/8

glossary = {
    'if': 'conditional judgment',
    'while': 'circulation',
    'break': 'out of circulation',
    'continue': 'go to next circulation',
    'list': 'some of strings'
}

# print("if\n\t" + glossary['if'])
# print("while\n\t" + glossary['while'])
# print("break\n\t" + glossary['break'])
# print("continue\n\t" + glossary['continue'])
# print("list\n\t" + glossary['list'])

for key,value in glossary.items():
    print(key + "\n\t" + value)