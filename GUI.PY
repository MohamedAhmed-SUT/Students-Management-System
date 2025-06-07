import customtkinter as ctk
from PIL import Image
import os
import json
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import webbrowser
import re

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

class StudentsManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("🎓 Students Management System")
        self.geometry("1000x700")
        self.minsize(800, 600)
        
        self.STUDENTS_FILE = "students.json"
        self.COURSES_FILE = "courses.json"
        self.GRADES_FILE = "grades.csv"
        
        self.initialize_files()
        self.load_images()
        self.create_widgets()
        
    def load_images(self):
        """Load images for the application"""
        try:
            self.student_img = ctk.CTkImage(Image.open("assets/student.png"), size=(30, 30))
            self.course_img = ctk.CTkImage(Image.open("assets/book.png"), size=(30, 30))
            self.grade_img = ctk.CTkImage(Image.open("assets/grade.png"), size=(30, 30))
            self.logo_img = ctk.CTkImage(Image.open("assets/school.png"), size=(50, 50))
            self.chart_img = ctk.CTkImage(Image.open("assets/chart.png"), size=(30, 30))
        except Exception as e:
            print(f"Error loading images: {str(e)}")
            self.student_img = None
            self.course_img = None
            self.grade_img = None
            self.logo_img = None
    
    def initialize_files(self):
        """Initialize data files if they don't exist"""
        try:
            if not os.path.exists(self.STUDENTS_FILE):
                with open(self.STUDENTS_FILE, "w") as f:
                    json.dump({}, f)
            
            if not os.path.exists(self.COURSES_FILE):
                with open(self.COURSES_FILE, "w") as f:
                    json.dump({}, f)
                    
            if not os.path.exists(self.GRADES_FILE):
                with open(self.GRADES_FILE, "w", newline="") as f:
                    writer = csv.writer(f)
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Failed to initialize files: {str(e)}")
    
    def create_widgets(self):
        """Create the main widgets"""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        
        self.create_header()
        self.create_navigation()
        
        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)
        
        self.show_welcome_screen()
    
    def create_header(self):
        """Create the header with logo and title"""
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        if self.logo_img:
            logo_label = ctk.CTkLabel(header_frame, image=self.logo_img, text="")
            logo_label.grid(row=10, column=0, padx=20, pady=20, sticky="w")
        
        title_label = ctk.CTkLabel(
            header_frame, 
            text="🎓 Students Management System", 
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.grid(row=0, column=1, padx=15, pady=20)
        
        github_btn = ctk.CTkButton(
            header_frame, 
            text="View on GitHub", 
            width=100,
            command=lambda: webbrowser.open("https://github.com/MohamedAhmed-SUT")
        )
        github_btn.grid(row=0, column=2, padx=10, pady=10)
    
    def create_navigation(self):
        """Create navigation buttons"""
        nav_frame = ctk.CTkFrame(self.main_frame)
        nav_frame.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="ew")
        
        self.welcome_btn = ctk.CTkButton(
            nav_frame, 
            text="🏠 Home", 
            command=self.show_welcome_screen
        )
        self.welcome_btn.pack(side="left", padx=5, pady=5)
        
        self.students_btn = ctk.CTkButton(
            nav_frame, 
            text="👥 Students", 
            command=self.show_students_section
        )
        self.students_btn.pack(side="left", padx=5, pady=5)
        
        self.courses_btn = ctk.CTkButton(
            nav_frame, 
            text="📚 Courses", 
            command=self.show_courses_section
        )
        self.courses_btn.pack(side="left", padx=5, pady=5)
        
        self.grades_btn = ctk.CTkButton(
            nav_frame, 
            text="📊 Grades", 
            command=self.show_grades_section
        )
        self.grades_btn.pack(side="left", padx=5, pady=5)
    
    def show_welcome_screen(self):
        """Show the welcome screen"""
        self.clear_content()
        
        welcome_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        welcome_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        welcome_label = ctk.CTkLabel(
            welcome_frame,
            text="🎉 Welcome to Students Management System! 🎉",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        welcome_label.pack(pady=20)
        
        desc_label = ctk.CTkLabel(
            welcome_frame,
            text="""This application helps you manage:
- 👥 Student information
- 📚 Course details
- 📊 Grades and results

Get started by selecting a section from the menu above!""",
            font=ctk.CTkFont(size=16),
            justify="left"
        )
        desc_label.pack(pady=10)
        
        features_frame = ctk.CTkFrame(welcome_frame)
        features_frame.pack(pady=20, fill="x", padx=50)
        
        features = [
            ("👤 Add, edit, and remove students", self.student_img),
            ("📖 Manage course information", self.course_img),
            ("📝 Record and analyze grades", self.grade_img),
            ("📈 Generate charts and reports", self.chart_img)
        ]
        
        for text, img in features:
            feature_frame = ctk.CTkFrame(features_frame, fg_color="transparent")
            feature_frame.pack(fill="x", pady=5)
            
            if img:
                img_label = ctk.CTkLabel(feature_frame, image=img, text="")
                img_label.pack(side="left", padx=10)
            
            text_label = ctk.CTkLabel(feature_frame, text=text, font=ctk.CTkFont(size=14))
            text_label.pack(side="left")
    
    def validate_student_code(self, code):
        """Validate student code format"""
        if not code or len(code.strip()) == 0:
            return False, "Student code cannot be empty"
        code = code.strip()
        if len(code) < 3:
            return False, "Student code must be at least 3 characters long"
        if not re.match("^[A-Za-z0-9_-]+$", code):
            return False, "Student code can only contain letters, numbers, underscores, and hyphens"
        return True, ""
    
    def validate_name(self, name):
        """Validate name format"""
        if not name or len(name.strip()) == 0:
            return False, "Name cannot be empty"
        name = name.strip()
        if len(name) < 2:
            return False, "Name must be at least 2 characters long"
        if not re.match("^[A-Za-z\s]+$", name):
            return False, "Name can only contain letters and spaces"
        return True, ""
    
    def validate_date(self, date_str):
        """Validate date format"""
        if not date_str or len(date_str.strip()) == 0:
            return False, "Date cannot be empty"
        try:
            date_obj = datetime.strptime(date_str.strip(), "%Y-%m-%d")
            if date_obj > datetime.now():
                return False, "Birthdate cannot be in the future"
            if date_obj.year < 1900:
                return False, "Birthdate year must be after 1900"
            return True, ""
        except ValueError:
            return False, "Invalid date format! Use YYYY-MM-DD"
    
    def validate_course_code(self, code):
        """Validate course code format"""
        if not code or len(code.strip()) == 0:
            return False, "Course code cannot be empty"
        code = code.strip().upper()
        if len(code) < 3:
            return False, "Course code must be at least 3 characters long"
        if not re.match("^[A-Za-z0-9_-]+$", code):
            return False, "Course code can only contain letters, numbers, underscores, and hyphens"
        return True, ""
    
    def validate_grade(self, grade, max_grade):
        """Validate grade value"""
        try:
            grade = int(grade)
            max_grade = int(max_grade)
            if not (0 <= grade <= max_grade):
                return False, f"Grade must be between 0 and {max_grade}"
            return True, ""
        except ValueError:
            return False, "Grade must be a valid number"
    
    def load_json_file(self, filename):
        """Safely load JSON file with error handling"""
        try:
            if not os.path.exists(filename):
                return {}
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except json.JSONDecodeError as e:
            messagebox.showerror("File Error", f"Invalid JSON format in {filename}: {str(e)}")
            return {}
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to load {filename}: {str(e)}")
            return {}

    def save_json_file(self, filename, data):
        """Safely save JSON file with error handling"""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save {filename}: {str(e)}")
            return False
    
    def load_csv_file(self, filename):
        """Safely load CSV file with error handling"""
        try:
            results = []
            if os.path.exists(filename):
                with open(filename, "r", newline="", encoding="utf-8") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row:
                            results.append(row)
            return results
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to load {filename}: {str(e)}")
            return []

    def show_students_section(self):
        """Show the students management section"""
        self.clear_content()
        
        self.students_tabview = ctk.CTkTabview(self.content_frame)
        self.students_tabview.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.students_tabview.add("👥 List Students")
        self.students_tabview.add("➕ Add Student")
        self.students_tabview.add("✏️ Edit Student")
        self.students_tabview.add("🗑️ Remove Student")
        
        self.create_list_students_tab()
        self.create_add_student_tab()
        self.create_edit_student_tab()
        self.create_remove_student_tab()
        
        self.load_students_data()
    
    def create_list_students_tab(self):
        """Create the list students tab"""
        tab = self.students_tabview.tab("👥 List Students")
        
        search_frame = ctk.CTkFrame(tab)
        search_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(search_frame, text="🔍 Search:").pack(side="left", padx=5)
        self.student_search_entry = ctk.CTkEntry(search_frame)
        self.student_search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.student_search_entry.bind("<KeyRelease>", lambda e: self.filter_students())
        
        tree_frame = ctk.CTkFrame(tab)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        self.students_tree = ttk.Treeview(
            tree_frame, 
            columns=("code", "name", "birthdate"), 
            show="headings"
        )
        
        self.students_tree.heading("code", text="Student Code")
        self.students_tree.heading("name", text="Name")
        self.students_tree.heading("birthdate", text="Birthdate")
        
        self.students_tree.column("code", width=120)
        self.students_tree.column("name", width=200)
        self.students_tree.column("birthdate", width=120)
        
        v_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.students_tree.yview)
        h_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.students_tree.xview)
        self.students_tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        self.students_tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)
        
        self.students_tree.bind("<Double-1>", self.on_student_double_click)
    
    def create_add_student_tab(self):
        """Create the add student tab"""
        tab = self.students_tabview.tab("➕ Add Student")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.add_code_entry = ctk.CTkEntry(form_frame)
        self.add_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Name:").pack(pady=(10, 0))
        self.add_name_entry = ctk.CTkEntry(form_frame)
        self.add_name_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Birthdate (YYYY-MM-DD):").pack(pady=(10, 0))
        self.add_birthdate_entry = ctk.CTkEntry(form_frame)
        self.add_birthdate_entry.pack(fill="x", pady=5)
        
        add_btn = ctk.CTkButton(
            form_frame, 
            text="➕ Add Student", 
            command=self.add_student
        )
        add_btn.pack(pady=20)
    
    def create_edit_student_tab(self):
        """Create the edit student tab"""
        tab = self.students_tabview.tab("✏️ Edit Student")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.edit_code_entry = ctk.CTkEntry(form_frame)
        self.edit_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="New Name:").pack(pady=(10, 0))
        self.edit_name_entry = ctk.CTkEntry(form_frame)
        self.edit_name_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="New Birthdate (YYYY-MM-DD):").pack(pady=(10, 0))
        self.edit_birthdate_entry = ctk.CTkEntry(form_frame)
        self.edit_birthdate_entry.pack(fill="x", pady=5)
        
        edit_btn = ctk.CTkButton(
            form_frame, 
            text="✏️ Update Student", 
            command=self.edit_student
        )
        edit_btn.pack(pady=20)
    
    def create_remove_student_tab(self):
        """Create the remove student tab"""
        tab = self.students_tabview.tab("🗑️ Remove Student")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.remove_code_entry = ctk.CTkEntry(form_frame)
        self.remove_code_entry.pack(fill="x", pady=5)
        
        remove_btn = ctk.CTkButton(
            form_frame, 
            text="🗑️ Remove Student", 
            fg_color="red", 
            hover_color="darkred",
            command=self.remove_student
        )
        remove_btn.pack(pady=20)
    
    def load_students_data(self):
        """Load students data into the treeview"""
        for item in self.students_tree.get_children():
            self.students_tree.delete(item)
        
        students = self.load_json_file(self.STUDENTS_FILE)
        
        for code, info in students.items():
            self.students_tree.insert("", "end", values=(code, info.get("name", ""), info.get("birthdate", "")))
    
    def filter_students(self):
        """Filter students based on search term"""
        search_term = self.student_search_entry.get().lower()
        for item in self.students_tree.get_children():
            self.students_tree.delete(item)
        
        students = self.load_json_file(self.STUDENTS_FILE)
        for code, info in students.items():
            if (search_term in code.lower() or 
                search_term in info.get("name", "").lower() or 
                search_term in info.get("birthdate", "").lower()):
                self.students_tree.insert("", "end", values=(code, info.get("name", ""), info.get("birthdate", "")))
    
    def on_student_double_click(self, event):
        """Handle double click on student row"""
        selection = self.students_tree.selection()
        if not selection:
            return
        item = selection[0]
        values = self.students_tree.item(item)["values"]
        
        self.students_tabview.set("✏️ Edit Student")
        self.edit_code_entry.delete(0, "end")
        self.edit_code_entry.insert(0, values[0])
        self.edit_name_entry.delete(0, "end")
        self.edit_name_entry.insert(0, values[1])
        self.edit_birthdate_entry.delete(0, "end")
        self.edit_birthdate_entry.insert(0, values[2])
    
    def add_student(self):
        """Add a new student with comprehensive validation"""
        code = self.add_code_entry.get().strip()
        name = self.add_name_entry.get().strip()
        birthdate = self.add_birthdate_entry.get().strip()
        
        valid_code, code_msg = self.validate_student_code(code)
        if not valid_code:
            messagebox.showerror("Validation Error", code_msg)
            self.add_code_entry.focus()
            return
            
        valid_name, name_msg = self.validate_name(name)
        if not valid_name:
            messagebox.showerror("Validation Error", name_msg)
            self.add_name_entry.focus()
            return
            
        valid_date, date_msg = self.validate_date(birthdate)
        if not valid_date:
            messagebox.showerror("Validation Error", date_msg)
            self.add_birthdate_entry.focus()
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        
        if code in students:
            messagebox.showerror("Error", "Student with this code already exists!")
            self.add_code_entry.focus()
            return
        
        students[code] = {
            "name": name,
            "birthdate": birthdate
        }
        
        if self.save_json_file(self.STUDENTS_FILE, students):
            messagebox.showinfo("Success", "Student added successfully!")
            self.add_code_entry.delete(0, "end")
            self.add_name_entry.delete(0, "end")
            self.add_birthdate_entry.delete(0, "end")
            self.load_students_data()
    
    def edit_student(self):
        """Edit an existing student with comprehensive validation"""
        code = self.edit_code_entry.get().strip()
        name = self.edit_name_entry.get().strip()
        birthdate = self.edit_birthdate_entry.get().strip()
        
        valid_code, code_msg = self.validate_student_code(code)
        if not valid_code:
            messagebox.showerror("Validation Error", code_msg)
            self.edit_code_entry.focus()
            return
            
        valid_name, name_msg = self.validate_name(name)
        if not valid_name:
            messagebox.showerror("Validation Error", name_msg)
            self.edit_name_entry.focus()
            return
            
        valid_date, date_msg = self.validate_date(birthdate)
        if not valid_date:
            messagebox.showerror("Validation Error", date_msg)
            self.edit_birthdate_entry.focus()
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        
        if code not in students:
            messagebox.showerror("Error", "Student not found!")
            self.edit_code_entry.focus()
            return
        
        students[code] = {
            "name": name,
            "birthdate": birthdate
        }
        
        if self.save_json_file(self.STUDENTS_FILE, students):
            messagebox.showinfo("Success", "Student updated successfully!")
            self.load_students_data()
    
    def remove_student(self):
        """Remove a student with validation"""
        code = self.remove_code_entry.get().strip()
        
        if not code:
            messagebox.showerror("Error", "Please enter a student code!")
            self.remove_code_entry.focus()
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        
        if code not in students:
            messagebox.showerror("Error", "Student not found!")
            self.remove_code_entry.focus()
            return
        
        student_name = students[code].get("name", "Unknown")
        if not messagebox.askyesno("Confirm", f"Are you sure you want to remove student '{student_name}' (Code: {code})?"):
            return
        
        del students[code]
        
        if self.save_json_file(self.STUDENTS_FILE, students):
            messagebox.showinfo("Success", "Student removed successfully!")
            self.remove_code_entry.delete(0, "end")
            self.load_students_data()
    
    def show_courses_section(self):
        """Show the courses management section"""
        self.clear_content()
        
        self.courses_tabview = ctk.CTkTabview(self.content_frame)
        self.courses_tabview.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.courses_tabview.add("📚 List Courses")
        self.courses_tabview.add("➕ Add Course")
        self.courses_tabview.add("✏️ Edit Course")
        self.courses_tabview.add("🗑️ Remove Course")
        
        self.create_list_courses_tab()
        self.create_add_course_tab()
        self.create_edit_course_tab()
        self.create_remove_course_tab()
        
        self.load_courses_data()
    
    def create_list_courses_tab(self):
        """Create the list courses tab"""
        tab = self.courses_tabview.tab("📚 List Courses")
        
        search_frame = ctk.CTkFrame(tab)
        search_frame.pack(fill="x", padx=10, pady=10)
        
        ctk.CTkLabel(search_frame, text="🔍 Search:").pack(side="left", padx=5)
        self.course_search_entry = ctk.CTkEntry(search_frame)
        self.course_search_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.course_search_entry.bind("<KeyRelease>", lambda e: self.filter_courses())
        
        tree_frame = ctk.CTkFrame(tab)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        self.courses_tree = ttk.Treeview(
            tree_frame, 
            columns=("code", "name", "max_grade"), 
            show="headings"
        )
        
        self.courses_tree.heading("code", text="Course Code")
        self.courses_tree.heading("name", text="Name")
        self.courses_tree.heading("max_grade", text="Max Grade")
        
        self.courses_tree.column("code", width=120)
        self.courses_tree.column("name", width=200)
        self.courses_tree.column("max_grade", width=100)
        
        v_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.courses_tree.yview)
        h_scroll = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.courses_tree.xview)
        self.courses_tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        self.courses_tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        
        tree_frame.grid_columnconfigure(0, weight=1)
        tree_frame.grid_rowconfigure(0, weight=1)
        
        self.courses_tree.bind("<Double-1>", self.on_course_double_click)
    
    def create_add_course_tab(self):
        """Create the add course tab"""
        tab = self.courses_tabview.tab("➕ Add Course")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Course Code:").pack(pady=(10, 0))
        self.add_course_code_entry = ctk.CTkEntry(form_frame)
        self.add_course_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Course Name:").pack(pady=(10, 0))
        self.add_course_name_entry = ctk.CTkEntry(form_frame)
        self.add_course_name_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Max Grade:").pack(pady=(10, 0))
        self.add_max_grade_entry = ctk.CTkEntry(form_frame)
        self.add_max_grade_entry.pack(fill="x", pady=5)
        
        add_btn = ctk.CTkButton(
            form_frame, 
            text="➕ Add Course", 
            command=self.add_course
        )
        add_btn.pack(pady=20)
    
    def create_edit_course_tab(self):
        """Create the edit course tab"""
        tab = self.courses_tabview.tab("✏️ Edit Course")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Course Code:").pack(pady=(10, 0))
        self.edit_course_code_entry = ctk.CTkEntry(form_frame)
        self.edit_course_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="New Course Name:").pack(pady=(10, 0))
        self.edit_course_name_entry = ctk.CTkEntry(form_frame)
        self.edit_course_name_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="New Max Grade:").pack(pady=(10, 0))
        self.edit_max_grade_entry = ctk.CTkEntry(form_frame)
        self.edit_max_grade_entry.pack(fill="x", pady=5)
        
        edit_btn = ctk.CTkButton(
            form_frame, 
            text="✏️ Update Course", 
            command=self.edit_course
        )
        edit_btn.pack(pady=20)
    
    def create_remove_course_tab(self):
        """Create the remove course tab"""
        tab = self.courses_tabview.tab("🗑️ Remove Course")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Course Code:").pack(pady=(10, 0))
        self.remove_course_code_entry = ctk.CTkEntry(form_frame)
        self.remove_course_code_entry.pack(fill="x", pady=5)
        
        remove_btn = ctk.CTkButton(
            form_frame, 
            text="🗑️ Remove Course", 
            fg_color="red", 
            hover_color="darkred",
            command=self.remove_course
        )
        remove_btn.pack(pady=20)
    
    def load_courses_data(self):
        """Load courses data into the treeview"""
        for item in self.courses_tree.get_children():
            self.courses_tree.delete(item)
        
        courses = self.load_json_file(self.COURSES_FILE)
        
        for code, info in courses.items():
            self.courses_tree.insert("", "end", values=(code, info.get("name", ""), info.get("max_grade", "")))
    
    def filter_courses(self):
        """Filter courses based on search term"""
        search_term = self.course_search_entry.get().lower()
        for item in self.courses_tree.get_children():
            self.courses_tree.delete(item)
        
        courses = self.load_json_file(self.COURSES_FILE)
        for code, info in courses.items():
            if (search_term in code.lower() or 
                search_term in info.get("name", "").lower() or 
                search_term in str(info.get("max_grade", "")).lower()):
                self.courses_tree.insert("", "end", values=(code, info.get("name", ""), info.get("max_grade", "")))
    
    def on_course_double_click(self, event):
        """Handle double click on course row"""
        selection = self.courses_tree.selection()
        if not selection:
            return
        item = selection[0]
        values = self.courses_tree.item(item)["values"]
        
        self.courses_tabview.set("✏️ Edit Course")
        self.edit_course_code_entry.delete(0, "end")
        self.edit_course_code_entry.insert(0, values[0])
        self.edit_course_name_entry.delete(0, "end")
        self.edit_course_name_entry.insert(0, values[1])
        self.edit_max_grade_entry.delete(0, "end")
        self.edit_max_grade_entry.insert(0, values[2])
    
    def add_course(self):
        """Add a new course with validation"""
        code = self.add_course_code_entry.get().strip().upper()
        name = self.add_course_name_entry.get().strip()
        max_grade = self.add_max_grade_entry.get().strip()
        
        valid_code, code_msg = self.validate_course_code(code)
        if not valid_code:
            messagebox.showerror("Validation Error", code_msg)
            self.add_course_code_entry.focus()
            return
            
        valid_name, name_msg = self.validate_name(name)
        if not valid_name:
            messagebox.showerror("Validation Error", name_msg)
            self.add_course_name_entry.focus()
            return
            
        try:
            max_grade = int(max_grade)
            if max_grade <= 0:
                messagebox.showerror("Validation Error", "Max grade must be a positive number")
                self.add_max_grade_entry.focus()
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Max grade must be a valid number")
            self.add_max_grade_entry.focus()
            return
        
        courses = self.load_json_file(self.COURSES_FILE)
        
        if code in courses:
            messagebox.showerror("Error", "Course with this code already exists!")
            self.add_course_code_entry.focus()
            return
        
        courses[code] = {
            "name": name,
            "max_grade": max_grade
        }
        
        if self.save_json_file(self.COURSES_FILE, courses):
            messagebox.showinfo("Success", "Course added successfully!")
            self.add_course_code_entry.delete(0, "end")
            self.add_course_name_entry.delete(0, "end")
            self.add_max_grade_entry.delete(0, "end")
            self.load_courses_data()
    
    def edit_course(self):
        """Edit an existing course with validation"""
        code = self.edit_course_code_entry.get().strip().upper()
        name = self.edit_course_name_entry.get().strip()
        max_grade = self.edit_max_grade_entry.get().strip()
        
        valid_code, code_msg = self.validate_course_code(code)
        if not valid_code:
            messagebox.showerror("Validation Error", code_msg)
            self.edit_course_code_entry.focus()
            return
            
        valid_name, name_msg = self.validate_name(name)
        if not valid_name:
            messagebox.showerror("Validation Error", name_msg)
            self.edit_course_name_entry.focus()
            return
            
        try:
            max_grade = int(max_grade)
            if max_grade <= 0:
                messagebox.showerror("Validation Error", "Max grade must be a positive number")
                self.edit_max_grade_entry.focus()
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Max grade must be a valid number")
            self.edit_max_grade_entry.focus()
            return
        
        courses = self.load_json_file(self.COURSES_FILE)
        
        if code not in courses:
            messagebox.showerror("Error", "Course not found!")
            self.edit_course_code_entry.focus()
            return
        
        courses[code] = {
            "name": name,
            "max_grade": max_grade
        }
        
        if self.save_json_file(self.COURSES_FILE, courses):
            messagebox.showinfo("Success", "Course updated successfully!")
            self.load_courses_data()
    
    def remove_course(self):
        """Remove a course with validation"""
        code = self.remove_course_code_entry.get().strip().upper()
        
        if not code:
            messagebox.showerror("Error", "Please enter a course code!")
            self.remove_course_code_entry.focus()
            return
        
        courses = self.load_json_file(self.COURSES_FILE)
        
        if code not in courses:
            messagebox.showerror("Error", "Course not found!")
            self.remove_course_code_entry.focus()
            return
        
        course_name = courses[code].get("name", "Unknown")
        if not messagebox.askyesno("Confirm", f"Are you sure you want to remove course '{course_name}' (Code: {code})?"):
            return
        
        del courses[code]
        
        if self.save_json_file(self.COURSES_FILE, courses):
            messagebox.showinfo("Success", "Course removed successfully!")
            self.remove_course_code_entry.delete(0, "end")
            self.load_courses_data()
    
    def show_grades_section(self):
        """Show the grades management section"""
        self.clear_content()
        
        self.grades_tabview = ctk.CTkTabview(self.content_frame)
        self.grades_tabview.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.grades_tabview.add("📝 Supply Grade")
        self.grades_tabview.add("📄 Print Results (HTML)")
        self.grades_tabview.add("📊 Bar Chart")
        self.grades_tabview.add("🥧 Pie Chart")
        
        self.create_supply_grade_tab()
        self.create_print_results_tab()
        self.create_bar_chart_tab()
        self.create_pie_chart_tab()
    
    def create_supply_grade_tab(self):
        """Create the supply grade tab"""
        tab = self.grades_tabview.tab("📝 Supply Grade")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.supply_student_code_entry = ctk.CTkEntry(form_frame)
        self.supply_student_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Course Code:").pack(pady=(10, 0))
        self.supply_course_code_entry = ctk.CTkEntry(form_frame)
        self.supply_course_code_entry.pack(fill="x", pady=5)
        
        ctk.CTkLabel(form_frame, text="Grade:").pack(pady=(10, 0))
        self.supply_grade_entry = ctk.CTkEntry(form_frame)
        self.supply_grade_entry.pack(fill="x", pady=5)
        
        supply_btn = ctk.CTkButton(
            form_frame, 
            text="📝 Supply Grade", 
            command=self.supply_grade
        )
        supply_btn.pack(pady=20)
    
    def create_print_results_tab(self):
        """Create the print results tab"""
        tab = self.grades_tabview.tab("📄 Print Results (HTML)")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.print_student_code_entry = ctk.CTkEntry(form_frame)
        self.print_student_code_entry.pack(fill="x", pady=5)
        
        print_btn = ctk.CTkButton(
            form_frame, 
            text="📄 Generate HTML Report", 
            command=self.print_student_result_html
        )
        print_btn.pack(pady=20)
    
    def create_bar_chart_tab(self):
        """Create the bar chart tab"""
        tab = self.grades_tabview.tab("📊 Bar Chart")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(form_frame, text="Student Code:").pack(pady=(10, 0))
        self.bar_chart_student_code_entry = ctk.CTkEntry(form_frame)
        self.bar_chart_student_code_entry.pack(fill="x", pady=5)
        
        chart_btn = ctk.CTkButton(
            form_frame, 
            text="📊 Generate Bar Chart", 
            command=self.bar_chart_student_results
        )
        chart_btn.pack(pady=20)
    
    def create_pie_chart_tab(self):
        """Create the pie chart tab"""
        tab = self.grades_tabview.tab("🥧 Pie Chart")
        
        form_frame = ctk.CTkFrame(tab)
        form_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        chart_btn = ctk.CTkButton(
            form_frame, 
            text="🥧 Generate Pie Chart", 
            command=self.pie_chart_course_registration
        )
        chart_btn.pack(pady=20)
    
    def supply_grade(self):
        """Supply a grade for a student in a course"""
        student_code = self.supply_student_code_entry.get().strip()
        course_code = self.supply_course_code_entry.get().strip().upper()
        grade = self.supply_grade_entry.get().strip()
        
        if not student_code or not course_code or not grade:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        courses = self.load_json_file(self.COURSES_FILE)
        
        if student_code not in students:
            messagebox.showerror("Error", "Student not found!")
            self.supply_student_code_entry.focus()
            return
        
        if course_code not in courses:
            messagebox.showerror("Error", "Course not found!")
            self.supply_course_code_entry.focus()
            return
        
        max_grade = courses[course_code].get("max_grade", 100)
        valid_grade, grade_msg = self.validate_grade(grade, max_grade)
        if not valid_grade:
            messagebox.showerror("Validation Error", grade_msg)
            self.supply_grade_entry.focus()
            return
        
        try:
            with open(self.GRADES_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([student_code, course_code, grade])
            messagebox.showinfo("Success", "Grade supplied successfully!")
            self.supply_student_code_entry.delete(0, "end")
            self.supply_course_code_entry.delete(0, "end")
            self.supply_grade_entry.delete(0, "end")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save grade: {str(e)}")
    
    def print_student_result_html(self):
        """Generate HTML report for a student's results"""
        student_code = self.print_student_code_entry.get().strip()
        
        if not student_code:
            messagebox.showerror("Error", "Please enter a student code!")
            self.print_student_code_entry.focus()
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        if student_code not in students:
            messagebox.showerror("Error", "Student not found!")
            self.print_student_code_entry.focus()
            return
        
        results = []
        try:
            with open(self.GRADES_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0] == student_code:
                        results.append(row)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read grades: {str(e)}")
            return
        
        student_name = students[student_code].get("name", "Unknown")
        
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
        
        try:
            file_name = f"{student_code}_results.html"
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(html)
            messagebox.showinfo("Success", f"Results written to {file_name}")
            webbrowser.open(f"file://{os.path.abspath(file_name)}")
            self.print_student_code_entry.delete(0, "end")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate HTML report: {str(e)}")
    
    def bar_chart_student_results(self):
        """Generate a bar chart for a student's results"""
        student_code = self.bar_chart_student_code_entry.get().strip()
        
        if not student_code:
            messagebox.showerror("Error", "Please enter a student code!")
            self.bar_chart_student_code_entry.focus()
            return
        
        students = self.load_json_file(self.STUDENTS_FILE)
        if student_code not in students:
            messagebox.showerror("Error", "Student not found!")
            self.bar_chart_student_code_entry.focus()
            return
        
        courses = []
        grades = []
        try:
            with open(self.GRADES_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0] == student_code:
                        courses.append(row[1])
                        grades.append(int(row[2]))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read grades: {str(e)}")
            return
        
        if not courses:
            messagebox.showerror("Error", "No grades found for this student!")
            return
        
        plt.figure(figsize=(8, 6))
        plt.bar(courses, grades, color="#4CAF50")
        plt.title(f"Grades for {student_code}")
        plt.xlabel("Course")
        plt.ylabel("Grade")
        plt.tight_layout()
        plt.show()
    
    def pie_chart_course_registration(self):
        """Generate a pie chart for course registration distribution"""
        course_counts = {}
        try:
            with open(self.GRADES_FILE, "r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        course = row[1]
                        course_counts[course] = course_counts.get(course, 0) + 1
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read grades: {str(e)}")
            return
        
        if not course_counts:
            messagebox.showerror("Error", "No course registrations found!")
            return
        
        plt.figure(figsize=(8, 6))
        plt.pie(course_counts.values(), labels=course_counts.keys(), autopct='%1.1f%%', colors=["#4CAF50", "#FF9800", "#2196F3", "#F44336"])
        plt.title("Course Registration Distribution")
        plt.tight_layout()
        plt.show()
    
    def clear_content(self):
        """Clear the content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    try:
        app = StudentsManagementApp()
        app.mainloop()
    except Exception as e:
        print(f"Application error: {str(e)}")
        messagebox.showerror("Application Error", f"Failed to start application: {str(e)}")