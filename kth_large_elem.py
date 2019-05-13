#shanu
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,k):
    s=max(l)
    l.remove(s)
print(s)
   
