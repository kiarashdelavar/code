n=int(input())
k=[]
t=[]
m=[]
z=[]
x=dict()
for i in range(0,n):
    t.append(input())
for i in range(0,n):
    t[i]=t[i].split(' ')
    for j in range(0,2):
        m.append(t[i][j])
for i in range(0,n):
    z.append(m.pop(i))
for i in z:
    x[i]=m.pop(0)
string=input()
u=string.split(' ')
for i in u:
    k.append(x.get(i,i))
b=len(k)
f=k[0]
for i in range(1,b):
    f=f+' '+k[i]
print(f)