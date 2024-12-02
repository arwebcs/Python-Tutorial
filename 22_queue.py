# Queue -> First In First Out (FIFO)

l=[]
while True:
    c=int(input('''
       1. Push
       2. Pop First Element
       3. Front Element
       4. Last Element
       5. Display Element
       6. Exit
       
       Please choose an option : 
    '''))
    if c==1:
        n = input("Enter the value : ")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[0])
    elif c == 4:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l[-1])
    elif c == 5:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print(l)
    elif c == 6:
        break
    else:
        print("Invalid")