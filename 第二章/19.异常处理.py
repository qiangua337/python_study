
# try:
#     print("============")
#     print(my_name)
#     print("============")
# except NameError:
#     print("程序有问题")

try:
    print("============")
    print(1/0)
    print("============")
except NameError:
    print("程序有问题")
except ZeroDivisionError:
    print("0不做被除数")

