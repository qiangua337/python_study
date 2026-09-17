# #函数定义
# def out_line():
#     print("-----------------")
#     print("-----------------")
#
# #调用
# out_line()
# out_line()
# out_line()
#
# import math


# # 函数参数 和 返回值return
# def circle_area(radius):
#
#     area = math.pi * radius * radius
#     return area
# print(f"{circle_area(10):.1f}")
#
#
# def rectangle(width, height):
#     area = width * height
#     return area
# print(f"{rectangle(7.8, 8.99):.1f}")

# def circle_area(radius):
#     """
#     用于计算圆的周长和半径
#     param radius: 半径
#     return: 圆的面积,周长
#     """
#     return round(math.pi * radius * radius , 2) , round(2 * math.pi * radius , 2)
# print(circle_area(float(input("输入"))))
# # print(type(circle_area(10)))
# help(circle_area)

# def f_a():
#     print("a.....1")
#     f_b()
#     print("a.....2")
#
# def f_b():
#     print("b.....1")
#     f_c()
#     print("b.....2")
#
# def f_c():
#     print("c.....")
#
# f_a()

# def triangle_area(b,h):
#     """
#     计算三角形面积
#     :param b:
#     :param h:
#     :return:
#     """
#     return h * b / 2
# print(triangle_area(30,20))

# def count_aeiou(s):
#     num = 0
#     for w in s :
#         if w in "aeiouAOEIU":
#             num += 1
#     return num
# print(count_aeiou(input("输入单词")))
#

def calc_socre(score_list):
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list) , 1)
    return max_s, min_s, avg_s

s_list = [455 , 555 ,444,  333]
print(calc_socre(s_list))

# global  局部变量转化为全局变量

# 不定长参数
# 基于位置参数的不定长参数  *args
