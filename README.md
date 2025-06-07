# Students-Management-System
A simple, colorful, and user-friendly Python application to manage students, courses, and grades.
Ideal for educational environments and learning purposes. Includes both command-line and customizable GUI (Tkinter) interfaces.

## Features
![Screenshot 2025-06-07 073033](https://github.com/user-attachments/assets/2317e7b3-f50b-4e78-becd-095a571afd6d)

![Screenshot 2025-06-07 122245](https://github.com/user-attachments/assets/82a2edf6-f95c-4d5f-ab3a-780710190fbd)

![Screenshot 2025-06-07 122536](https://github.com/user-attachments/assets/69792ea6-78dc-4423-983d-ff4fe6a457b5)

![Screenshot 2025-06-07 122304](https://github.com/user-attachments/assets/2c02e731-336b-4af1-b7e4-5eae4f56e38f)

![Screenshot 2025-06-07 122546](https://github.com/user-attachments/assets/2445fa07-6e91-4126-bfe6-0da627a5e3d1)

![Screenshot 2025-06-07 122343](https://github.com/user-attachments/assets/d63f9966-14ed-47c9-ac7b-4e1681f5c444)

![Screenshot 2025-06-07 122848](https://github.com/user-attachments/assets/ef211b18-9e0b-4d1b-8d8e-d727b2e52b5b)

- **Student Management**: Add, list, and delete student records
- **Course Management**: Create and manage courses
- **Grade Recording**: Assign grades per student and course
- **HTML Reports**: Export final results per student as a styled HTML file
- **Data Visualization**:
  - 📊 Bar charts for student grades
  - 🥧 Pie charts for course enrollment


## 🗂 File Structure

| File              | Description                                       |
|-------------------|---------------------------------------------------|
| `main.py`         | Main CLI application to manage students, courses, and grades |
| `gui.py` _(opt)_  | Simple GUI using Tkinter for entering student data |
| `students.json`   | Stores student data in JSON format                |
| `courses.json`    | Stores course information                         |
| `grades.csv`      | Stores student-course-grade mappings              |
| `*_report.html`   | HTML reports auto-generated per student           |

## 🛠️ Requirements
- **Language**: Python 3
- **UI**: Tkinter (optional)
- **Charts**: `matplotlib` for visual output
