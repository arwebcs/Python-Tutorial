# Type of Errors
# 1. Logical
# 2. Name
# 3. Type
# 4. Value
# 5. Index
# 6. Key
# 7. Module
# 8. Import
#---------------------------------------------------------

# Syntax Error
# a =10
# b=20
# if a==b
#     print("Yes")
# else
#     print("No")

# N.B.: Syntax error cannot be handled

# -----------------------------------


# Error handling (Logical Error)
try:
  print(1/0)
except Exception:
  print("Cannot be divisible by 0")