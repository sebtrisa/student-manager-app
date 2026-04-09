#A list that will store the dictionaries of students
students = []

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
    print("Student added!\n")

#a new function to view all the students
def view_students():
    for student in students:
        print(student)
    print()

#creating the main menu 
def menu():
    while True:
        print('1. Add Student')
        print('2. View Students')
        print('3. Exit')

        choice = input('Choose an option: ')

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            break
        else:
            print('Invalid choice\n')

#running the programm
menu()