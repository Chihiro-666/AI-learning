student={}

meun="""
##############教务管理系统##############
            1.添加学生信息
            2.修改学生信息
            3.删除学生信息
            4.查询学生信息
            5.列出所有学生
            6.统计班级成绩
            7.退出系统
######################################        
"""
print("欢迎使用教学管理系统！")
while True:
    print(meun)
    num=int(input("请输入所需功能编号："))
    match num:
        case 1 :
            name=input("请输入学生姓名:")
            chinese = input("请输入学生语文成绩:")
            math = input("请输入学生数学成绩:")
            English = input("请输入学生英语成绩:")
            if name in student:
                print("学生信息已经存在，请重新输入~")
            else:
                student[name]={"chinese":chinese,"math":math,"English":English}
                print("学生信息添加完毕~")
        case 2:
            name = input("请输入学生姓名:")
            chinese = input("请输入学生语文成绩:")
            math = input("请输入学生数学成绩:")
            English = input("请输入学生英语成绩:")
            if name not in student:
                print("学生信息不存在，请重新输入~")
            else:
                student[name] = {"chinese": chinese, "math": math, "English": English}
                print("学生信息修改完毕~")
        case 3:
            name = input("请输入学生姓名:")
            if name not in student:
                print("学生信息不存在，请重新输入~")
            else:
                del student[name]
                print("学生信息删除完毕~")
        case 4:
            name = input("请输入学生姓名:")
            if name not in student:
                print("学生信息不存在，请重新输入~")
            else:
                student_mess=student[name]
                print(f"学生姓名:{name}")
                print(f"学生语文成绩:{student_mess['chinese']}")
                print(f"学生数学成绩:{student_mess['math']}")
                print(f"学生英语成绩:{student_mess['English']}")
        case 5:
            if not student:
                print("暂无学生信息")
            else:
                for name in student:
                    student_mess=student[name]
                    print(f"学生姓名:{name}")
                    print(f"学生语文成绩:{student_mess['chinese']}")
                    print(f"学生数学成绩:{student_mess['math']}")
                    print(f"学生英语成绩:{student_mess['English']}")
        case 7:
            print("系统即将退出，再见！")
            break
        case _:
            print("编号不存在，请重新输入~")




