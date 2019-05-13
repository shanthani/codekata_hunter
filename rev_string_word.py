#shanu
n=input()
s=[]
for i in n.split():
    s.append(i[::-1])    
print(*s)
