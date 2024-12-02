# Type 1.1
import arithmetic_module
print(arithmetic_module.sum(10,20))
print(arithmetic_module.prod(10,20))

# Type 1.2
import arithmetic_module as m
print(m.sum(10,20))
print(m.prod(10,20))

print()

#Type 2.1
from arithmetic_module import sum
print(sum(5,1))

#Type 2.2
from arithmetic_module import *
print(sum(5,1))
print(prod(5,1))
