mark=float(input("write your mark"))

if mark<0 or mark>100:
    print("Invalid input")
elif mark>90:
    print(f"Your grade is C")
elif mark>80:
    print(f"Your grade is B")
elif mark>70:
    print(f"Your grade is A")
elif mark>60:
    print(f"Your grade is Pass")
else:
    print(f"Your grade is F")

