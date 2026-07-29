'''
tokens --> variables, puctuators
variables --> Named memory location, its a placeholder for data
#Rule are to be followed
'''
#multiassignment of variables
'''
name,age,place='shashank',22,'warangal'
print(name,age,place,sep=',' )
print(name,age,place,sep='-->' )
print(name,age,place,sep='\n' )
'''
#a,b=2,3,4,#value error as too many values to unpack

#reassigning variables
'''
name="shasshank"
a,b=45,7.8
print(a,b)
a,b=b,a
print(a,b,sep=',')
'''
#a,b=b,c#Name Error because c is not defined
#print(a,b)
#deleting the variables -->
'''
del a
print(b)
'''

#puctuators --> []( list ),ArithmeticError (tuple),{} (Dict,sets)
#sep='\n' helps to separate the output element in step by step
'''
name ="shashank";age = 22;course = "Data analytics"
print(name,age,course,sep='\n')
'''
#Datatypes-->Numetric (int,float,complex,boolean,None)
         #-->Sequences(lists,Tuple,Sets,Strings)
         # Frozensets,mapings(dict)

#numeric type -->int,float,complex
#int datatype-->quntity, age
         
'''
age=7
print(age)
print(type(age))#type-->returns the data type of object
print(type(1234))
'''

#quantity = 03 #it is not allowed
#print(quantity)
#float datatype -->temp,sal,price
'''

price=850.24;discount=7.4
print(price,discount,sep=',')
print(type(price))

'''

#complex-->combination of real and imag# a variable cannot be started with the integer
'''
i2=17
data=7+i2
print(data)
print(type(data))

data=7+2j
print(data)
print(type(data))
'''

#Boolean--> True/False

'''
valid = True
print(type(valid))
error = False
print(type(error))

'''

#type casting --> converting one type to another type
#python ny default follows implicit type(we need not mention the data type )

#every built in data type is built in function
#int,float,complex,bool
#typecating float--> int, complex,bool
'''
age=22
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)
e=bool(0)
print(e)
'''

#float type casting-->int,complex,bool
'''
price=445.1
print(type(price))
b=int(price)
print(b)
c=complex(price)
print(c)
print(type(c))
f= bool(price)
print(f)
'''
#complec typecasting --> int, float, bool
'''
data = 2+5j
print(type(data))
#b= int(data)#type error
#print(data)
#c= float(data)
#print(c)
d=bool(data)
print(d)
d=5+4.5
print(d)
'''
'''
e=int(float(bool(45))) #bool(45)=trueso float(true)=1.0,int(1.0)=1,int(true)=1
print(e)

'''

f = 45+2.5 +2 +3j +False
print(f)





