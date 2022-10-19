
# write()
file=open('demo.txt','w')
name=input("enter a name")
file.write('hello welocome{} to the world '.format(name))

# writeline()

file=open('demo.txt','w')
filename=['sandeep','sneha','shravani','vijay']
file.writelines(filename)

# read()
file=open('demo.txt','r')
print(file.read())

#append()
file=open('demo.txt','a')
file.write('its mee ')

#close()

file=open('demo.txt','a')
file.write('\nmy classmate')
file.close()


with open('demo.txt','w') as file:
    file.write('thank you so much')



