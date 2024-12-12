import re
ip = input("Enter the string:")
num_count=0
letter_count=0
for c in ip:
    if c==re.search("[A-Z]",ip) or c==re.search("[a-z]",ip):
        letter_count+=1
    elif c==re.search("[0-9]",ip):
        num_count+=1
print(num_count,letter_count)
