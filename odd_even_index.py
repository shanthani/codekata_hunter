#shanu
n=int(input())
m=list(map(int,input().split()))
c=0
for i in range(n):
        if i%2==0 and m[i]%2==1:
            a=m[i]
        elif i%2==1 and m[i]%2==0:          
            b=m[i]
