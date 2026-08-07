'''
total=0
for i in range(4):
    price=list(map(int,input("Enter the price:").split(",")))
    total = total + sum(price)
print("sum:",total)
'''
'''
price=list(map(int,input("Enter the price:").split(",")))
total=0
for i in price:
    total +=i
print("sum:",total)
'''
#write a code to print number of uppercase, lowercase,specialcharacter,and digits
'''
password=input("Enter password:")
upper=0
lower=0
special=0
digit=0
for char in password:
    if 'A' <= char <='Z':
        upper =upper+1
    elif 'a' <=char <='z':
        lower =lower+1
    elif '0' <= char <='9':
        digit =digit+1
    else:
        special =special+1
print("upper:",upper)
print("lower:",lower)
print("digit:",digit)
print("special:",special)
'''
'''
email=input("Enter mail:").split()
for mail in email:
    print(mail.split("@")[1])
'''
#fibinoci series
'''
number=int(input("Enter the number:"))
a=0
b=1
for i in range(number):
    print(a,end=',')
    c=a+b
    a=b
    b=c
'''

number=int(input("Enter the number:"))
a=0
b=1
i=0
while i < number:
    print(a,end=',')
    c=a+b
    a=b
    b=c
    i=i+1


























