#for循环: 遍历输入的字符串

# msg = input("输入要遍历的字符串")
# for i in msg:
#     print(f"元素:{i}")

#案例  计算1-100奇数的和
# # range语句   range(start,end,step)(不包含end)
# total = 0
# for i in range(1,101,2):
#         total +=  i
# print(total)

#案例  计算100-500的三的倍数的和
# # range语句   range(start,end,step)(不包含end)
# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total +=  i
# print(total)

#打印长方形
# print("*",end=" "),以什么方式结束,默认是换行 end="\n"
# m = int(input("输入长度"))
#
# n = int(input("输入宽度"))


# for j in range (n):
#     for i in range (m):
#         print("*",end=" ")
#     print() #调用默认换行


#打印99乘法表
# for i in range(1,10):
#     for j in range (1,i+1):
#         print(f"{j}*{i}={j*i}",end="\t")
#     print()

#打印等腰直角三角形
# a = int(input("输入边长"))
# for i in range(a):
#     for j in range(i+1):
#         print("*",end="  ")
#     print()

#打印数字金字塔
# a = int(input("输入最大数字"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(f"{j}",end="  ")
#     print()
#
#打印国际棋盘
# a = int(input("输入国际棋盘边长:"))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if (i+j) % 2 == 0:
#             print("♥", end="  ")
#         else:
#             print("♡", end="  ")
#     print()

#案例,直到登陆成功---while循环
# break只能出现循环中,结束或者跳出循环
# continue 只能在循环中

#猜数字
import random
from operator import truediv

random_num = random.randint(1,100)  #生成随机数

while True:
    num = int(input("输入一个数字"))
    if num > random_num:
        print("数字太大")
    elif num < random_num:
        print("数字太小")
    else:33
        print("输入对了666")
        break

print("随机的数字是:",random_num)