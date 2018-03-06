x = int(input())
y = int(input())
z = int(input())
n = int(input())
i=0
j=0
k=0
b=[]
print('[',end='')
for i in range( x + 1):        
    for j in range( y + 1):
        for j in range( z + 1):
            if ( ( i + j + k ) != n ):
                a=[i,j,k]
                #b=[b,a]
                print(a,',',end='')
 #               print ('[',i,j,k,']',end='')
  #          print(',',sep='')       
print(']')



                    
