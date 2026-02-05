#printing pattern

n = 5

for i in range(n):
    #space print
    for st in range(2*i+1):
        print("*", end="")
    for s in range(n-i-1):
        print(" ", end="")
   
    print()

