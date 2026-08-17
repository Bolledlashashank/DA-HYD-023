'''
sequences ---> string,lists,Tuples,set,frozenset
Mapping -> Dictionary
'''

#sets --> set is a unique collection of objects, un ordered, mutable,
#hashing,unindexed,unique,heterogenous
#sets(),{}
#a={} its an empty dictionary
'''
a=set()
print(type(a))
stud_ids = {123,234,345,657}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2])#type error
print(234 in stud_ids)
#print(stud_ids * 2)
#print(stud_ids + stud_ids)#two sets cannot be merged
'''
#data = {12,3,4,5,[12,3,4],'shashank'}
#print(data)#no lists in =side a set (hasing technique) lists are mutable
'''
data = {12,3,4,(12,3,4),'shashank'}
print(data)
print(len(data))
for i in data:
    print(i)
'''

#methods on sets -->add(),update(),remove(),discard(),pop()
'''
names={'shashank','rakesh','nikhil','bablu'}
print(len(names))
'''
#add() will insert an element into the set (it can be anywhere but only unique
'''
names.add('python')
print(names)
names.add('java')
print(names)
#names.add('add','suntract')#takes only one argument
#print(names)
names.add(('add','police'))
print(names)
'''
da_names={'mani','akash','sai','sonu'}
'''
names.update(da_names)
print(names)
print(len(names))
print(da_names)
da_names.update(names)
print(len(names))
print(len(da_names))
'''
#remove(),discard(),pop(),clear()
'''
da_names.remove('sai')
print(da_names)
#da_names.remove('sai')#key error
#discard(),will remove an element if its present else it ignores
da_names.discard('mani')
print(da_names)
'''
#pop()
'''
da_names.pop()
print(da_names)
print(da_names.pop())#removes and returns an arbitary element
print(da_names)
da_names.clear()
print(da_names)
da_names.add('sharma')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)
'''
#copy()#create a shallow copy of set(independent of each other)
'''
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)
'''
da_23={12,23,34,45,23,36}
da_24={34,46,47,23}
'''
#event =  da_23.union(da_24)
event = da_23 | da_24#'|'is for union
print(event)
print(len(event))
#common = da_23.intersection(da_24)#intersection can be on two elemnets
common = da_23 & da_24#'&'is for intersection
print(common)

'''
print(da_23)
print(da_24)
#difference() removes common elements and prints rmng elements from first selection
diff = da_23.difference(da_24)
print(diff)
f = da_23-da_24
print(f)
'''
#symmetric_diference()-->removes common elements and prints all remaining elements from two sets
symm = da_23.symmetric_differencd(da_24)
#print(sym)
h = da_23^da_24
#print(h)

'''

#issubset() --> checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)
print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns False for sets having common elements
print(da_23.isdisjoint(da_24))

















