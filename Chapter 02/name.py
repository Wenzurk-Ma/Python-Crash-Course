# Title     : TODO
# Objective : TODO
# Created by: Wenzurk
# Created on: 2018/2/2

name = "ada lovelace"
print(name.title())         # 方法title()出现在这个变量的后面
# 在name.title()中，name后面的句点(.)让Python对变量name执行title()指定的操作。
# title()以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。

# 还有其他几个很有用的大小写处理方法
name = "Ada Lovelace"
print(name.upper())         # 全部大写
print(name.lower())         # 全部小写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
# print(full_name)
# print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)

