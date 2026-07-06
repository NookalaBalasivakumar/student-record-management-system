student={}
def calculate_grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
def add_student():
    roll=input("Enter Roll Number:")
    if roll in student:
        print("Student already exists!")
        return
    name=input("Enter Student Name:")
    marks=[]
    for i in range(3):
        mark=float(input(f"Enter marks of subject:"))
        marks.append(mark)
    total=sum(marks)
    average=total/len(marks)
    grade=calculate_grade(average)
    student[roll]={
        "Name"   :name,
        "Marks"  :marks,
        "Total"  :total,
        "Average":average,
        "Grade"  :grade  
    }
    print("Student record added successfully!")
def search_student():
    roll=input("Enter Roll number to search:")
    if roll in student:
        s=student[roll]
        print("\n Student details")
        print("------------------")
        print("Roll number:",roll)
        print("Name:",s["Name"])
        print("Marks:",s["Marks"])
        print("Total:",s["Total"])
        print("Average:",round(s["Average"],2))
        print("Grade:",s["Grade"])
    else:
        print("Student not found!")
def display_student():
    if not student:
        print("No student records found")
        return
    print("\n All student records")
    print("-"*60)
    for roll,s in student.items():
        print("Roll number:",roll)
        print("Name:",s["Name"])
        print("Marks:",s["Marks"])
        print("Total:",s["Total"])
        print("Average:",round(s["Average"],2))
        print("Grade:",s["Grade"])
        print("-"*60)
#main menu
while True:
    print("\n====STUDENT RECORD MANAGEMENT SYSTEM====")
    print("1.Add student Record")
    print("2.Search Student Details")
    print("3.Display All Student Records")
    print("4.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        search_student()
    elif choice=="3":
        display_student()
    elif choice=="4":
        print("Thank You!")
        break
    else:
        print("Invalid choice! Please try again!")
        
    
        