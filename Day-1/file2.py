import re
"""passwd=input("Enter the passwd:")
while passwd:
    if len(passwd)<6:
        print("invalid passwd")
        break
    elif len(passwd)>16:
        print("invalid passwd")
        break
    elif not re.search("[a-z]",passwd):
        print("invalid passwd")
        break
    elif not re.search("[A-Z]",passwd):
        print("invalid passwd")
        break
    elif not re.search("[0-9]",passwd):
        print("invalid passwd")
        break
    elif not re.search("[$#@]",passwd):
        print("invalid passwd")
        break
    else:
        print("valid passwd")
        break
"""
passwd="1234abcd"
result=re.search("1bcd",passwd)
print(result)
