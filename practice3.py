#write a python progarm to calculate inings of a bats man and count the boundeires,dotballs,total score
#[4,6,1,0,2,4,0,6]
'''
Runs=list(map(int,input("enter the runs:").split(",")))
total_score=0
boundries=0
dot_ball=0
for i in Runs:
    total_score +=i
    if i==4 or i==6:
        boundries +=1
    elif i==0:
        dot_ball +=1
print("total_score:",total_score)
print("Boundries:",boundries)
print("Dot_Balls:",dot_ball)
'''
password = "8247"
Max_attempts = 3
current_attempts = 0
while current_attempts < Max_attempts:
    enter_pass=input("enter the password:")
    if enter_pass == password:
        print("Phone unlocked")
        current_attempts=3
    else:
        print("Entered incorect password...")
        current_attempts +=1
        print("Remaining attemps:",Max_attempts-current_attempts)
        print("Please try angain in 25 seconds......")
        


        
    






































