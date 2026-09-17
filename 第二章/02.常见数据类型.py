#常见数据类型----type()获取自变量或变量的类型
from inspect import istraceback

# print("hello")
# print(type("hello"))
#
# print(type(10))
# print(type(13.14))
# print(type(True))
# print(type(False))
# print(type(None))
#
# #isinstance(数据,类型)
# num = 100
# print(isinstance(num,int))
# print(isinstance(num,float))
# print(isinstance(num,bool))
# print(isinstance(num,str))

# #字符串定义三种方式
# s1 = "hello"
# s2 = "world"
# s3 = """
# hello:
#     一起学python
# """
# print(s1)
# print(s2)
# print(s3)
#
# print(type(s1))
# print(type(s2))
# print(type(s3))

#定义字符串 It's very good
# #转义字符 \'   \"  \n  \t
# msg = 'It\'s very good'
# print(msg)
#
# msg2 = "It\'s very good"
# print(msg2)
#
# print("你们好!\n\t我是python")

# s1 = "人生苦短" "我用pppppython" ", ok"
# s2 = "我用python"
# print(s1)

# s1 = "人生苦短"
# s2 = "我用python"
# print("鬼叔说:" + s1 + " , " +s2)

#str(int数字)
name = "名字"
age = 20
pro = "软件工程"
hobby = "python"
print("大家好,我是" + name + ",今年" + str(age) + "岁,学习的专业是" + pro + ",爱好" + hobby )

#  %占位符
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好%s" % (name, age, pro, hobby))

# f"内容{变量/表达式}"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好{hobby}" )












