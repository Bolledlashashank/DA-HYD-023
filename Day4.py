'''
#identiti operators --> check the identity of an object --> id()

a=5
b=a
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)
'''
'''
a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#as we have lists (Mutable collection) both c and a lists will have different
#id whereas values are same
print(c is a)
print(c==a)

'''

'''
#Bitwise operators --> we perform bit wise operations over operands
#& (and) , | (or),^(XOR), shifting operators (<<,>>)
print(5&3) #both 5 and 3 to be converted binary and bit wise and is performed
print(5|3) # bitwise OR
print(5^3) #bitwise XOR
print(5 and 3)#here and is logical operator checks for both existance
#return 5 in above case
print(5 or 3)#here it returns to 4 in this case
'''
'''
#left operator << , right shift operator>>
print(5 < 1)#False comparision
print(15 <<2 )#left shift operation
print(15 >>2 )#Right shift operation

'''

'''
Print(15 << 2) #convert 15 to binary and perform 2 times left shifting
print(15>>2) #same 2 times right shifting

#input formatting --> input(), int(input()) , float(input())
# you know --> single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(",")))

names = input("enter the names:").split(",")
print(names)
name1,name2 = map(str,input("enter the names:").split(','))
print(name1,name2)

'''

#conditional statements
'''
If <condition>:
    statements(s)....
    ....
'''
#age
'''
age = int(input("enter the age:"))
if age >=18:
    print('your age is:',age)

age=int(input("enter the age:"))
if age>=18 and age in [19,20,25]:
        print('your age is',age)
print(age)

'''
'''
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    years = 18 - age
    print("You are not eligible to vote.")
    print("You need to wait", years, "more years.")

'''

#marks
marks= int(input("enter the marks:"))
if marks >=0 and marks <=100 :
    if marks >= 90 :
        print("you got grade: A")
    if marks >= 80 and marks <= 89 :
        print("you got grade: B")
    if marks >= 70 and marks <= 79 :
        print("you got grade: c")
    if marks >= 60 and marks <= 69 :
        print("you got grade: D")
    if marks < 60 :
        print ("you got failed")
else :
    print("Enter only +ve values greater than 0 and less than 100 ")




