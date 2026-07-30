#numeric Datatype-->int,float,complex,along with boolean
#input formating -->Accepting input from the user-->input()
#Accepting integer input from user
#by default input() accept any input-->str
#int(input()) --> will accept only integerrs
'''
age=int(input('enter the age:'))
print(age)
print(type(age))
'''

#float(input())
'''
age=float(input('enter the age:'))
print(age)
print(type(age))
'''

#acepting string input from user
'''
name=input('enter the name:')
print(name)
print(type(name))
'''
#space separated valuse
'''
a=input('enter the value:').split()
pirnt(a)'''
#comma separated values
'''
a=input('enter the value:').split(',')
print(a)'''

#list of integers(why list because we didnt mentioned number of values 
'''
marks=list(map(int,input('enter the values:').split(',')))
print(marks)
'''
#now we want to accept 2 values from user
'''
age,salary=map(int,input('enter the values:').split(','))
print(age)
print(salary)
'''
#single input -->int(input())
#two inputs -->a,b = (int,input().split(','))
#any number result as list -->a = list(map(int(,input().split(',')))


#float of integers
'''
marks = list(map(float,input('enter the values:').split(',')))
print(marks)
'''
#group of float values
'''
age,salary = map(float,input('enter the values').split(','))
print(age)
print(salary)
'''
'''
#accepting input from user --> int,float-->input formating
#operators -->operators perform operations between values (operands)
#7Types -->Arithemetic,Assignment,comparision (Relationship)
#arthemetic operators -->Arithmetic operations
#+,-,*,/
print(5+3)
print(5*3)
print(5-3)
#Floor division (integeer division) --> return quotient
print(5//3)
#Modulous -->divisible rules ->return remainder
print(5%3)
print(5/3)#float value

#power (exponential)
print(5**3)
'''
#Task --> Accept integer input as length,bradth -->find the area of rectangle
#area = length * breadth
'''
length,breadth= map(int,input('enter the values:').split(','))
a=length*breadth
print(a)
'''
#assignment Operators -->assign the values
# =, +=, -=
'''
a = 45
print(a)
#update the value of a
a=a+5
print(a)
b=67
b=b+a
print(b)
b =b-7
print (b)

'''
#Task : *=,/=,//=,%=,**= workout

#comparision operators --> we compare the values -->boolean
# == (equal to ), !=(not equal to) ,<(less than), > greater than
#<= lessthan or equal to) >= greater than or equal to



#membership operator -->in , not in -->boolean
#it check for thr existanse of an object in a collection
'''
marks = [56,74,98,65]
print(58 in marks)
print(78 not in marks)
print('sha' in 'shashank')
'''
#logical operators --> logical decision making --> and,or,not
#and -->all conditions to be satisfied
#or --> any one  condition to be satisfied
'''
a=(45 in[23,45,78]) and 45> 23
print(a)
b=24<=45 and 54<=14 
print(b)
'''

#identity operators -->check for identity of an object-->id()
#is,is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)







