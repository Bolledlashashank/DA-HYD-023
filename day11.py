'''
list,Tuple
'''
#list --> Mutable,ordered,heterogenous
#index (),count(), copy(),sort(),reverse()
'''
details = ['shashank',7,2026,'hanamkonda']
print(len(details))
print(details.index(7))
print(details.index('shashank'))
details.extend([7,21,45,21])
print(details)
print(details.index(21))
print(details.index(21,6))
#print(details.index('python'))value error
print(details.count(21))
#pritn(detail.count('python'))#it returns to zro because we dont have pyhton in details
'''
#task
'''
0:sodegnan
1:shashank
2:python
3:java

data=['codegnan','shashank','python','java']

for i in data:
    print(data.index(i),':',i)
    
for i in range(len(data)):
    print(i,':',data[i])



#copy()--> shallow copy of the given collection
new = data.copy()
print(new)
print(type(new))
print(len(data))

new[2] = 'agentic ai'
print(new)
print(data)

data.append('shashank')
print(data)
print(new)
'''

'''
data=[1,2,3,[32,45,56],67]
print(data)
new=data.copy()
print(new)
new[3][2] = 'agents'#when ever we make changes in nested list original will also be effected
print(new)
print(data)

new[1] = 'python'
print(new)
print(data)
'''
'''
marks = [14,24,-45,27,35]
print(marks)
#print(marks.sort())#retorns none
#print(marks)#returns in ascending order
#marks.sort(reverse=True)#returns in descending order
#print(marks)
marks.insert(2,'code')
#marks.sort()#sort works when we have same element in the list
print(marks.reverse())
print(marks)
print(marks[::-1])
#type(),len(),max(),min(),print()

print(sorted('codegnan'))#return in ascending order

'''

#opeeratinons --> indexing,slicing,strding,membership,merging,repetition

courses=('pfs','jfs',('Da','Ds'),'AgenticAi',[100,6,6])
'''
print(courses)
print(len(courses))
print(courses[3][-2:])
#courses[2] = 23 Tuples are immutable
courses[-1].append('shashank')
print(courses)

'''
#Tuple iimutable --> count(),index()
print(courses.index('AgenticAi'))
print(courses.count('agents'))
#print(courses.sort())#attributeError-->sort() is in lists not in tuples
print(sorted(courses[-1]))
#print(sorted(courses))
'''
#typecasting
d=tuple(sorted((23,12,3,4,5,)))
print(d)
'''
#eval() function can take any kind of input
print('9+4')
print(eval('9+4'))
a=eval(input("enter a list:"))
print(a)
print(type(a))










