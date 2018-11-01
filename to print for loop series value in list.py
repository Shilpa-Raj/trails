data=input('enter the number of figures ')

a=int(data)

x=0

y=1

z=0

l=[]

temp=l.append(x)

temp=l.append(y)


for i in range(a):

    z=x+y

    
x=y

    y=z

    temp=l.append(z)

print(l)