'''
oop --> Class,object,methods (__init__())
encapsulation --> public,protected,private
inheritance--> it is one of key feature of oop where we inherit the the properties (attributes/methods) from one class
to another class(base class (parent class) --> derived class(child class))
whatsaapp --> personal user,business user(catalog),community admin
featuress-->code reusability, avoiding code Duplication,code maintainability,polymorphism (method overriding,method overlading, operator overloading __add__,__str__)

Types: single inheritance(finger print
-->one child class inheriting properties from one parent class multiple inheritance (mother,father -->(child)-->one child))
class inheriting properties from two parent classes
Multilevel Inheritance (grandparent --> parent -->child)
level by level
heirarical inheritance-->multiple child classes inheriting properties from single parent
Hybrid inheritance-->it can carry one or more type of inheritances

syntax:
single inheritance:
class baseclass:
    statement(s)..
    ....
class Derivedclass(baseclass)
    ......
    .....
'''
#whattsapp scenario-->personal user,business user
'''
class user:
    """single inheritance usage"""
    def send_message(self):
        print('sending message')
    def voice_call(self):
        print('making voice calls')
    def video_call(self):
        print('making video calls')
class Businessuser(user):
    #pass
    def create_catalog(Self):
        print("displaying products catalog")
u1 = Businessuser()
print((dir(u1)))
u1.send_message()
u1.voice_call()   
u1.video_call() 
u1.create_catalog()
'''
#social media login-->user-->update_users scenario
'''
class users:
    """single inheritance usage"""
    company = "Sr university"#class attribute 
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return self.fname + self.lname
#u1=users("shashank","Reddy")
#print(u1.full_name())
#print(u1.company)
class update_users(users):
    def update_name(self):
        return self.fname.title()+""+self.lname.title().strip(',')
u1=update_users("Shashank"," Reddy")
print(u1.company)
print(u1.full_name)
print(u1.update_name())
u2 = users("Bolledla","shashank")
print(u2.full_name())
print(u2.company)
'''
#father --> kid (property)
'''
class Father:
    """usage of constructor in single inheritance"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'Father property is: {self.property}')
class kid(Father):
    """Now childclass will have constructor"""
    def __init__(self):
        self.property=200000
    def kid_property(self):
        print(f'kid property is {self.property}')
    #pass
obj = kid()
obj.father_property()
obj.kid_property()
'''
#parent class having constructor child class having contructor so constructor overriding is happening
'''
To avoid constructor overriding we start using "super()" method
usage of super() method types

1. super(). __intit__
2.super.__init__(args)
3.super().method() method overriding
'''
class Father:
    """usage of constructor in single inheritance"""
    def __init__(self):
        self.property=100000
    def father_property(self):
        print(f'Father property is: {self.property}')
class kid(Father):
    """Now childclass will have constructor"""
    def __init__(self):
        super().__init__()
        self.cash=200000
    def kid_property(self):
        print(f'kid property is {self.cash}')
    #pass
obj = kid()
obj.father_property()
obj.kid_property()














