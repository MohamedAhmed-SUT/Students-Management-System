import utils
import os

def grades():
    os.system('cls')
    print('''🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽\n_______________________________________\n''')
    while True:

        print("1. Supply grade")
        print("2. Print student result (HTML)")
        print("3. Bar chart for student results")
        print("4. Pie chart for course registration")
        print("5. Back")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            utils.supply_grade()
        elif choice == "2":
            utils.print_student_result_html()
        elif choice == "3":
            utils.bar_chart_student_results()
        elif choice == "4":
            utils.pie_chart_course_registration()
        elif choice == "5":
            os.system('cls')
            break
        else:
            print("Invalid choice. Try again.")