import json
blog = {
    "course":"Python",
    "fees":15000
}

f= json.dumps(blog)
print(type(f), f)

print()

jsonParse = json.loads(f) # parsing json string to object
print(type(jsonParse), jsonParse)
print(jsonParse['fees'])

file =open("dummy.json", "r")
x = file.read()
finalData = json.loads(x)

for a in finalData:
 print(a['id'], a['title'])