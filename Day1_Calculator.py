#Simple Calculator just 4 operator 

def Add(x,y):
    return x+y
def Subtract(x,y):
    return x-y

def Multiply(x,y):
    return x*y

def Divide(x,y):
    return x/y



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice=input ("Select operations(1/2/3/4):")
m= int(input("Enter first number"))
n=int(input("Enter second number"))



if choice=='1':
    print(Add(m,n))
elif choice=='2':
    print(Subtract(m,n))
elif choice=='3':
    print(Multiply(m,n))
elif choice=='4':
    print(Divide(m,n))
else:
    print("invalid")
