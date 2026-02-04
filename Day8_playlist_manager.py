#Song Playlist manager
songs=[]

while True:

    print("1-Show song list")
    print("2-Add song")
    print("3-Remove")
    print("0-Exit")

    choice=int(input("I wants to choose the program :"))

    if choice==1:
        if len(songs)==0:
            print("Empty song list. please add your favourite song")

        else:
            for i,s in enumerate(songs):
                print(f"{i+1}.{s}")
    
    elif choice==2:
        new_s=input("Enter your song title :")
        songs.append(new_s)
        print("New song added")
    
    elif choice==3:
        for i,s in enumerate(songs):
                print(f"{i+1}.{songs}")
        num=int(input("Enter the song number you wants to remove"))
        songs.pop(num-1)
        print("Song removed")
    

    elif choice==0:
        print("Good Bye🙌")
        break
    else:
        print("Invalid input")

            


