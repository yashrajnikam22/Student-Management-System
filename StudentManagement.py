import json

#Student File Loader
def LoadStudentFile():
    try:
        with open("StudentFile.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

#Info saver into file
def SaveInfo(students):
    with open("StudentFile.json","w") as file:
        json.dump(students,file)

class Students:
    def __init__(self,fname,dob,roll_no,std,div):
        self.Full_Name = fname
        self.DOB = dob
        self.Roll_No = roll_no
        self.Standard = std
        self.Division = div
    
    def to_dict(self):
        return self.__dict__


#To Add Students
def AddStudent():

    print("\n ---Add Student--- \n")
    students = LoadStudentFile()

    try:
        fname = str(input("Enter Student Full Name(First Middle Last) : "))
        dob = input("Enter Student Date of Birth(YYYY-MM-DD) : ")
        roll_no = int(input("Enter Student Roll No : "))
        std = input("Enter Student Standard : ")
        div = str(input("Enter Student Division : "))
    except ValueError:
        print("Please Enter valid Roll_No!")
    

    StdInfo = Students(fname,dob,roll_no,std,div)

    students.append(StdInfo.to_dict())
    SaveInfo(students)

#To remove Student
def RemoveStudent():

    print("\n ---Remove Student--- \n")
    students = LoadStudentFile()

    if not students:
        return

    try:
        idx = int(input("Enter Index to remove Student : ")) -1

        if 0 <= idx < len(students):
            students.pop(idx)
            SaveInfo(students)

            print("Student Removed Successfully...")
        else:
            print("Invalid Index!")
    except ValueError:
        print("Please enter a valid number!")

#To search Student
def SearchStudent():

    print("\n ---Search Student--- \n")
    students = LoadStudentFile()

    try:
        roll_no = int(input("Enter student Roll Number : "))
        found = False
        for student in students:
            if(roll_no == student['Roll_No']):
                Std_Found = student
                found = True

                print(print("\nStudent Name : ",Std_Found["Full_Name"],"\nDate Of Birth : ",Std_Found["DOB"],"\nRoll Number : ",Std_Found["Roll_No"],"\nStandard : ",Std_Found["Standard"],"\nDivision : ",Std_Found["Division"]))
        if found == False:
            print("Student Not Found")
    except ValueError:
        print("Please Enter valid Roll number!")

#To Update marks
def UpdateMarks():

    print("\n ---Update Student Marks--- \n")
    students = LoadStudentFile()

    try:
        roll_no = int(input("Enter Student roll number : "))
        try:
            mar = int(input("Enter marks for Marathi : "))
            hin = int(input("Enter marks for Hindi : "))
            eng = int(input("Enter marks for English : "))
            math = int(input("Enter marks for Mathematics : "))
            sci = int(input("Enter marks for Science : "))
            hist = int(input("Enter marks for History : "))
        except ValueError:
            print("Please enter valid marks!")
    except ValueError:
        print("Please enter valid Roll Number!")

    found = False

    for student in students:
        if student["Roll_No"] == roll_no:
            student["Marathi"] = mar
            student["Hindi"] = hin
            student["English"] = eng
            student["Mathematics"] = math
            student["Science"] = sci
            student["History"] = hist

            found = True
            break

    if found:
        SaveInfo(students)
        print("Marks updated successfully!")
    else:
        print("Student not found!")

#To generate Student Report
def GenerateReports():

    print("\n ---Student Report--- \n")
    students = LoadStudentFile()

    try:
        roll_no = int(input("Enter Student Roll number : "))
    except ValueError:
        print("Enter Valid Roll number!")
    
    for student in students:
        if student["Roll_No"] == roll_no:
            print("\nStudent Name : ",student["Full_Name"],"\nDate Of Birth : ",student["DOB"],"\nRoll Number : ",student["Roll_No"],"\nStandard : ",student["Standard"],"\nDivision : ",student["Division"])

            sum = student["Marathi"] + student["Marathi"] + student["Marathi"] +student["Marathi"] + student["Marathi"] + student["Marathi"]
            perc = (sum / 600) * 100

            print("\n ---Marks--- \n")
            print("\nSubjects\t\tMarks")
            print("-"*30)
            print(
                "Marathi : \t\t",student["Marathi"],
                "\nHindi : \t\t",student["Hindi"],
                "\nEnglish : \t\t",student["English"],
                "\nMathematics : \t\t",student["Mathematics"],
                "\nScience : \t\t",student["Science"],
                "\nHistory : \t\t",student["History"]
            )
            print("-"*30)
            print("\nTotal : ",sum,"/600\tPercentage : ",perc)
            if perc >= 35:
                print("Result : PASS")
            else:
                print("Result : FAIL")
    print("\n ===Thank You=== \n")


def AttendanceRecord():
    students = LoadStudentFile()
    present = 0
    absent = 0
    AttClass = int(input("Enter total number of Classed held : "))
    try:
        roll_no = int(input("Enter Roll Number : "))
        for student in students:
            if student["Roll_No"] == roll_no:
                status = input("Enter Status(P / A) : ")
                if status == 'P' or status == 'p':
                    present += 1
                else:
                    absent += 1
            else:
                print("Student Not Found!")
    except ValueError:
        print("Please enter valid Roll Number!")
    AttPerce = (present / AttClass) * 100
    print(f"Attendance Percentage : {AttPerce}")

#main function
def main():

    students = LoadStudentFile()
    
    print("\n ===STUDENT MANAGEMENT SYSTEM=== \n")
    while True:
        print("\n1.Add Student\n2.Remove Student\n3.Search Student\n4.Update Marks\n5.Generate Reports\n6.Attendance Record\n7.Exit")
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Please enter valid choice!")

        if choice == 1:
            AddStudent()
        elif choice == 2:
            RemoveStudent()
        elif choice == 3:
            SearchStudent()
        elif choice == 4:
            UpdateMarks()
        elif choice == 5:
            GenerateReports()
        elif choice == 6:
                AttendanceRecord()
        elif choice == 7:
            return
        else:
            print("Invalid Choice!")

main()
