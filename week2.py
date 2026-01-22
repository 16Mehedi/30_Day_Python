students = [
    {"name": "Mehedi", "Age": 23, "marks": [67, 77, 97]},
    {"name": "Farsi", "Age": 24, "marks": [65, 87, 95]},
    {"name": "Naeem", "Age": 25, "marks": [87, 93, 87]}
]

def total_marks(marks):
    return sum(marks)

def Average_marks(marks):
    return sum(marks)/len(marks)

# Show initial students
for stu in students:
    print("Name:", stu["name"])
    print("Age:", stu["Age"])
    print("Total marks:", total_marks(stu["marks"]))
    print("Average Marks:", Average_marks(stu["marks"]))
    print("---------------------")

# Find top student
top_student = None
highest_avg = 0

for stu in students:
    avg = Average_marks(stu["marks"])
    if avg > highest_avg:
        highest_avg = avg
        top_student = stu["name"]

print("Top Scorrer:", top_student)
print("Highest Average:", highest_avg)
print("\n----- Student Manager -----\n")

def add_student():
    name = input("Enter student name: ")
    Age = input("Enter student age: ")
    marks = input("Enter marks separated by space: ")

    marks = [int(m) for m in marks.split()]

    student = {"name": name, "Age": Age, "marks": marks}
    students.append(student)

    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return

    for stu in students:
        print("Name:", stu["name"])
        print("Age:", stu["Age"])
        print("Marks:", stu["marks"])
        print("----------------")

def update_student():
    name = input("Enter name to update: ")

    for stu in students:
        if stu["name"].lower() == name.lower():
            new_marks = input("Enter new marks separated by space: ")
            stu["marks"] = [int(m) for m in new_marks.split()]
            print("Marks updated!\n")
            return

    print("Student not found.\n")

def delete_student():
    name = input("Enter name to delete: ")

    for stu in students:
        if stu["name"].lower() == name.lower():
            students.remove(stu)
            print("Student removed.\n")
            return

    print("Student not found.\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
