import random as r
arr= ["apple","orange","banana"]
print(r.randint(5,10))
print(r.randrange(5,10))
print(r.choice(arr))
print(r.random()) # 0<x<1
r.shuffle(arr)
print(arr)
u=r.uniform(3,9)
print(u)
