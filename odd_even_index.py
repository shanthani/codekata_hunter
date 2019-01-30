#shanu
n=int(input())
m=list(map(int,input().split()))
c=0
a=[]
for i in range(n):
        if i%2==0 and m[i]%2==1:
            a.append(m[i])
        elif i%2==1 and m[i]%2==0:          
            a.append(m[i])
for j in a:
    if c==0:
        print(j,end="")
        c+=1
    else:
        print("",j,end="")
