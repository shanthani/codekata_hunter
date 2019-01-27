#shanu
n=int(input())
lis=list(map(int,input().split()))
a=[]
d={ }
for i in lis:
     s=lis.count(i)
     d.update({i:s})
     a.append(s)
w=max(a)
if w>1:
    c=0
    for x,y in d.items():
        if c==0:
            if y>1:
                print(x,end="")
                c+=1
        else:
            if y>1:
                print("",x,end="")
else:
    print("unqiue")
