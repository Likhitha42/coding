n = 5
for i in range(n):
    for j in range(n):
        if(j==0 or i==n-1 or i-j==0):
            print("*",end=" ")
        else:
            print(" ",end= " ")
    print()        
