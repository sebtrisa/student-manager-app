#import JSON to be able to store data
import json
#------DATA SAVING------
#Function to save students to file with JSON
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

#Load students from the file 
def load_students():
    try:
        #Try to open and read the file
        with open("students.json", "r") as file:
            return json.load(file)
    except:
        #if it doesnt exist yet
        return []



#------MAIN FUNCTIONS------
#A list that will store the dictionaries of students
students = load_students()
#creating a function to add students to the list
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    score = input("Enter score: ")
    #This dictionary will take the values of the inputs
    student = {
        "name": name,
        "age": age,
        "score": score
    }
    #Appending the student dictionary to the students list, will be done with each student
    students.append(student)
    #save the students to the file 
    save_students(students)
    print("Student added!\n")

#a new function to view all the students
def view_students():
    for student in students:
        print(f'Name: {student["name"]}, Age: {student["age"]}, Score: {student["score"]}')
    print()

#a function to update students details
def update_student():
    name_to_update = input('Enter name of student to update')

    found = False  

    for student in students:
        if student["name"] == name_to_update:
            found = True

            #asking for new data
            new_name = input('Enter new name (leave blank to keep current): ')
            new_age = int(input('Enter new age (leave blank to keep current): '))
            new_score = int(input('Enter new score (leave blank to keep current): '))

            #Update dictionary if user typed something
            if new_name != "":
                student["name"] = new_name
        
            if new_age != "":
                student["age"] = int(new_age)

            if new_score != "":
                student["score"] = int(new_score)

            print('Student updated!\n')
            break
    
    #handling 'not found'
    if not found:
        print('Student not found\n')

    save_students(students)




#------MAIN MENU------
#creating the main menu 
def menu():
    while True:
        print('1. Add Student')
        print('2. View Students')
        print('3. Delete a student')
        print('4. Update a student')
        print('5. Exit')

        choice = input('Choose an option: ')

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            name_to_delete = input('Add the name of the student you wish to delete: ')

            found = False #to track if we found the student

            for student in students:
                if student["name"] ==  name_to_delete:
                    students.remove(student)
                    found = True
                    print('Student deleted\n')
                    break

            if not found:
                print('Student not found\n')
            save_students(students)

        elif choice == "4":
            update_student()
        elif choice == "5":
            break
        else:
            print('Invalid choice\n')


#running the programm
menu()