import pickle

exp = [10,20,30,40,50]
file = open("test.txt","wb")
pickle.dump(exp,file)
file.close()
f=open("test.txt","rb")
l=pickle.load(f)
print(l)