# -*- coding: utf-8 -*-
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''

# print('''n = 123
# f = 456.789
# s1 = \'Hello, world\'
# s2 = \'Hello, \\\'Adamr'\\\'\'
# s3 = r\'Hello, \"Bart\"\'
# s4 = r\'\'\'Hello,
# Lisa!\'\'\'''')

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
# s1 = 72
# s2 = 85
# print(float(s1) / s2)
# r = (float(s2) - s1) / s1
# print('%.2f' % r)

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# # 打印Apple:
# print(L[0][0])
# # 打印Python:
# print(L[1][1])
# # 打印Lisa:
# print(L[2][2])

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 体重除以身高的平方
# height = 1.75
# weight = 80.5
# bmi = weight / pow(height, 2)
# if bmi < 18.5:
#     print("过轻")
# elif bmi < 25:
#     print("正常")
# elif bmi < 28:
#     print("过重")
# elif bmi < 32:
#     print("肥胖")
# else:
#     print("严重肥胖")

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('hello,' + name)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s,str)]
# print(L2)

# 杨辉三角
# def triangles():
#     L = [1];
#     length = 1;
#     while True:
#         yield L
#         length += 1;
#         temp = L
#         L = [1,1]
#         index = 1
#         while index <= length - 2:
#             L.insert(index,temp[index-1] + temp[index]);
#             index += 1
# 能实现杨辉三角，但是效率太低了，每次都创建一个新的列表
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def normalize(name):
#     name = str(name).lower();
#     name = str(name[0]).upper() + name[1:];
#     return name;

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# 编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

# def prod(L):
#     def add(x,y):
#         x += y
#         return x
#     return reduce(add,L)
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# def str2float(s):
#     def char2num(char):
#         num = int(char)
#         return num
#     def sum(x,y):
#         x = x*10 + y
#         return x
#     array = str(s).split('.')
#     integer = reduce(sum,list(map(char2num,array[0])))
#     floatnum = reduce(sum,list(map(char2num,array[1])))
#     print(integer,floatnum,1/pow(10,len(array[1])))
#     floatnum = floatnum / pow(10,len(array[1]))
#     return integer+floatnum
# print('str2float(\'123.456\') =', str2float('123.456'))

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))