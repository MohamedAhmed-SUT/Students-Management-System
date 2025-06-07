import utils
import os

def Courses():
    os.system('cls')
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
    while True:
        print("1. List courses")
        print("2. Add course")
        print("3. Edit course")
        print("4. Remove course")
        print("5. Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            utils.list_courses()
        elif choice == "2":
            code = input("Enter course code: ").strip().upper()
            name = input("Enter course name: ").strip()
            if not name.isalpha():
                print("Invalid input. Please enter a valid course name.")
                input("Press Enter to continue...")
                os.system("cls")
                break
            max_grade = input("Enter max grade: ").strip()
            if not max_grade.isdigit():
                print("Invalid input. Please enter a valid max grade.")
                input("Press Enter to continue...")
                os.system("cls")
                break
            utils.add_course(code, name, max_grade)
        elif choice == "3":
            code = input("Enter course code to edit: ").strip().upper()
            if not code.isalnum():
                print("Invalid input. Please enter a valid course code.")
                input("Press Enter to continue...")
                os.system("cls")
                break
            name = input("Enter new course name: ").strip()
            if not name.isalpha():
                print("Invalid input. Please enter a valid course name.")
                input("Press Enter to continue...")
                os.system("cls")
                break
            max_grade = input("Enter new max grade: ").strip()
            if not max_grade.isdigit():
                print("Invalid input. Please enter a valid max grade.")
                input("Press Enter to continue...")
                os.system("cls")
                break
            utils.edit_course(code, name, max_grade)
        elif choice == "4":
            utils.remove_course()
        elif choice == "5":
            os.system("cls") 
            break
        else:
            print("Invalid choice. Please try again.\n---------------------------------")
            input("Press Enter to continue...")
            Courses()