ls=[23,4,5,6,76,34,56]

print(ls)
temp=ls[0]
ls[0]=ls[-1]
ls[-1]=temp
print(ls)
