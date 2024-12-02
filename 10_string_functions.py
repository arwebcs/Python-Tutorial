a = 'Welcome to Python course'
b='123'
c='Price1200'

print("Basic functions")
print("----------------------")
print("Length of a string '", a, "': ",len(a))  # Length of a string
print(a.lower()) # Lower case
print(a.upper()) # Upper case
print(a.capitalize()) # Capitalize first letter of a sentence
print(a.title()) # Capitalize first letter of each word in a sentence

print("-------------------------------------------------")

# Search a letter or a word

print("Search a letter or a word")
print("----------------------")
# str.find('any letter/word') -> Returns 1, if the string is found, else returns -1, if the string is not found
# str.find('any letter/word', start_index) -> Returns 1, if the string is found, else returns -1, if the string is not found. Starting from a specific index
# str.index('any letter/word', start_index) -> Returns 1, if the string is found, else returns -1, if the string is not found. Starting from a specific index

print(a.find('e'))
print(a.find('e',2))
print(a.index('e',3))

print("-------------------------------------------------")

# Preg match of a string

print("Preg match of a string")
print("----------------------")
print(a.isalpha()) # Checks if the string has only letters without white space
print(b.isdigit()) # Checks if the string has only numbers without white space
print(c.isalnum()) # Checks if the string has letters or numbers without white space