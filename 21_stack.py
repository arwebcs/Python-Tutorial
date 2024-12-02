# Stack -> Last In First Out (LIFO)

l=[]
while True:
    c=int(input('''
       1. Push
       2. Pop Last Element
       3. Peek Last Element
       4. Display
       5. Exit
       
       PLease choose an option
    '''))
    if c==1:
        n = input("Enter the value : ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[-1])
    elif c == 4:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l)
    elif c == 5:
        break
    else:
        print("Invalid")