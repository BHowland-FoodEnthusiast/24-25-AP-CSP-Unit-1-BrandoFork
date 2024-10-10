def menu():
    print("Welcome to my grading system.")
    print("Press 1 to view grades")
    print("Press 2 to add grades")
    print("Press 3 to remove grades")
    print("Press 4 to convert to letter grades")
    print("Press 5 to exit the program")

status = True
grades = [67, 95, 88, 42, 99, 77]

def show_grades():
    for grade in grades:
        print(grade)

def new_grade():
    added_grade = int(input("Enter your new grade: "))
    grades.append(added_grade)
    print("You added the grade " + str(added_grade) + " to your list")

def remove_grade():
    print("The following are your grades.  If you wish to simply delete the last one, enter -1")
    show_grades()
    delete_grade = int(input("Which index would you like to delete?"))
    if delete_grade == -1:
        print("You deleted the grade: " + str(grades.pop()))
    else:
        print("You deleted the grade: " + str(grades.pop(delete_grade)))

def letter_grade():
    for i in range(len(grades)):
        if grades[i] >= 89:
            print("A")
        elif grades[i] >= 79:
            print("B")
        elif grades[i] >= 69:
            print("C")
        elif grades[i] >= 65:
            print("D")
        else:
            print("F")


while status:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_grades()
    elif choice == 2:
        new_grade()
    elif choice == 3:
        remove_grade()


    elif choice == 4:
        letter_grade()
    elif choice == 5:
        print("Thank you for using our program.  Have a great day!")
        status = False
    else:
        print("Please read the menu carefully and select a valid option.")