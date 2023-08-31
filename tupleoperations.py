tpl = []
print(tpl)

tpl = (10,)
print(type(tpl))
print(tpl)

tpl = (12,2,34,'Sham',13.56)
print(tpl)

print(tpl[2])
print(tpl[1:])
print(tpl[:-3])
print(tpl[1:3])


n=len(tpl)
print("length of the tpl=",n)

print(tpl*3)

tpl1 = (1,2,3)
tpl2= (11,22,33)
print(tpl1+tpl2)

tpl = (12,13,15,45,85,96,45,78,15,45)
print("The minimum element in the tuple=",min(tpl))
print("The maximum element in the tuple=",max(tpl))

search = 45
n = tpl.count(search)
print("no of time the element %d present in the tuple=%d" %(search,n))

n = tpl.index(96)
print("The index of 96=",n)

print("The sorted element in tuple tpl=",sorted(tpl))
print("The sorted element in tuple tpl=",sorted(tpl,reverse=True))

tpl = (1,2,3,4,(11,22,33))
print(tpl[4])