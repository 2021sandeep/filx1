def invert_list(listt):
    inverted_list=[]
    for i in listt:
        i=int(i)
        i=(-(i))
        inverted_list.append(i)
    return inverted_list
num_list=input().split(" ")
inverted_list=invert_list(num_list)
print(inverted_list)

