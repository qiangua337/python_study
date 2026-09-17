__all__ = ["log_separator1",  "log_separator3" , "PI"]

# 定义常量(不会发生变化):名称全大写
PI = 3.1415926
NAME = "牵挂"

def log_separator1():
    print("-" * 30)

def log_separator2():
    print("+" * 30)

def log_separator3():
        print("#" * 30)

def log_separator4():
        print("*" * 30)

# __name__ :内置变量,表示当前模块的名字 (直接运行)
if __name__ == '__main__':
    log_separator1()

if __name__ == '__main__':
    log_separator2()