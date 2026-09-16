from student import students

def show_menu():
    return f"""
    --- Options ---
      1. Register user
      2. Search student
      3. Delete student
      4. Show students
      5. Exit
      Chose option: """

def show_student(students) :
    for student in students:
        return f"""
        Name: {student["name"]}
        Age: {student["age"]}
    """

