#deseision making

#marks
'''
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
'''

#elif keyword -->if-else-elif
'''
if <condition1>:
   statement(s)..
elif <condition 2>
   statement(s)...
elif <condition 3>
   statement(s)
else:
    statement(s)
    .......
'''

'''
marks = int(input("enter the student marks:"))
if marks >= 100:
    print("entered values should be greater than 1 and less than 100")
elif marks >= 90 and marks <= 100:
    print("user got grade A")
elif marks >= 80 and marks <= 89:
    print("user got grade B")
elif marks >= 70 and marks <= 79:
    print("user got grade C")
elif marks >= 60 and marks <= 69:
    print("user got grade D")
elif marks < 60 and marks >= 0:
    print ("user failed the exam")
else :
    print("-ve values are not valid")
'''

'''
age=int(input("enter the age:"))
if age >=18 and age >=100:
    print('---user has vote eligibility---')
    print("Access Granted")
elif age <18 and age >0:
    print('---user is not eligible to vote---')
    print('---user need to wait for more',(18-age),'years')
else:
    print('only positive vales less than 100 are acceptable')
    
'''

'''
a,b=9,8
print(a)
print(b)
print(a,b)
name="shashank";batch="data Analytics"
print(name,batch)
print(name,batch,sep='')
print(name,batch,sep='---->')
#end = '\n',\t-->tabspace
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")

'''
'''
name='shashank';age=22;batch='DA-023';place='hyd'
'''
#git status
#git add "filename" (to push only one selected file to github)(elif usage print)
#git commit -m "elif usage print" "file name"

#if we ge conflicts git pus --force origin main



#output --> print() --> we can pass any pass any value also use sep and end 
#output formatting --> old style formatting (using commas)
# % usage (%f , %d), .format() usage, fstring notation
'''
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "codegnan"; course= "data analysis"
print(name,course,sep=",")
'''
#end = '\n' , \t --> TAB SPACE
'''
print(name,course,end="\t")
print(a,b, end=" ")
print ("hyderabad")
'''
#USING COMMAS
'''
name = "codegnan"; age=12; batch="DA-023"; place="hyderabad"
print(name,"is in", place, batch,"is running batch",)
'''
#OLD STYLE FORMATTING --> %d--> integer, %s--> string, %f--> float
'''
salary = 24234.1234
print("His salary is %d" %(salary))
print("His salary is %f" %(salary))
print("His salary is %.1f" %(salary))# --> %.1f --> rounded to 1 decimal 
'''
# .format() usage
'''
name = "codegnan"; place="hyderabad"
print("{} is in {}".format(name,place)) # order matters
'''
# fstring usage (MORE RECOMMENDED)
'''
print(f"{name} is in {place}")
print(f"{"saketh"} is in {name}")

'''

'''
num=int(input("Enter the number:"))
if num %2 == 0:
    print("the given number is even")
else:
    print("the given number is odd")
'''
user='shashank'
passid="1234"
username=input("Enter username:")
password=input("enter the password:")
if username==user and password==passid:
    print("login sucessfull")
else:
    print("u entered invalid credintials")

