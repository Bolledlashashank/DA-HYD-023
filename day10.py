'''
sequences --> Strings, list,tuples,sets
mapping --> Dictionary
'''

#lists --> collection of heterogenous elements (items)
#lists --> indexed , ordered , mutable, heterogenous,we use [] to store the data
'''
marks=[24,34,55,76]
print(marks)
print(len(marks))
print(type(marks))
print(55 in marks)
'''
#operations : Indexing,slicing,striding,membership,merging,repetition

#nested list-->A list inside a list
names = ['codegnan',25,4.6,[56,67,89,95],'DA23',34]
'''
print(len(names))
print(names[0])
print(names[3])
print(names[-3])
print(type(names[0]))
print(names[0][:4])
print(names[0][4:])
print(names[0][::2])
#names[0] = names[0][::-1]
#print(names)
print(names[3])
print(len(names[3]))
print(names[3][2])

#indexing,slicing--->mutable
names[2] ='python'
print(names)
#by indexing we can change the elements, length of collection will remain same
names[4] = ['codegnan','jfs','pfs','DA','aaa']

print(names)
print(len(names))
print(names[4][0])
print(names[4][0][4:])

names[2:4]='abhi','sai','saketh','sairam'
print(names)
#in slicing whatever elements u pass as per
names[3:6:2]='python','java'
print(names)
'''
#create a nested list with strings , lists and work on indexing,slicing,striding
#added advantages if u could add string functions also it
#lists the funtions-->append(),insert(),extend(),pop(),remove(),clear()
#indexing(),count(),copy(),sort(),reverse()
names = ['codegnan','shashank']
#append() -->inserts single elements to the end of the list
names.append('data')
#names.append('analysis','agents')#type errror because we can only enter the single element
names.append(['analysis','agents'])
print(names)
#append()will always increment the length of list by 1
#print(names[3])
#print(names[3].append('chatgpt'))#it returns to none as append is applicable
#on list not print
#print(names[3])
#print(names)

#extend() -->inserts multiple elements to the end of the list
'''
names.extend('analysis')#string will be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([40,45,47,50])
print(names)
'''
#names.extend(35,45)#type error--> as only 1 argument to be passed..
#print(names)
#insert(index.object)-->insert given object before index
'''
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#syntax error
#print(names)
names.insert(-1,'AAA')
print(names)
'''

#pop(),remove(),clear()
#pop() by default last,else givel index
print(names.pop())
print(names)
names.pop(2)
print(names)


#remove() we can remove a specific value
names.extend([23,14,15])
print(names)
names.remove(14)
print(names)
#names.remove(14) #it raises valueerror
del names[1:3]
print(names)
names.clear()
print(names)















