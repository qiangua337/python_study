# #字符串
# s = "hello python"
#
# print(s[4])
# print(s[-7])
#
# for i in s:
#     print(i)
#
# print(s[:5])
# print(s[-6:-10:-1]
#

# 验证邮箱格式
mail = input("输入邮箱:")
if mail.count("@") and "." in mail:
    print("有效邮箱")
else:
    print("非法邮箱")
