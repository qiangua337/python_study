
# 基于位置参数的不定长参数  *args  元组
# def calc(*args):
#     min_data = min(*args)
#     max_data = max(*args)
#     avg_date = sum(args) / len(args)
#     return min_data, max_data, round(avg_date , 1)
# print(calc(22,44,66,33))

# 基于关键字参数的不定长参数  **kwargs  字典
# def calc(*args,**kwargs):
#     min_data = min(*args)
#     max_data = max(*args)
#     avg_date = sum(args) / len(args)
#
#     if kwargs.get('print') is not None:
#         avg_date = round(avg_date , kwargs.get("round"))
#     if kwargs.get('print') is True:
#         print(min_data,max_data,avg_date)
#
#
#     return min_data, max_data, avg_date
#
# print(calc(34,11,67,37,round=3 , print=True))



#匿名函数 lambda 参数列表:函数体  (无法直接调用,先=给其他字符使用)
# out_line  = lambda  :print("hello")
# out_line()

# add = lambda x, y: x + y
# print(add(3,4))
#
# date_list = ["c++", "c", "Java", "Python"  ]
# print(date_list)
#
# date_list.sort(key=lambda x: len(x))
# print(date_list)

#阶乘
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n-1)
#
# print(jc(10))
#



"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""



a : int =10
print(a)















