# encoding=UTF-8
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性 name&age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        """模拟小狗被命令时翻滚"""
        print (self.name.title()+ " is roll over")

if __name__ == "__main__":
    dog = Dog("harri",3)
    dog.sit()
