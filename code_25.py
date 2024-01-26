import math
n=int(input())
list=[]
for i in range (0,n):
    list.append(int(input()))
list_sqrt=[]
for i in list:
    list_sqrt.append(math.sqrt(i))
t=[]
m=[]
for i in list_sqrt:
    if i//1==i:
        i=str(i)
        t.append(i+'000')
    else:
        i=str(i)
        m=i.split('.')
        if len(m[1])>4:
            t.append(m[0]+'.'+m[1][:4])
        if len(m[1])<4:
            for x in range(len(m[1]),4):
                m[1]=m[1]+'0'
                t.append(m[0]+'.'+m[1])
for i in t:
    print(i)