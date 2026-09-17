#if条件判断  if   :不能忘
# score = int(input("输入你的高考分数"))
# if score > 680:
#     print("欢迎来清华大学读书")
#     print("也恭喜有精彩生活")
# print("----- ")


# account= int(input("请输入账号"))
# possword = int(input("请输入密码"))
# if account == 188888888 and possword == 888:
#     print("账号密码正确!")
# else:
#     print("登录失败!")

# year = int(input("输入年份"))
# if (year % 100 != 0 and year %4 == 0 )  or (year % 400 == 0):
#     print(f"{year} 是闰年" )
# else:
#     print(f"{year} 是平年")
#

# math = int(input("输入数字"))
# if math == 0:
#     print(f"{math} 是0")
# elif math >= 0:
#     print(f"{math} 是正数")
# else:
#     print(f"{math} 是负数")

# account= input("请输入账号")
# possword = input("请输入密码")
# if account == "1" and possword == "a":
#      print("账号密码正确!")
# elif account == "2" and possword == "b":
#      print("账号密码正确!")
# elif account == "3" and possword == "c":
#      print("账号密码正确!")
# else:
#      print("登录失败!")

a = int(input("第一条边:"))
b = int(input("第二条边:"))
c = int(input("第三条边:"))

if a +b >c and a+c>b and b+c>a:
    if a == b and b == c:
        print("等边三角形")
    elif a == b or b == c  or a == c:
        print("等腰三角形")
    else:
        print("三角形")
else:
    print("不能构成三角形")


#模式匹配 match...case