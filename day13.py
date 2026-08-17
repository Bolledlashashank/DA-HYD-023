'''
mapping-->dictionary-->collection of key-value pairs used to store related data -->JSON,APIs,DATABASE records

dict() --> data = {} --> data = {key : value}
dictionary is mutable,indexed through keys,ordered,heterogeneous,keys,must be unique(int,strings,float values...)
'''
details = {}
print(type(details))
details = {'ID':'CGf45','NAME':'shashank',
           'Gender':'m','Age':22,
           'Batch':'DA-23','place':'hyd'}
print(details)
print(len(details))

#Access the data from dictionary
#details[0]#key error
print(details.keys())#it returns keys from the dictionary
print(details['ID'],details['NAME'])
#if key name is not matching / invalid
#print(details['marks'])#key error as marks is not present
details['marks']=[]
print(details)
print(type(details['marks']))


details['marks'].append(45)
print(details)

details['marks'].extend([15,20,25,20,20])
print(details)
'''
#create key value pair for practice session
details['ps']=[]
print(details)

details['ps'].append('Tuesday')
print(details)

details['ps'].extend(['thursday','saturday'])
print(details)

#accessing 3rd day marks of student
print(details['marks'][2])
#accessing 2nd day of practice session
print(details['ps'][1])
details['mi']=('monday','wednesday','friday')
print(details)

print('wednesday' in details)#it returs false because the wednesday is no key value

print('mi' in details)
#it returns true because mi is key value
'''

################################################################################
'''
for i in details.keys():
    print(i)

for i in details.keys():
    print(f'key ={i}')
    print(f'value = {details[i]}')
'''
'''
for i in details.values():#returns value from  dictionary
    print(i)


for i in details.items():#return a key-value pair in tuple
    print(i)

for keys,value in details.items():
    print(f'keys is {keys}')
    print(f'value is {value}')
'''
#update()-->updating the dictionary with key-value pairs
'''
details.update({'marks':[],
                 'ps':('tuesday','thursday','saturday')})
print(details)

marks=list(map(int,input("enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

'''
print(details.keys())
print(details.get('marks'))
print(details.get('branch'))#it returns none as we dont have branch as key
print(details.keys())

details.setdefault(('Branch'))
print(details)
details['Branch']=['CSE']
print(details)


print(details.setdefault('NAME'))
print(details.keys())

print(details.pop('Branch'))
print(details.keys())

del details['ID']
print(details.keys())

details.clear()
print(details)

#form keys()--> creates a dictionary from iterable (lists,tuples,sets,strings
data = ['shashank','reddy','data']
b=dict.formkeys














