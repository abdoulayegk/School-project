
# School management system
"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
faculty-Fields :- ['roll', 'name', 'age', 'email', 'phone']
6. Add New Student
7. View Students
8. Search Student
9. Update Student
10. Delete Student
11. Quit
"""
 
import csv
# Define global variables
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'
faculty_database = 'faculty.csv'
faculty_fields = ['roll', 'name','age','departement','email','phone','salary']
 
 
def display_menu():
    print("=================================================================================================")
    print(" Welcome to School Management System")
    print("=================================================================================================")
    print("1.  Add New Student")
    print("2.  View Students")
    print("3.  Search Student")
    print("4.  Update Student")
    print("5.  Delete Student")
    print("6.  Add faculty Member")
    print("7.  View Faculty Member")
    print('8.  Search Faculty Memeber')
    print('9.  Update Faculty Member')
    print('10. Delete Faculty Member')
    print('11. Quit')

# this function is for student
 
def add_student():
    print("==================================================================================================")
    print("Add Student Information")
    print("==================================================================================================")
    global student_fields
    global student_database
 
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
 
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
 
    print("Data saved successfully")
    input("Press any key to continue")
    return
# this function is for faculty member.
def add_faculty():
    print('==================================================================================================')
    print('Add Faculty Member Information ')
    print('===================================================================================================')
    global faculty_database
    global faculty_fields
    faculty_data = []
    for field in faculty_fields:
        value = input("Enter " + field + ": ")
        faculty_data.append(value)
    with open (faculty_database, 'a',encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([faculty_data])
    print('Data saved successfully')
    print('Press 11 any key to continue')
 
 
def view_students():
    global student_fields
    global student_database
 
    print("=========================================== Student Records=======================================")
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n============================================================================================")
 
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
 
    input("Press any key to continue")
    
 # function for faculty
def view_faculty():
    global faculty_fields
    global faculty_database
    print('===================================Faculty records=====================================================')
    with open(faculty_database, 'r', encoding = 'utf-8') as f:
        reader =csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print('\n')
        
        for row in reader:
            for item in row:
                print(item, end='\t |')
            print('\n')
    print('Press any key to continue ')

 
def search_student():
    global student_fields
    global student_database
 
    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("=================================== Student Found =================================")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")
    
# function for faculty

def search_faculty():
    
    print('====================================== Search faculty ==============================================')
    roll=input("Enter the roll number to search: ")
    with open (faculty_database, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)>0:
                if roll == row[0]:
                    print("================================ faculty member found ==============================")
                    print('Roll: ',row[0])
                    print('Name: ',row[1])
                    print('Age: ',row[2])
                    print('Email: ',row[3])
                    print('Phone: ', row[4])
                    print('Salary: ',row[5])
                    break
        else:
            print("roll No not found in our database")
    print(" Press any key to continue ")
        
      # function for student

def update_student():
    global student_fields
    global student_database
 
    print("========================================= Update Student ===========================================")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
 
 
    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")
 
    input("Press any key to continue")
 
    def updatre_faculty():
        
        global faculty_database
        global faculty_fields
        print("========================================= Update_faculty ===========================================")
        roll = input("Enter the roll number to update: ")
        index_faculty=None
        updated_data =[]
        with open(faculty_database, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader :
                if len(row)> 0:
                    if roll == row[0]:
                        index_faculty = count
                        print("Faculty member found at index". index_faculty)
                        faculty_data = []
                        for field in faculty_fields:
                            value = input( 'Enter '+ field + ' : ')
                            faculty_data.append(value)
                        updated_data.append(faculty_data)
                    else:
                        updated_data.append(row)
                    count +=1
        if index_faculty is not None:
            with open(faculty_database, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("Roll number is not found in this database")
        input(" Press any key to continue")
            
 
def delete_student():
    global student_fields
    global student_database
 
    print("========================================= Delete Student ===========================================")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
 
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")
 
    input("Press any key to continue")
 
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        add_faculty()
    elif choice == '7':
        view_faculty()
    elif choice == '8':
        search_faculty()
    elif choice == '9':
        update_faculty()
    else:
        break
 
print("===============================")
print(" Thank you for using our system ")
print('copyright @abodulaye')
print("===============================")

"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. Add New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
faculty-Fields :- ['roll', 'name', 'age', 'email', 'phone']
6. Add New Student
7. View Students
8. Search Student
9. Update Student
10. Delete Student
11. Quit
"""
 
