tasks=[]

while True:
    print("1-show task")
    print("2-add task")
    print("3-delete task")
    print("0-quite program")

    choice=int(input("Enter your desired program number"))

    if choice==1:
        if len(tasks)==0:
            print("Empty task please add task ")
        else:
            for i ,t in enumerate(tasks):
                print(f"{i+1},{tasks}")

    elif choice==2:
        new=input("write your task")
        tasks.append(new)
        print("New task added")

    elif choice==3:
       
        for i, t in enumerate(tasks):
                print(f"{i+1},{tasks}")

        num=int(input("enter which one you wants to delete"))
        tasks.pop(num-1)
        print("task deleted")
        
    
    elif choice==0:
        print("goodbye!")
        break
    else:
        print("invalid input")

            