'''
Constructor --> Instance Methods --> Public Attributes
Encapsulation
'''
# Constructor --> It is a Special Method (__init__())
# which will automatically initialize the attributes and met to the object in the class


'''
class Cars:
    """Understanding the usage of OOP"""
    def __init__(self,Brand,Name,Price,Colour):
        self.Brand = Brand         # Public Attributes
        self.Name = Name
        self.Price = Price
        self.Colour = Colour
    #Methods(behaviour)
    def details(self):      # Instance Method
        print(f"Car Brand is {self.Brand}")
        print(f"Car Model Name is {self.Name}")
        print(f"Car Price is {self.Price}")
        print(f"Car Colour is {self.Colour}")
Z1 = Cars("Tata","Nexon","9 Lakhs","Blue")
Z1.details()
Z2 = Cars("BMW","Sedans",Colour="White",Price="25 Lakhs")
Z2.details()
'''

'''
class Cars:
    """Understanding the usage of OOP"""
    def __init__(self):
        self.Brand ="BMW"    
        self.Name = "Sedans"
        self.Price = "50 Lakhs"
        self.Colour = "White"
    #Methods(behaviour)
    def details(self):
        print(f"Car Brand is {self.Brand}")
        print(f"Car Model Name is {self.Name}")
        print(f"Car Price is {self.Price}")
        print(f"Car Colour is {self.Colour}")
A1 = Cars()
print(A1.Brand,A1.Name,A1.Colour,A1.Price)
A1.details()
'''

# Encapsulation --> It is One of the main Feature of OOP
# It binds (bundles) the data (Attributes) and the methods (behaviour) into a single unit (class) --> Multiple Objects
# Attributes --> Public, Protected, Private

# Public Attributes --> Attributes defined inside the class (Co) and can be modified outside the class

'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user = username   # Public attribute
    # To Access Student details
    def display(self):
        print(f"Student Username is {self.user}")
U1 = CodegnanPortal("Saketh")
U1.display()
U1.user = "Saketh Kallepu"
U1.display()
print(U1.__dict__)
U2 = CodegnanPortal("Jay")
U2.display()
print(U2.__dict__)
'''


# Protected Attributes --> We use Simple underscorfe before an Attribute. Moreover it can be modified outside the Class also
# and even Accessible in subclasses

'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp):
        self.user = username   # Public attribute
        self._otp = _otp     # Protected attribute
    # To Access Student details
    def display(self):
        print(f"Student Username is {self.user}")
        print(f"Student has received OTP as {self._otp}")
U1 = CodegnanPortal("Saketh",23456)
U1.display()
U1._otp = 3456 
U1.display()
'''

# Private Attributes --> We use Special Notation as Double Underscore such as __password
# They are accessible only inside the class and cannot be directly modified

'''
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username   # Public attribute
        self._otp = _otp      # Protected attribute
        self.__password = password        # Private attribute
    # To Access Student details
    def display(self):
        print(f"Student Username is {self.user}")
        print(f"Student has received OTP as {self._otp}")
        print(f"Student password is {self.__password}")

U1 = CodegnanPortal("Saketh",23456,"admin123")
# print(U1.password)       Attribute Error as Password is Private
print(U1.__dict__)
print(U1._CodegnanPortal__password)        # NameMangling
'''

# In Above Case, we are using Name Mangling. But, The right way is 
# Usage of getter() and setter() methods

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username   # Public attribute
        self._otp = _otp      # Protected attribute
        self.__password = password        # Private attribute
    # Usage of getter() method
    def get_password(self):
        #return "*******"
        return self.__password
    # To Modify the password. we use setter() method
    def set_password(self,new_password):
        if len(new_password) <= 6:
            print("Wrong Password. Not Satisfied 6 Characters")
        else:
            self.__password = new_password
            print("Now password is updated")

U1 = CodegnanPortal("Saketh",23456,"admin123")
print(U1.get_password())
U1.set_password("saketh")
U1.set_password("saketh123")    # Compulsory more than 6
print(U1.get_password())