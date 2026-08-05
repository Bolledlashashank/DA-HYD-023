#work_out -->1,work_out_missed -->
'''
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
            print(longest_streak)
            #break
    else:
        current_streak = 0#streak breaks
else:
    print(f'longest_streak is {longest_streak}')
'''

#in this case when entire loop execution is done we get result of
#else block




#for -else with notifications senario
'''
#notifications=[0,0,0,0,0]
notifications=list(map(int,input('Enter the values --> 0 or 1:').split(',')))
print(notifications)
for notification in notifications:
    if notification==1:
        print('unread notification')
        break
else:
    print('all caughtup')
'''

#while -->it relies on condition,it will be completely executed until the condition is satisfied..
#condition is satisfied..
'''
syntax while:
while<condition>:
    statements()>....
    .....
'''
'''
while True:
    print("yes")
'''
#it runs an infinite loops we need to press  ctrl+c
'''
i=10#initialised statement
while i>=1:
    print(i)
    i=i-1
'''
'''
i=0
while i<=10:
    print(10-i)
    i=i+1
'''
#banking senario --> pin authentication if more than 3 attempts
#account locked..
pin = "8247"
max_attempt = 3
current_attempt = 0
while current_attempt < max_attempt:
    entered_pin=input('enter the pin:')
    if entered_pin==pin:
        print("login sucessfull")
        break
    else:
        print("Entered pin is Wrong.. try again")
        current_attempt +=1
        print("Remaining Attempts",max_attempt-current_attempt)
else:
    print("Account is locked .. try after 5 min")

    
    
    
        















