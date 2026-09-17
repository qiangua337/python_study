# #定义类(大驼峰命名法)
# class  Car:
#     pass
#
# #创建对象
# c1 = Car()
# # 动态添加属性
# c1.color = "red"
# c1.brand = "bmw"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1.__dict__)# __dict__:将对象中的属性以字典形式输出出来

# class Car:
#      # __init__:初始化的方法,会在对象创建时自动调用
#      # self :第一个参数,当前所创造出来的第一个实例对象
#      def __init__(self, c_color , c_brand, c_name , c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型初始化完毕")
# # 创建对象
# c1 = Car("红色","BMW","X7","800000")
# print(c1.__dict__)

# class Car:
#      def __init__(self, c_color , c_brand, c_name , c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型初始化完毕")
#
#      def running(self):
#          print(f" {self.brand} {self.name} 正在高度行驶中")
#      def total_cost(self, discount ,rate = 0.1) :
#          # 计算提车总价格
#          return discount * self.price  + rate * self.price
#      # 魔法方法
#      def __str__(self):
#          return f"{self.color} {self.brand} {self.name} {self.price}"
#
#      def __eq__(self,other):
#          return self.color == other.color and self.brand == other.brand
#
#      def __lt__(self, other):
#          return self.price < other.price
#
# c1 = Car("红色","BMW","X7",800000)
# print(c1)
#
# c2 = Car("红色","BMW","X7",800000)
# print(c2)
#
# print(c1 == c2)
# print(c1 < c2)

class Car:
    # 类属性,先输出实例属性,没有就输出类属性
    wheel = 4
    tax_rate = 0.1

    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        # self.wheel = 2
        print("Car类型初始化完毕")

    def running(self):
        print(f" {self.brand} {self.name} 正在高度行驶中")

    def total_cost(self, discount, rate=0.1):
        # 计算提车总价格
        return discount * self.price + rate * self.price



c1 = Car("红色", "BMW", "X7", 800000)
print(c1.name)
print(c1.wheel)

# c2 = Car("白色", "byd", "汉", 180000)
# print(c2)

