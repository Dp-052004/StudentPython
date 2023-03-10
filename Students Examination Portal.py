import csv


student_fields=['Student ID','Name','Class Roll Number','Batch Name']
student_database='students.csv'


def display_menu():
    print("---------------------")
    print("Student Examination Portal")
    print("---------------------")
    print("1.Add new student")
    print("2.View students")
    print("3.Update student")
    print("4.Delete student")
    print("5.Calculate Grade")
    print("6.Quit")


def add_student():
    print("------------------------")
    print("Add student information:")
    print("------------------------")
    global student_fields
    global student_database
    student_data = []
    for field in student_fields:
      value=input("Enter "+field+":")
      student_data.append(value)
    with open(student_database,"a",encoding="utf-8")as f:
        writer=csv.writer(f)
        writer.writerows([student_data])
    print("Data saved successfully!!")
    input("Press enter to continue")
        


def view_students():
    global student_fields
    global student_database

    print("-----Student Records:-----")
    print("--------------------------")
    with open(student_database,"r",encoding="utf-8")as f:
        reader=csv.reader(f)
        for x in student_fields:
            print(x, end='\t|')
        print("\n-------------------------")


        for row in reader:
           for item in row:
             print(item,end="\t|")
           print("\n")       
    input("Press enter to continue")



def update_student():
    global student_fields
    global student_database

    print("------Update Student:------")
    print("---------------------------")
    roll=input("Enter student ID to update:")
    index_student=None
    updated_data=[]
    with open(student_database,"r",encoding="utf-8")as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
          if len(row)>0:
             if roll==row[0]:
                index_student=counter
                print("Student found at index ", index_student)
                student_data=[]
                for field in student_fields:
                   value=input("Enter "+ field +":")
                   student_data.append(value)
                updated_data.append(student_data)
             else:
                updated_data.append(row)
             counter+= 1

              
    if index_student is not None:
        with open(student_database,"w",encoding="utf-8")as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
        print("Student ID", roll,"Updated successfully!!")
    else:
        print("Student ID not found in our database")

    input("Press enter to continue")

def delete_student():
    global student_fields
    global student_database

    print("----Delete Student:----")
    print("-----------------------")
    roll=input("Enter student ID to delete:")
    student_found=False
    updated_data=[]
    with open(student_database,"r",encoding="utf-8")as f:
        reader=csv.reader(f)
        counter=0
        for row in reader:
            if len(row)>0:
                if roll!=row[0]:
                   updated_data.append(row)
                   counter+=1
                else:
                    student_found=True
    if student_found is True:
        with open(student_database, "w" ,encoding="utf-8")as f:
            writer=csv.writer(f)
            writer.writerows(updated_data)
        print("Student ID",roll,"deleted successfully!!")
    else:
        print("Student ID not found in our database!!")

    input("Press enter to continue")


def search_student():
    global student_fields
    global student_database
    print("----Search Student:----")
    print("-----------------------")
    roll=input("Enter Student ID to search")
    with open(student_database,"r",encoding="utf-8")as f:
        reader=csv.reader(f)
        for row in reader:
            if len(row)>0:
                if roll==row[0]:
                    print ("Student found with th following details")
                    print("Student ID: ",row[0])
                    print("Name: ",row[1])
                    print("Class Roll Number: ",row[2])
                    print("Batch Name: ",row[3])
                    grade()
                    break
        else:
            print("Student ID not found in our database!!")     
    input("Press enter to continue")
                                              


def grade():
    print("Enter marks out of 100:")
    m1=int(input("Enter marks in 1st subject:"))
    m2=int(input("Enter marks in 2nd subject:"))
    m3=int(input("Enter marks in 3rd subject:"))
    m4=int(input("Enter marks in 4th subject:"))
    m5=int(input("Enter marks in 5th subject:"))
    total=m1+m2+m3+m4+m5
    percent=(total)//5
    if percent>=90:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=A\nStatus: Passed!!")
    elif percent>=80 and percent<90:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=B\nStatus: Passed!!")
    elif percent>=70 and percent<80:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=C\nStatus: Passed!!")
    elif percent>=60 and percent<70:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=D\nStatus: Passed!!")
    elif percent>=50 and percent<60:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=E\nStatus: Passed!!")
    else:
        print("Total marks = ",total, "\nPercentage= ",percent,"\nGrade=F\nStatus: Failed!!")


while True:
    display_menu()
    choice=input("Enter your choice:")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_students()
    elif choice=='3':
        update_student()
    elif choice=='4':
         delete_student()
    elif choice=='5':
        search_student()
    else:
        break
print("------------------------------")
print("Thank you for using our system")
print("------------------------------")
                    
                
                
                

                          
