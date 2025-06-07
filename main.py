import os
from students import Students
from courses import Courses
from grades import grades
def main():
    os.system("cls") 
    while True:
        try:
            
            print("  "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅼 🅰  🅸 🅽  🅼 🅴 🅽 🆄""\n__________________\n")
            print("1. Students")
            print("2. Courses")
            print("3. Grades")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                Students()
            elif choice == "2":
                Courses()
            elif choice == "3":
                grades()
            elif choice == "4":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.\n---------------------------------")
                input("Press Enter to continue...")
                os.system("cls")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

main()