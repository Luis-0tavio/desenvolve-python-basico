import random
list=[]
for i in range(0,20,1):
    list+=[random.randint(-100,100)]
print(sorted(list))
print(list)
print(max(list))
print(min(list))