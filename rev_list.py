#shanu
n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    if i==n-1:
        print(l[-1])
        del(l[-1])
    else:
        print(str(l[-1])+'->',end="")
        del(l[-1])
