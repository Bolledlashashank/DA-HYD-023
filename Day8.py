#strings -->group of characters, we use single or double or triple quotes
#for the representation of strings..
#strings are immutable, ordered,indexed collection
#Space is also a characters
'''
name='shashank'
print(name)
print(type(name))
print('len:',len(name)) #len--> returns the number of items in contrainer
#index()-->fetch the object(position) starts at 0 and ends at len(obj) - 
#we use [] representation
print(name[0])
print(name[5])
#print(name[25])#indexError --> as its out of range
#negative indexing --> -1 to len(obj)
print(name[-1])
print(name[-2])
#slicing -->we can acess group of characters(objects)
print(name[:5])
print(name[2:5])
print(name[4:])
'''
'''
name='Python'

print(name[3:7])
print(name[7:3])#returns empty as strings are immutable
#slicing is applicable from lower to heigher index
print(name[:45])#return till end of the string
print(name[45:])

print(name[-1:-5])#return empty string
print(name[-5:-1])
#print 'on' from above string
print(name[4:])
print(name[4:6])
print(name[-2:])
#observe +ve+ve , -ve -ve, +ve-ve, all possibilities
'''
#striding -->[start:end:step]
'''
course = 'DataAnalysis'
print(course[::1])
print(course[::2])
#tnys
print(course[2::3])

print(course[::-1])
print(course[::-2])
'''

'''
name='codegnan'
#name[3] = 'w' #strings are immutable
#operations on strings --> Indexing,concatetaipn,Repetition,Membership
print(name * 3)
print('*' * 25)

data = 'shashank' + 'python' +''+'database'
print(data)
print('123'*4)#numeric string
print('code' in 'codegnan')
for i in 'codegnan':
    print(i,':')
#in above case we get every characters line by line
for i in 'codegnan':
    print(i,end='')
'''
#built-in functuons --> len(),min(),max()
'''
name = 'shashanReddy'
print(len(name))
print(min(name))
print(ord('A'))
print(ord('a'))
print(max(name))
print(sorted(name))

'''
#Methods on strings--> case-sonversations,findng/searching...
name = 'Shashank Reddy'
#Case-conversions --> upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#
c=name.capitalize()
print(c)
d=name.title()
print(d)







































































































































































































