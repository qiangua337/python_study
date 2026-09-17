from random import choice


# 案例:
# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1.
# 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2.
# 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3.
# 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4.
# 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5.
# 列出所有学生：遍历所有学生信息并输出。

# 学生类
class Student:
    def __init__(self, name, chinese , math , english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名:{self.name} | 语文:{self.chinese} |数学:{self.math} |英语:{self.english} | 总分:{self.chinese +self.math +self.english} "

    # 修改学生成绩
    def update_score(self , chinese = None , math = None , english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 教育系统管理类
class EduManagment:
    system_version = "1.0"
    system_name = "教育管理系统"

    def __init__(self, name=None):
        self.student_list = [ ]

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生姓名:")

        # 判断学生姓名是否重复
        for s in self.student_list:
            if s.name == name:
                print("学生存在,添加失败")
                return

        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生成绩添加成功")
        else:
            print("学生成绩要在0-100之间")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入需要修改学生姓名:")

        # 根据学生姓名找到学生信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩:{s}")

                chinese = int(input("请输入修改后学生语文成绩:"))
                math = int(input("请输入学生修改后数学成绩:"))
                english = int(input("请输入修改后学生英语成绩:"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score (chinese, math, english)
                    print("成绩修改成功")
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("学生成绩要在0-100之间")
                    return
        print("未找到学生,修改失败!")

    # 删除学生成绩
    def delete_student(self):
        name = input("请输入需要删除学生姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学会信息删除成功")
                return
        print("未找到该学生,删除失败")


    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入需要删除学生姓名:")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
        print("未找到该学生,查询失败")

    # 查展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    #运行系统方法
    def run(self):
        print(f"欢迎使用教务系统 V{EduManagment.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生  2.修改学生   3.删除学生   4.查询指定学生   5,查询所有学生  6.推出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            choice = input("请输入要执行操作,输入1-6:")
            match choice:
                 case "1":#添加学生
                     self.add_student()
                 case "2":
                     self.update_student()
                 case "3":
                     self.delete_student()
                 case "4":
                     self.query_student()
                 case "5":
                     self.list_student()
                 case "6":
                     print("Bye~")
                     break
                 case _:
                     print("输出错误,请输入1-6")




if __name__ == "__main__":
    edu_management = EduManagment()
    edu_management.run()


