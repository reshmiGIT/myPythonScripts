import sys
a=int(input())
if 1>= a >= 10**10:
    print ('please enter a number between 1>= var1 >= 10**10')
    sys.exit()
b=int(input())
if 1>= b >= 10**10:
    print ('please enter a number between 1>= var1 >= 10**10')
    sys.exit()
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
print("type is" ,type(a/b))
c=input("enter string:")
c=chr(int(c))
print("data type c",c,type(c))
