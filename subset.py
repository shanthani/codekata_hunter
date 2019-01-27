#shanu
n,m=map(int,input().split())
a=list(map(str,input().split()))
b=list(map(str,input().split()))
if n>m:
    c=0
    for i in b:
        if i in a:
            c=c+1
    if c==m:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
