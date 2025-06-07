import json
import os
import csv
import matplotlib.pyplot as plt
from datetime import datetime

STUDENTS_FILE = "students.json"
COURSES_FILE = "courses.json"
GRADES_FILE = "grades.csv"

def _read_json(filename):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except:
            return {}

def _write_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4) 

############################################################################################################

def list_students():
    os.system("cls")
    students = _read_json(STUDENTS_FILE)
    if not students:
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        print("No students found.\n")
    else:
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        for code, info in students.items():
            print(f"Code: {code}, Name: {info['name']}, Birthdate: {info['birthdate']}\n")

def add_student(code, name, birthdate):
    os.system("cls")
    students = _read_json(STUDENTS_FILE)
    if code in students:
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        print("Student already exists.\n")
        return
    students[code] = {"name": name, "birthdate": birthdate}
    _write_json(STUDENTS_FILE, students)
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")

def edit_student(code, name, birthdate):
    students = _read_json(STUDENTS_FILE)
    if code not in students:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        print("Student not found.\n")
        return
    students[code] = {"name": name, "birthdate": birthdate}
    _write_json(STUDENTS_FILE, students)
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
    print("Student updated.\n")

def remove_student():
    students = _read_json(STUDENTS_FILE)
    code = input("Enter student code to remove: ").strip()
    if code in students:
        del students[code]
        _write_json(STUDENTS_FILE, students)
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        print("Student removed.\n")
    else:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n𝕤 𝕥 𝕦 𝕕 𝕖 𝕟 𝕥 𝕤  𝕚 𝕟 𝕗 𝕠 𝕣 𝕞 𝕒 𝕥 𝕚 𝕠 𝕟""\n________________________________________\n")
        print("Student not found.\n")

############################################################################################################

def list_courses():
    os.system("cls")
    courses = _read_json(COURSES_FILE)

    if not courses:
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        print("No courses found.\n")
    else:
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        for code, info in courses.items():
            print(f"Code: {code}, Name: {info['name']}, Max Grade: {info['max_grade']}\n")

def add_course(code, name, max_grade):
    courses = _read_json(COURSES_FILE)
    if code in courses:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        print("Course already exists.\n")
        return
    courses[code] = {"name": name, "max_grade": max_grade}
    _write_json(COURSES_FILE, courses)
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
    print("Course added.\n")

def edit_course(code, name, max_grade):
    courses = _read_json(COURSES_FILE)
    if code not in courses:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        print("Course not found.\n")
        return
    courses[code] = {"name": name, "max_grade": max_grade}
    _write_json(COURSES_FILE, courses)
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
    print("Course updated.\n")

def remove_course():
    courses = _read_json(COURSES_FILE)
    code = input("Enter course code to remove: ").strip().upper()
    if code in courses:
        del courses[code]
        _write_json(COURSES_FILE, courses)
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        print("Course removed.\n")
    else:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅲 🅾  🆄 🆁 🆂 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_________________________________________\n")
        print("Course not found.\n")

############################################################################################################

def supply_grade():
    if not os.path.exists(GRADES_FILE):
        with open(GRADES_FILE, "w", newline='') as f:
            pass 
    students = _read_json(STUDENTS_FILE)
    courses = _read_json(COURSES_FILE)
    student_code = input("Enter student code: ").strip()
    course_code = input("Enter course code: ").strip().upper()
    grade = int(input("Enter grade: ").strip())
    max_grade = courses.get(course_code, {}).get('max_grade', None)
    if not (0 <= grade <= int(max_grade)):
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
        print(f"Invalid grade. Please enter a number between 0 and {max_grade}.\n")
        return
    if student_code not in students or course_code not in courses:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
        print("Student or course not found.\n")
        return
    with open(GRADES_FILE, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([student_code, course_code, grade])
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
    print("Grade supplied.\n")

def print_student_result_html():
    students = _read_json(STUDENTS_FILE)
    student_code = input("Enter student code: ").strip()
    if student_code not in students:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
        print("Student not found.\n")
        return
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
    results = []
    with open(GRADES_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == student_code:
                results.append(row)

    student_name = students[student_code]['name']

    html = f"""
    <html>
    <head>
        <title>Results for {student_name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 20px; }}
            h1 {{ color: #333; }}
            table {{
                border-collapse: collapse;
                width: 60%;
                background-color: #fff;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            th, td {{
                border: 1px solid #ccc;
                text-align: center;
                padding: 10px;
            }}
            th {{
                background-color: #f4b41a;
                color: white;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
        </style>
    </head>
    <body>
        <h1>Results for {student_name} (Code: {student_code})</h1>
        <table>
            <tr><th>Course Code</th><th>Grade</th></tr>
    """

    for r in results:
        html += f"<tr><td>{r[1]}</td><td>{r[2]}</td></tr>"

    html += """
        </table>
    </body>
    </html>
    """

    file_name = f"{student_code}.html"
    with open(file_name, "w") as f:
        f.write(html)

    print(f"Results written to {file_name}\n")


def bar_chart_student_results():
    student_code = input("Enter student code: ").strip()
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅱 🆁 🅰  🅲 🅷 🅰  🆁 🆃 🅴  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_____________________________________________________\n")
    courses = []
    grades = []
    with open(GRADES_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == student_code:
                courses.append(row[1])
                grades.append(int(row[2]))
    if not courses:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
        print("No grades found for this student.\n")
        return
    plt.bar(courses, grades)
    plt.title(f"Grades for {student_code}")
    plt.xlabel("Course")
    plt.ylabel("Grade")
    plt.show()

def pie_chart_course_registration():
    course_counts = {}
    os.system("cls")
    print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
    with open(GRADES_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                course = row[1]
                course_counts[course] = course_counts.get(course, 0) + 1
    if not course_counts:
        os.system("cls")
        print("          "'''🅦 🅔 🅛 🅒 🅞 🅜 🅔'''"\n🅶 🆁 🅰  🅳 🅴 🆂  🅸 🅽 🅵 🅾  🆁 🅼 🅰  🆃 🅸 🅾  🅽""\n_______________________________________\n")
        print("No course registrations found.\n")
        return
    plt.pie(course_counts.values(), labels=course_counts.keys(), autopct='%1.1f%%')
    plt.title("Course Registration Distribution\n")
    plt.show()