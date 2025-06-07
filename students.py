import os
import utils
from datetime import datetime
def Students():
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
    while True:
            print("1. List students")
            print("2. Add student")
            print("3. Edit student")
            print("4. Remove student")
            print("5. Back")
            choice = input("Enter your choice: ").strip()
            
            if choice == "1":
                utils.list_students()
            elif choice == "2":
                code = input("Enter student code: ").strip()
                if not code.isdigit():
                    print("Invalid input. Please enter a valid student code.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                    
                name = input("Enter student name: ").strip()
                if not name.isalpha():
                    print("Invalid input. Please enter a valid student name.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                try:
                    birthdate = input("Enter student birth date (YYYY-MM-DD): ").strip()
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    print("Invalid input. Please enter a valid birth date.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                utils.add_student(code, name, birthdate)
                print(f"Student {name} with code {code} added successfully.\n")

            elif choice == "3":
                code = input("Enter student code: ").strip()
                if not code.isdigit():
                    print("Invalid input. Please enter a valid student code.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                    
                name = input("Enter student new name: ").strip()
                if not name.isalpha():
                    print("Invalid input. Please enter a valid student name.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                try:
                    birthdate = input("Enter student new birth date (YYYY-MM-DD): ").strip()
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    print("Invalid input. Please enter a valid birth date.")
                    input("Press Enter to continue...")
                    os.system("cls")
                    break
                utils.edit_student(code, name, birthdate)
            elif choice == "4":
               utils.remove_student()
            elif choice == "5":
                os.system("cls") 
                break
            else:
                print("Invalid choice. Please try again.\n---------------------------------")
                input("Press Enter to continue...")
                Students()