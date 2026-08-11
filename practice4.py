'''
user=input('enter the text:')
methods=["upper","lower","title","capitalize","swapcase"]
for method in methods:
    if method=="upper":
        print('Upper:',user.upper())
    elif method=="lower":
        print('lower:',user.lower())
    elif method=="title":
        print('Title:',user.title())
    elif method=="capitalize":
        print('capitalize:',user.capitalize())
    elif method=="swapcase":
        print('Swapcase:',user.swapcase())
if user.isupper():
    print("text is uppercase",True)
else:
    print("text is not uppercase",False)
if user.islower():
    print("text is lowercase",True)
else:
    print("text is not lowercase",False)
if user.istitle():
    print("text is title",True)
else:
    print("text is not title",False)
'''

while True:
    username = input("Enter username: ")

    if username == "quit":
        break

    if username.isalnum():
        print("contains only letters and numbers")
    else:
        print("does not contain only letters and numbers")

    if username[0].isalpha():
        print("begins with a letter")
    else:
        print("does not begin with a letter")

    if username.isidentifier():
        print("valid python identifier")
    else:
        print("not a valid python identifier")

    if username.isascii():
        print("contains only ASCII characters")
    else:
        print("contains non-ASCII characters")





























































