import sys
number=int(input())
#if number not in range(1,100):
if 1 >= number >= 100:
    print("your number is not between 1 to 100,try again!")
    sys.exit()
if number%2!=0:
    print('Weird')
    sys.exit()
elif number%2==0 and  2 <= number <= 5:
    print('Not Weird')
    sys.exit()
elif  number%2==0 and  6 <= number <= 20:
    print('Weird')
    sys.exit()
elif number%2==0 and  number > 20: 
    print('Not Weird')
else:
     sys.exit()
print('learing git')    
    

