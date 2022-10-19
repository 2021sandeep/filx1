l=[1,2,3,4,5]
new_list=[]
for i in range(0,len(l)):
    new_list.append(l[i]*5)
print(new_list)
######################
l=[1,2,3,4,5]
new_list=[x*5 for x in l]
print(new_list)
##########################

even_list=[x for x in range(20) if x%2==0]
odd_list=[x for x in range(20) if x%2==1]
print(even_list)
print(odd_list)
