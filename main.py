#import JSON to be able to store data
import json


#DATA STORAGE FUNCTIONS
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)
def load_students():
    try:
        #Try to open and read the file
        with open("students.json", "r") as file:
            return json.load(file)
    except:
        #if it doesnt exist yet
        return []

students = load_students()

# INPUT FUNCTIONS
#function to get int numbers from input
def get_number_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except:
            print('Please enter a valid number')

#FEATURES FUNCTIONS
def add_student():
    name = input("Enter student name: ")
    age = get_number_input("Enter age: ")
    score = get_number_input("Enter score: ")
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
    if len(students) == 0:
        print("No students available\n")
        return
    
    print('\n--- Student List ---')

    for i, student in enumerate(students, start=1):
        print(f'{i}. Name: {student["name"]}, Age: {student["age"]}, Score: {student["score"]}')
    print()
#a function to update students details
def update_student():
    
    if len(students) == 0:
        print("No students available\n")
        return
    
    view_students()
    
    index = get_number_input("Enter student number to update: ")
    
    if 1 <= index <= len(students):
        student = students[index - 1]
        
        print(f"Updating {student['name']}")
        
        new_name = input("Enter new name (leave blank to keep current): ")
        new_age = input("Enter new age (leave blank to keep current): ")
        new_score = input("Enter new score (leave blank to keep current): ")
        
        if new_name != "":
            student["name"] = new_name
        
        if new_age != "":
            student["age"] = int(new_age)
        
        if new_score != "":
            student["score"] = int(new_score)
        
        print("Student updated!\n")
        save_students(students)
    
    else:
        print("Invalid number\n")
#Delete students
def delete_student():

    if len(students) == 0:
        print('No students to delete\n')
        return
    
    view_students()

    index = get_number_input("Enter student number to delete: ")

    if 1 <= index <= len(students):
        removed = students.pop(index - 1)
        print(f'{removed["name"]} deleted!\n')
        save_students(students)

    else:
        print('Invalid number\n')

#MENU
def menu():
    while True:
        print('\n=== Student Manager ===')
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

#RUNNING THE PROGRAMM
menu()