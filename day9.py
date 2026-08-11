'''
strings --> caseconversions, searching @ finding, String testing methods, Replace , space removal
'''
'''
a = 'shashank'

print(len(a))
print(max(a))
print(min(a))
b=a.index('a')#it returns only the first occurance
print(b)
c=a.index('a',4) #it returns to the next occurance
print(c)
d=a.index('k')
print(d)
e=a.index('k',6)#value error
print(e)
'''

#rindex() --> returns last occurance
'''
b= a.rindex('n')
print(b)
c=a.rindex('h')
print(c)

'''
'''
#count
print('shashank'.count('a'))
print('shashank'.count('W'))#it returns 0 as we dont have w in shashank
print('reddy'.count('e'))
'''
#find()--> first occurance but it avoid error returns -1 if substring is not found
'''
print('shashank'.find('g'))#it returns -1 
print('reddy'.find('d'))


a="data"
print(len(a))
for i in a:
    print(a.count(i),a.index(i))

'''
#Replacing, spliting, joining
#strings are immutable
'''
a='codegnan'
print(a.replace('g','s'))
print(a)
a=a.replace('g','s')
print(a)
b='$JBSJBQDE$JGVCJG$S$D$CQ$DS$$'
print(b.replace('$',''))
'''
'''
a= 'shashank reddy'
print(len(a))
b=a.split()
print(b)
print(len(b))
c= 'code gnan jntu'
d=c.split()
print(d)
print(len(d))
'''

#join(iterable)--> concatenate any number of strings
'''
a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print(''.join('shahshank'))
'''

#string testing methods (boolean)
#isalpha(),isalnum(),isdigit(),issupper(),islower()...
'''
a='shashank123'
print(a.isalnum())
b='codegnan'
print(b.isalnum())
print(a.isalpha())
print(a.isdigit())
print('8989898989'.isdigit())
print('2345'.isnumeric()) #this has uppervedge (numbers,fractions,romans)
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
'''

'''
print('codegnan'.islower())
print('Codegnan'.isupper())
print('codegnan python'.istitle()) 
'''

#space removal--> strip() (remove leading and tralling spaces)
'''
a='   codegnan'
print(a.strip())
b=input('enter the string:').strip().upper()
print(b)
'''

#zfill() filling with zeros as per the given numeric string
print ('234'.zfill(4))
print('234'.zfill(7))
#Center(),ljust(),rjust() -->Alignment  of string (check length and then modify the width accordingly)
print('hai'.center(6))
print('hai'.center(7,'-'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))






















