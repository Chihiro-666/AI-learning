from abc import ABC, abstractmethod
import json

#书籍类
class Book:
    def __init__(self,book_id,title,author,total_num):
        self.book_id = book_id      #编号
        self.title = title          #标题
        self.author = author        #作者
        self.total_num = total_num  #数量
        self.__available_num = total_num #可用数量

    def borrow_book(self):
        if self.__available_num >0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self):
        self.__available_num += 1
        return True

    def get_available_num(self):
        return self.__available_num

#抽象类：不能被实例化，只能被继承的类；作用：定义类的模板，强制子类实现某些方法。
#Python中的抽象类，需要继承abc模块中的ABC类，并使用abstractmethod装饰器来定义抽象方法。

#会员类
class Member:
    def __init__(self,member_id,name,password):
        self.member_id = member_id  #卡号
        self.name = name            #名称
        self.__password = password  #密码
        self.__borrowed_books = []    #借出的书籍

    #父类统一提供获取密码方法
    def get_password(self):
        return self.__password

    # 借书
    def borrow_book(self,book:Book):
        #判断当前会员借阅数量是否达到限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print(f"会员{self.member_id}借阅数量达到限制，不能借阅")
            return False
        #获取会员最大可借阅的数量（子类中实现）
        #判断书籍是否可以借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"会员{self.member_id}成功借阅《{book.title}》")
            return True
        else:
            print(f"会员{self.member_id}借阅失败,书籍《{book.title}》已借出")
            return False

    # 还书
    def return_book(self,book:Book):
        #判断书籍是否在会员借阅列表中
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.return_book()
            print(f"会员{self.member_id}成功还书《{book.title}》")
            return True
        else:
            print(f"会员{self.member_id}还书失败,未借阅该书籍《{book.title}》")
            return False

    # 获取会员最大可借阅数量
    @abstractmethod     #装饰器，表示该方法为抽象方法
    def get_max_books(self)->int:
        pass

    def get_borrowed_books(self):
        return self.__borrowed_books

#普通会员
class NormalMember(Member):  #继承Member类
    def get_max_books(self)->int:
        return 3


#VIP会员
class VIPMember(Member):  #继承Member类
    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level

    def get_max_books(self)->int:
        return 6+self.vip_level

class LibrarySystem:
    def __init__(self):
        self.books = {}  # 书籍列表--->{“AIoo1":Book}
        self.members = {}  # 会员列表--->{“N001”:Member}
        self.current_member: Member|None = None  # 当前会员--->Member
        #加载数据（书籍，会员）
        self.load_books_data()
        self.load_members_data()

    #加载书籍数据
    def load_books_data(self):
        with open('data/books.json','r',encoding='utf-8') as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book["编号"]] = Book(book["编号"],book["标题"],book["作者"],book["数量"])
            print("书籍数据加载完成")

    #加载会员数据
    def load_members_data(self):
        with open('data/members.json','r',encoding='utf-8') as f:
            members_data = json.load(f)
            for member in members_data:
                if member["卡号"].startswith("N"):
                    self.members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])
                else:
                    self.members[member["卡号"]] = VIPMember(member["卡号"], member["姓名"], member["密码"],
                                                             member["会员等级"])

            print("会员数据加载完成")

    #登录
    def login(self):
        while True:
            print("\n")
            print("【登录】")
            member_id = input("请输入会员卡号：")
            password = input("请输入密码：")

            if member_id in self.members:
                if self.members[member_id].get_password() == password:
                    self.current_member = self.members[member_id]
                    print(f"登录成功，欢迎您，{self.current_member.name}！")
                    return True
                else:
                    print("登录失败，密码错误！")
                    continue
            else:
                print("登录失败，会员卡号不存在！")
                continue

    # 借书
    def borrow_book(self):
        print("【图书列表】")
        #展示所有书籍
        for book in self.books.values():
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}，数量：{book.total_num}，可借数量：{book.get_available_num()}")

        book_id = input("请输入图书编号：")
        if book_id in self.books:
            book = self.books[book_id]
            self.current_member.borrow_book(book)
        else:
            print("借阅失败，该图书不存在！")

    # 还书
    def return_book(self):
        print("【已借阅图书列表】")
        borrowed_books = self.current_member.get_borrowed_books()
        for book in borrowed_books:
            print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}")

        book_id = input("请输入归还图书编号：")
        if book_id not in self.books:
            print("归还失败，该图书不存在！")
        else:
            self.current_member.return_book(self.books[book_id])

    # 查询已借阅的图书
    def show_borrowed_books(self):
        if len(self.current_member.get_borrowed_books()) > 0:
            print("【已借阅图书列表】")
            for book in self.current_member.get_borrowed_books():
                print(f"编号：{book.book_id}，标题：{book.title}，作者：{book.author}")
        else:
            print("您当前没有借阅任何图书！")

    # 运行
    def run(self):
        if self.login():
            while True:
                print("\n")
                print("【主菜单】")
                print("1. 借阅图书")
                print("2. 归还图书")
                print("3. 查询借阅")
                print("4. 退出系统")

                choice = input("请选择操作（1-4）：")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("Bye~感谢您的使用，欢迎下次光临！")
                        break
                    case _:
                        print("无效的选择，请重新输入！")


if __name__ == "__main__":
    ls = LibrarySystem()
    ls.run()
