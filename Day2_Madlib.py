#Second day minni project its a madlib like i input some ingridient of a sentence it will make the story for me
loop=1
#loop back to the point once finished
while loop<5:
    #question the user will face
    noun=input("write your name").strip().upper()
    adjective=input("write a adjective of your character").strip().upper()
    verb=input("write what you do").strip().upper()
    place=input("write your Country name").strip().upper()


    #the full story of mine

    story=f"My name is {noun}.I am an {adjective} man.I {verb} in {place}."

    print(story)

    #loop to continue the process
    loop=loop+1


  


