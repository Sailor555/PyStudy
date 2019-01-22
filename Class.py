

#------------------------类---------------------------
# （1）{方法、类变量、特性}的集合
# （2）生成一个类对象，充当着命名空间（与模块极为相似）

class Person(object):
    count = 0   #类变量，实例间共享
    def __init__(self, name='NoName', age=0):
        self.name = name    #实例变量属性
        self.age = age
        Person.count += 1
    def __del__(self):
        Person.count -= 1
    def __str__(self):
        return '{Name : %s, Age : %d}' % (self.name, self.age)
    def __repr__(self):
        return 'Person("%s", %d)' % (self.name, self.age)
    def __call__(self):
        return Person.__str__(self)
    def self_introduction(self):    #实例方法
        print(Person.__str__(self))