import csv
# Define global variables
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'
faculty_database = 'faculty.csv'
faculty_fields = ['roll', 'name','age','departement','email','phone','salary']
 
 
def display_menu():
    print("=================================================================================================")
    print(" Welcome to School Management System")
    print("=================================================================================================")
    print("1.  Add New Student")
    print("2.  View Students")
    print("3.  Search Student")
    print("4.  Update Student")
    print("5.  Delete Student")
    print("6.  Add faculty Member")
    print("7.  View Faculty Member")
    print('8.  Search Faculty Memeber')
    print('9.  Update Faculty Member')
    print('10. Delete Faculty Member')
    print('11. Quit')

# this function is for student
 
def add_student():
    print("==================================================================================================")
    print("Add Student Information")
    print("==================================================================================================")
    global student_fields
    global student_database
 
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)
 
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
 
    print("Data saved successfully")
    input("Press any key to continue")
    return
# this function is for faculty member.
def add_faculty():
    print('==================================================================================================')
    print('Add Faculty Member Information ')
    print('===================================================================================================')
    global faculty_database
    global faculty_fields
    faculty_data = []
    for field in faculty_fields:
        value = input("Enter " + field + ": ")
        faculty_data.append(value)
    with open (faculty_database, 'a',encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([faculty_data])
    print('Data saved successfully')
    print('Press 11 any key to continue')
 
 
def view_students():
    global student_fields
    global student_database
 
    print("=========================================== Student Records=======================================")
 
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n============================================================================================")
 
        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")
 
    input("Press any key to continue")
    
 # function for faculty
def view_faculty():
    global faculty_fields
    global faculty_database
    print('===================================Faculty records=====================================================')
    with open(faculty_database, 'r', encoding = 'utf-8') as f:
        reader =csv.reader(f)
        for x in faculty_fields:
            print(x, end='\t |')
        print('\n')
        
        for row in reader:
            for item in row:
                print(item, end='\t |')
            print('\n')
    print('Press any key to continue ')

 
def search_student():
    global student_fields
    global student_database
 
    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("=================================== Student Found =================================")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")
    
# function for faculty

def search_faculty():
    
    print('====================================== Search faculty ==============================================')
    roll=input("Enter the roll number to search: ")
    with open (faculty_database, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row)>0:
                if roll == row[0]:
                    print("================================ faculty member found ==============================")
                    print('Roll: ',row[0])
                    print('Name: ',row[1])
                    print('Age: ',row[2])
                    print('Email: ',row[3])
                    print('Phone: ', row[4])
                    print('Salary: ',row[5])
                    break
        else:
            print("roll No not found in our database")
    print(" Press any key to continue ")
        
      # function for student

def update_student():
    global student_fields
    global student_database
 
    print("========================================= Update Student ===========================================")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1
 
 
    # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")
 
    input("Press any key to continue")
 
    def updatre_faculty():
        
        global faculty_database
        global faculty_fields
        print("========================================= Update_faculty ===========================================")
        roll = input("Enter the roll number to update: ")
        index_faculty=None
        updated_data =[]
        with open(faculty_database, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader :
                if len(row)> 0:
                    if roll == row[0]:
                        index_faculty = count
                        print("Faculty member found at index". index_faculty)
                        faculty_data = []
                        for field in faculty_fields:
                            value = input( 'Enter '+ field + ' : ')
                            faculty_data.append(value)
                        updated_data.append(faculty_data)
                    else:
                        updated_data.append(row)
                    count +=1
        if index_faculty is not None:
            with open(faculty_database, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("Roll number is not found in this database")
        input(" Press any key to continue")
            
 
def delete_student():
    global student_fields
    global student_database
 
    print("========================================= Delete Student ===========================================")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True
 
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")
 
    input("Press any key to continue")
 
while True:
    display_menu()
 
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        add_faculty()
    elif choice == '7':
        view_faculty()
    elif choice == '8':
        search_faculty()
    elif choice == '9':
        update_faculty()
    else:
        break
 
print("===============================")
print(" Thank you for using our system ")
print('copyright @abodulayegk')
print("===============================")
print('Follow me on twitter: https://twitter.com/abdoulayegk')

