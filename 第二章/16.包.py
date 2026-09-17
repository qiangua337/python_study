# 1. 导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
#
# from utils import my_fun
# my_fun.log_separator1()

# 如果要通过from utils import *导入包下所有文件,需要在__init__.py 文件中添加__all__=[ ]
from utils import *
my_fun.log_separator1()