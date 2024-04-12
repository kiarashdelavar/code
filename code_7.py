class clas():
    def __init__(self,listsen,listghad,listvazn):
        self.listsen = listsen
        self.listghad = listghad
        self.listvazn = listvazn
    def avreage_sen(self):
        tempsen=0
        for sen in self.listsen:
            tempsen+= sen
        self.avreage_sen=tempsen/len(self.listsen)
        return self.avreage_sen
    def avreage_ghad(self):
        tempghad=0
        for ghad in self.listghad:
            tempghad+= ghad
        self.avreage_ghad=tempghad/len(self.listghad)
        return self.avreage_ghad
    def avreage_vazn(self):
        tempvazn=0
        for vazn in self.listvazn:
            tempvazn+= vazn
        self.avreage_vazn=tempvazn/len(self.listvazn) 
        return self.avreage_vazn   
sen_a=[]
ghad_a=[]
vazn_a=[]
t_a=[]
z_a=[]
count_a=int(input()) 
for i in range (0,3):
    t_a.append(input())
for i in t_a:
    z_a.append(i.split(' '))
for i in z_a[0]:
    sen_a.append(int(i))
for i in z_a[1]:
    ghad_a.append(int(i))
for i in z_a[2]:
    vazn_a.append(int(i))
sen_b=[]
ghad_b=[]
vazn_b=[]
t_b=[]
z_b=[]
count_b=int(input()) 
for i in range (0,3):
    t_b.append(input())
for i in t_b:
    z_b.append(i.split(' '))
for i in z_b[0]:
    sen_b.append(int(i))
for i in z_b[1]:
    ghad_b.append(int(i))
for i in z_b[2]:
    vazn_b.append(int(i))
a=clas(sen_a,ghad_a,vazn_a) 
print(a.avreage_sen())
print(a.avreage_ghad())
print(a.avreage_vazn())
b=clas(sen_b,ghad_b,vazn_b)
print(b.avreage_sen())
print(b.avreage_ghad())
print(b.avreage_vazn())
if b.avreage_ghad<a.avreage_ghad:
    print('A')
elif a.avreage_ghad<b.avreage_ghad:
    print('B')
else:
    if b.avreage_vazn<a.avreage_vazn:
        print('A')
    elif a.avreage_vazn<b.avreage_vazn:
        print('B')
    else:
        print('Same')

------------

class school:
    def __init__(self,number_of_students):
        self.quantity = number_of_students

    def get_age(self,ages:list):
        for index,i in enumerate(ages):
            ages[index] = int(ages[index])
        return sum(ages)/self.quantity
    
    def get_height(self,heights:list):
        for index,i in enumerate(heights):
            heights[index] = int(heights[index])        
        return sum(heights)/self.quantity
    
    def get_weights(self,weights):
        for index,i in enumerate(weights):
            weights[index] = int(weights[index])        
        return sum(weights)/self.quantity
    
dict1 = dict()
for i in ["A","B"]:
    students = school(float(input()))
    dict1[i] = {
        "age": students.get_age(input().split()),
        "height":students.get_height(input().split()),
        "weight":students.get_weights(input().split())
        }
tmp = []
for i in dict1:
    print(dict1[i]["age"])
    print(dict1[i]["height"])
    print(dict1[i]["weight"])

    tmp.append((i,dict1[i]["weight"]))
if tmp[1][1] == tmp[0][1]:
    print("Same")
else:
    max_tmp = max(tmp[1][1],tmp[0][1])
    if max_tmp in tmp[1]:
        print(tmp[1][0])
    else:
        print(tmp[0][0])
