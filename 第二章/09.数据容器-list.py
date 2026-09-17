# s = [32 , 45 , 67 , "hello" , True]
# # print(type(s))
# #
# # print(s[0])
# # print(s[-5])
#
# # 替换
# s[3] = "ttttt"
# print(s)
#
# # 删除索引  del
# del s[1]
# print(s)
# print(s[2])
#
# for i in s:
#     print(i,end="  ")

# # 序列元素[开始索引:结束索引:步长],不包含结束索引
# s = [11,22,33,44,55,66,77,88,99]
#
# s.append(33)
# print(s)
#
# s.insert(1,33)
# print(s)
#
# s.remove(22)
# print(s)
#
# a = s.pop(3)
# print(s)
# print(a)
#
# s.reverse()
# print(s)
#
# s.sort()
# print(s)
#
# s = [ ]
# # for i in range(10):
# #     num = int(input("输入数字:"))
# #     s.append(num)
# # print("添加后的数组",s)
# #
# # s.sort()
# # print(s)
# #
# # # sum(求和)
# # print("最小值",s[0])
# # print("最大值",s[-1])
# # print("平均值",sum(s)/len(s))
#
# #合并列表 去处重复
# num1 = [22,33,44,55,77,99,44]
# num2 = [22,44,66,88,]
#
# # for num in num1:
# #     num2.append(num)
# # 将列表元素解包,*    组包
# # num12 = [*num1,*num2]
# num12 = num1 + num2
# print(num12)
#
#
# new_list = []
# for num in num12:
#     if num not in new_list:
#       new_list.append(num)
# print(new_list)


# num_list = []
# for i in range(1,21):
#      num_list.append(i**2)
# print(num_list)
#
# #列表推导式: 按照一定规则快速生成列表: [要插入的值 for i in 序列/列表]
# num_list2 = [i**2  for i in range(1,21) ]
# print(num_list2)

# # [要插入的值 for i in 序列/列表 if 条件]
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mew_list = [i**2 for i in num_list if i % 2 == 0]
# print(mew_list)
#

list =[1,2,3,4,5,6,7,8,9,10,11,12,13,-14,15,1-6,17,-18,19,-20,21,22,23,-24,-25,26,-27,28,29,30,31]
new_list = [ i for i in list if i >0]
print(new_list)

 