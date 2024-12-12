password=input("Enter the password: ")
uppercase=False
lowercase=False
number=False
is_specchar=False
specchar="#$@"
for char in password:
    if len(password)<6 or len(password)>16:
        break
    elif char>='A' and char<='Z':
        uppercase=True
    elif char>='a' and char<='z':
        lowercase=True
    elif char>='0' and char<='9':
        number=True
    elif char in specchar:
        is_specchar=True
if uppercase and lowercase and number and is_specchar:
    print("valid passwd")
else:
    print("invalid passwd")