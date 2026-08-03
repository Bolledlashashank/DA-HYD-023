'''
control statements --> control of flow execution of the program
                   --> conditional statements --> if, elif, else...
                --> Repetition statements(Loops) --> for, while(for with else)
                                                           (while with else)
                ---> jumping statements --> break,continue,pass
'''

#loops --> loops are helpful for reptition(Automative tasks)
#for keyword will be helpfull to iterate over a sequence / range
#syntax for (for Keyword):
'''
for <temp_var> in sequence/range:
    statement(s)...
    ....
'''
#range(start,stop,step)
#by default range picks 0 as start value
'''
for i in range(10):
    print(i)
'''
#in above case we got 10 iterations
'''
for i in range(0,10):
    print(f'value of i is -->{i}')
'''
'''
for i in range(1,10):
    #if i>5:
      #  print(f'value of i is -->{i}')
      #now i want to gent only even numbers with above condition
     if i>5 and i%2==0:
         print(f'final Value of i is--{i}')
'''
#range(start,stop,step) -->here step-->interval
'''
for i in range(1,20,3):
    print(i,"Done")
'''
# to print in reverse order
'''
for i in range(-10,0,1):#<-- fro -ve values# reverse order for +ve values(10,0,-1)
    print(i)
'''
#[]-->we generally lists
'''
names = ['rakesh','nikhil','aravind']
print(len(names)) #len(obg) --> Return the number of i tems in a container
for name in names:
    if name=="rakesh":
        print(f"student  name is {name}")
'''
    #print(name)
    #print(f'student name is {name}')
#calculate the sum of first 10 numbers
'''
result = 0#target variable
for i in range(11):
    result = result + i
    print(f"now the result is {result}")
print(f"sum of the 10 numbers is {result}")
'''
#sum of first 10 even numbers
#first understand your input -->rabge(11)-->10 numbers
#second understand your output -->sum(number)
#third we need to to map the logic
'''
result = 0
for i in range(21):
    if i %2 == 0:
        result = result + i
        print(f"now the result is {result}")
print(f"sum of first 10 even numbers {result}")
'''
#understand the loops usage with finess streak example
#work_out -->1,work_out_missed -->
work_log = [0,1,1,1,0,1,0]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0#streak breaks
print(f'longest_streak is {longest_streak}')


































                 
