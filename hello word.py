'''
定义一个学生类
'''
# 定义一个空的类
class Student():
    pass

# 定义一个对象
mingyue=Student()

# 再定义一个类，用来描述所有听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name=None
    age=18
    course="Python"


# 需要注意
# 1. def Homework的缩进层级
# 2. 系统默认有一个self函数
    def doHomework(self):
        print("I am doing homework!")
        # 推荐在函数末尾使用return语句
        return None
# 实例化
ZoeHu=PythonStudent()
ZoeHu.age=20
ZoeHu.course="Math"
ZoeHu.doHomework()
