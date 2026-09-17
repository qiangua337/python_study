#match..case  模式匹配;工作日安排
# day = input("请输入星期几(1-7)")
# match day:
#     case "1":
#         print("周一:工作会议日")
#     case "2":
#         print("周二:工作会议日")
#     case "3":
#         print("周三:工作会议日")
#     case "4":
#         print("周四:工作会议日")
#     case "5":
#         print("周五:工作会议日")
#     case "6"|"7":
#         print("周末:休息")
#     case _:
#         print("输入错误")


#简易计算器
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
oper = input("输入运算符(+ - * /):")
match oper:
    case "+":
        print(f" {num1} +{num2} = {num1 + num2}")
    case "-"  :
        print(f" {num1} - {num2} = {num1 - num2}")
    case "*":
        print(f" {num1} * {num2} = {num1 * num2}")
    case "/" if num2 !=0:
        print(f" {num1} /{num2} = {num1 / num2}")
    case _ :
        print("操作不支持!!!")
