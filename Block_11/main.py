from entrada import read_options, read_name
from student import create_student, save_student, search_student, delete_student,students
from output import show_menu, show_menu_students, show_students, show_student, show_messages, show_error


def main() -> None:
    run_program = True

    while run_program:
        print(show_menu())
        option = read_options()

        if option == 1:
            try:
                student = create_student()
                save_student(students,student)
                show_messages("User saved successfully")
            except (ValueError, TypeError) as error:
                show_error(error)
        elif option == 2:
            name = read_name()
            try:
                result = search_student(students,name)
                if result:
                    show_messages(f'The student {name} has found.')
                else:
                    show_error(f'The student {name} not found')
            except(ValueError,TypeError) as error:
                show_error(error)
        elif option == 3:
            name = read_name()
            try: 
                result = delete_student(students,name)
                if result:
                    show_messages(f'The student {name} has remove.')
                else:
                    show_error(f'The student {name} not remove')
            except(ValueError,TypeError) as error:
                show_error(error)
        elif option == 4:
            print(show_menu_students())
            options = read_options()
            if options == 1:
                name = read_name()
                student =show_student(students,name)
                if not student:
                    show_error(f'The student named {name} does not exist.')
            elif options == 2:
                show_students(students)
            elif options == 3:
                print("Exiting the option")
            else:
                show_error("This option does not exist.")
        elif option == 5:
            print("exiting the program...")
            run_program = False
        else:
            print("Incorrect option; please try again.")

if __name__ == "__main__":
    main()