class Student:
    def __init__(self,name,chinese,math,english):
        #属性名=参数名
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学{self.math} | 英语：{self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english

class EduManagement:
    system_version="1.0.0"
    system_name="教务管理系统"

    def __init__(self):
        self.student_list=[]  #学生成绩信息

    #添加学生信息
    def add_student(self):
        name=input("请输入学生姓名：")
        for s in self.student_list:
            if s.name==name:
                print("该学生已存在，添加失败")
                return

        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english=int(input("请输入学生英语成绩："))

        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu=Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("已添加成功！")
        else:
            print("学生各科成绩要在0-100之间")

    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩：{s}")

                chinese = int(input("请输入学生修改后的语文成绩："))
                math = int(input("请输入学生修改后的数学成绩："))
                english = int(input("请输入修改后的学生英语成绩："))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print("已修改成功！")
                    print(f"修改后的成绩：{s}")
                    return
                else:
                    print("学生各科成绩要在0-100之间")
                    return
        print("未找到该学生，修改失败")

    #删除学生
    def del_student(self):
        name = input("请输入要删除的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("删除成功！")
                return
        print("未找到该学生，删除失败！")

    #查询
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print("查询成功！")
                print(f"该学生成绩为：{s}")
                return
        print("未找到该学生，查询失败！")

    #展示所有学生信息
    def list_student(self):
        for s in self.student_list:
                print(s)

    #运行系统
    def run(self):
        print(f"欢迎使用教务管理系统 V{EduManagement.system_version} ")

        while True:
            print()
            print("#####################################################################")
            print("#1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统")
            print("#####################################################################")
            choice=input("请选择要执行的操作，输入1-6:")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("Bye~")
                        break
                    case _:
                        print("请输入1-6的数字")
            except ValueError as e:
                print("输入数据有问题，请重新输入！")
                #contuine
            except Exception as e:
                print("程序运行出错了，请重新选择！")

if __name__ == "__main__":
    edu=EduManagement()
    edu.run()