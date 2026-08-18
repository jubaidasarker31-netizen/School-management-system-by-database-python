There is my Student management system by database, python and Tkinter
# 🎓 Student Management System

A simple and user-friendly **Student Management System** built with **Python, PostgreSQL, and Tkinter**.

This project allows users to manage student information through a graphical user interface (GUI). It supports basic **CRUD operations** such as adding, updating, deleting, and viewing student records.

---

## ✨ Features

- ➕ Add Student
- ✏️ Update Student
- 🗑️ Delete Student
- 🔄 Refresh Student Records
- 🧹 Clear Input Fields
- 📋 View All Students
- 🗄️ PostgreSQL Database Integration
- 🖥️ Tkinter Graphical User Interface
- 🎨 User-friendly and colorful dashboard design

---

## 🛠️ Technologies Used

- 🐍 **Python**
- 🐘 **PostgreSQL**
- 🖼️ **Tkinter**
- 🔌 **psycopg2-binary**
- 🎨 **ttk / Tkinter Styling**

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
└── README.md

🗄️ Database

This project uses PostgreSQL as the database.

Student Table

The student table contains information such as:

Column	Description
ID	Unique student ID
Name	Student name
Age	Student age
Gender	Student gender
Department	Student department
Email	Student email
Phone	Student phone number
City	Student city
📦 Installation
1. Clone the Repository
git clone https://github.com/jubaidasarker31-netizen/School-management-system-by-database-python.git
2. Go to the Project Folder
cd School-management-system-by-database-python
3. Create a Virtual Environment
python -m venv v
4. Activate the Virtual Environment

For Windows:

v\Scripts\activate
5. Install Required Package
pip install -r requirements.txt

Or install psycopg2-binary directly:

pip install psycopg2-binary
⚙️ PostgreSQL Setup

First, make sure PostgreSQL is installed and running on your computer.

Create a database in PostgreSQL, for example:

CREATE DATABASE students_db;

Then create the student table:

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    gender VARCHAR(20),
    department VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    city VARCHAR(100)
);

Update your PostgreSQL connection information in database.py according to your local PostgreSQL setup.

Example:

conn = psycopg2.connect(
    host="localhost",
    database="students_db",
    user="postgres",
    password="YOUR_PASSWORD",
    port="5432"
)
▶️ Run the Project

After setting up PostgreSQL and installing the required packages, run:

python app.py

The Student Management System GUI will open.

🔄 CRUD Operations
Create

Add a new student using the Add Student button.

Read

Student records are displayed in the table.

Update

Select a student and update their information using Update Student.

Delete

Select a student and remove the record using Delete Student.

🖥️ User Interface

The application contains:

📊 Dashboard-style sidebar
🎓 School management header
📝 Student information form
🔘 CRUD operation buttons
📋 Student data table
🎨 Green-themed user interface
🎯 Project Purpose

This project was created to practice:

Python programming
GUI development with Tkinter
PostgreSQL database management
SQL queries
CRUD operations
Python database connectivity
Basic software project structure
🔮 Future Improvements

Some features that can be added in the future:

🔐 User Login System
🔎 Student Search
📊 Dashboard Statistics
📄 Generate Student Reports
📥 Export Data to Excel/PDF
🖼️ Student Profile Pictures
📱 More responsive GUI
👥 Teacher Management
📚 Course Management
💰 Student Fee Management
👩‍💻 Author

Jubaida Sarker

GitHub:

https://github.com/jubaidasarker31-netizen
