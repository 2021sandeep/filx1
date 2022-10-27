def special_char(word):
    list_special=[]
    list_normal=[]
    count=0
    for i in word:
        if (i=="@" or i=="$" or i=="%" or i=="&"):
            list_special.append(i)
        else:
            list_normal.append(i)
    list_special=list_normal[::-1]
    for i in range(len(word)):
        if word[i] in list_special:
            pass
        else:
            word[i]=list_normal[count]
        count+=1
        if count==len(list_normal):
            break
    return (word)
word=list(input())
print(special_char(word))


