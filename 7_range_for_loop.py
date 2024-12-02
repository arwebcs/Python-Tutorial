# Range : range(Start, Condition, Increment/Decrement)

# ---------------------------------------------------------

# range(5) # Start -> '0' (By default), Condition -> '<5', Increment(By default) -> '+1' (By default)

for n in range(5):
    print(n)

print("------------------------")

range(1,5) # Start -> '1', Condition -> '<5', Increment(By default) -> '+1' (By default)

for n in range(1,5):
    print(n)

print("------------------------")

range(1,5,2) # Start -> '1', Condition -> '<5', Increment -> '+2'

for n in range(1,5,2):
    print(n)


print("------------------------")

# Reverse loop

print("Reverse loop")

range(10,5,-1) # Start -> '10', Condition -> '>5', Decrement -> '-1'

for n in range(10,5,-1):
    print(n)


