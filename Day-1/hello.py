"""print("Hello, World!")
if 5>2:
    print ("5")
x=5
#x="Hai"
print(type(x))
a,b,c="Python","is","good"
l="hai"
m=6
print(l,m)
print(a,b,c)"""

x='awsome'
def func():
    global x
    x="abc"
    print(x)
func()
print(x)