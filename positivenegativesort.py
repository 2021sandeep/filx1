list_1=input().split()
list_a=[]
list_p=[]
for i in list_1:
    list_a.append(int(i))
for i in list_a:
    if i>0:
        list_p.append(i)
list_p.sort()
count=0
for i in range(len(list_a)):
    if (list_a[i]>0):
        pass
    else:
        list_a[i]=list_p[count]
        count+=1
print(list_a)

