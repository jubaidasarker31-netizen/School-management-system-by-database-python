import tkinter as tk
from tkinter import ttk, messagebox

from database import get_connection



# =========================
# Add students
# =========================
def add_students():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_combo.get()
    department = department_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    city = city_entry.get()

    if name == "" or age == "":
        messagebox.showwarning(
            "Warning",
            "Name and Age are required!"
        )
        return

    try:
        age = int(age)

        conn = get_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO students
            (name, age, gender, department, email, phone, city)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                name,
                age,
                gender,
                department,
                email,
                phone,
                city
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo(
            "Success",
            "students added successfully!"
        )

        clear_fields()
        load_studentss()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number!"
        )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================
# Load studentss
# =========================
def load_studentss():
    for row in students_table.get_children():
        students_table.delete(row)

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                name,
                age,
                gender,
                department,
                email,
                phone,
                city
            FROM students
            ORDER BY id
        """)

        rows = cursor.fetchall()

        for row in rows:
            students_table.insert(
                "",
                tk.END,
                values=row
            )

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================
# Select students
# =========================
def select_students(event):
    selected = students_table.focus()

    if not selected:
        return

    values = students_table.item(
        selected,
        "values"
    )

    clear_fields()

    id_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    age_entry.insert(0, values[2])
    gender_combo.set(values[3])
    department_entry.insert(0, values[4])
    email_entry.insert(0, values[5])
    phone_entry.insert(0, values[6])
    city_entry.insert(0, values[7])


# =========================
# Update students
# =========================
def update_students():
    students_id = id_entry.get()

    if students_id == "":
        messagebox.showwarning(
            "Warning",
            "Please select a students first!"
        )
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
            UPDATE students
            SET
                name = %s,
                age = %s,
                gender = %s,
                department = %s,
                email = %s,
                phone = %s,
                city = %s
            WHERE id = %s
        """

        cursor.execute(
            query,
            (
                name_entry.get(),
                int(age_entry.get()),
                gender_combo.get(),
                department_entry.get(),
                email_entry.get(),
                phone_entry.get(),
                city_entry.get(),
                students_id
            )
        )

        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo(
            "Success",
            "students updated successfully!"
        )

        clear_fields()
        load_studentss()

    except ValueError:
        messagebox.showerror(
            "Error",
            "Age must be a number!"
        )

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================
# Delete students
# =========================
def delete_students():
    students_id = id_entry.get()

    if students_id == "":
        messagebox.showwarning(
            "Warning",
            "Please select a students first!"
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this students?"
    )

    if not confirm:
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (students_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo(
            "Success",
            "students deleted successfully!"
        )

        clear_fields()
        load_studentss()

    except Exception as e:
        messagebox.showerror(
            "Database Error",
            str(e)
        )


# =========================
# Clear Fields
# =========================
def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

    gender_combo.set("Male")

    department_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)


# =========================
# Main Window
# =========================
root = tk.Tk()

root.title("Yellow-Green School"),
root.geometry("1200x700"),
root.configure(bg="#F4F7F6"),
root.resizable(False, False)
# =========================
# Sidebar
# =========================

sidebar = tk.Frame(
    root,
    bg="#1B5E20",
    width=220
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)
sidebar_title = tk.Label(
    sidebar,
    text="📚\nSTUDENT\nMANAGEMENT\nSYSTEM",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1B5E20",
    justify="center"
)

sidebar_title.pack(
    pady=(30, 40)
)

dashboard_btn = tk.Button(
    sidebar,
    text="🏠  Dashboard",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#2E7D32",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    anchor="w",
    padx=20,
    width=20
)

dashboard_btn.pack(
    pady=5,
    ipady=8
)
students_btn = tk.Button(
    sidebar,
    text="👨‍🎓  Students",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#1B5E20",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    anchor="w",
    padx=20,
    width=20
)

students_btn.pack(
    pady=5,
    ipady=8
)
add_btn = tk.Button(
    sidebar,
    text="➕  Add Student",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#1B5E20",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    anchor="w",
    padx=20,
    width=20
)

add_btn.pack(
    pady=5,
    ipady=8
)
report_btn = tk.Button(
    sidebar,
    text="📊  Reports",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#1B5E20",
    activebackground="#388E3C",
    activeforeground="white",
    relief="flat",
    anchor="w",
    padx=20,
    width=20
)

report_btn.pack(
    pady=5,
    ipady=8
)
main_frame = tk.Frame(
    root,
    bg="#F4F7F6"
)

main_frame.pack(
    side="left",
    fill="both",
    expand=True
)


# =========================
# Title
# =========================
header = tk.Frame(
    main_frame,
    bg="#2E7D32",
    height=80
)

header.pack(
    fill="x",
    padx=15,
    pady=(15, 10)
)

title = tk.Label(
    header,
    text="🎓 Yellow-Green School",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#2E7D32"
)

title.pack(pady=20)


# =========================
# Form Frame
# =========================
# =========================
# Form Frame
# =========================

form_frame = tk.Frame(
    main_frame,
    bg="white",
    bd=1,
    relief="solid"
)

form_frame.pack(
    padx=40,
    pady=10,
    fill="x"
)


# =========================
# Student ID
# =========================

tk.Label(
    form_frame,
    text="Student ID",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=0, column=0, padx=15, pady=10, sticky="w")

id_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

id_entry.grid(row=0, column=1, padx=10, pady=10)


# =========================
# Name
# =========================

tk.Label(
    form_frame,
    text="Name",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=0, column=2, padx=15, pady=10, sticky="w")

name_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

name_entry.grid(row=0, column=3, padx=10, pady=10)


# =========================
# Age
# =========================

tk.Label(
    form_frame,
    text="Age",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=1, column=0, padx=15, pady=10, sticky="w")

age_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

age_entry.grid(row=1, column=1, padx=10, pady=10)


# =========================
# Gender
# =========================

tk.Label(
    form_frame,
    text="Gender",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=1, column=2, padx=15, pady=10, sticky="w")

gender_entry = ttk.Combobox(
    form_frame,
    width=23,
    font=("Arial", 11),
    values=["Male", "Female", "Other"],
    state="readonly"
)

gender_entry.set("Male")

gender_entry.grid(row=1, column=3, padx=10, pady=10)


# =========================
# Department
# =========================

tk.Label(
    form_frame,
    text="Department",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=2, column=0, padx=15, pady=10, sticky="w")

department_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

department_entry.grid(row=2, column=1, padx=10, pady=10)


# =========================
# Email
# =========================

tk.Label(
    form_frame,
    text="Email",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=2, column=2, padx=15, pady=10, sticky="w")

email_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

email_entry.grid(row=2, column=3, padx=10, pady=10)


# =========================
# Phone
# =========================

tk.Label(
    form_frame,
    text="Phone",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=3, column=0, padx=15, pady=10, sticky="w")

phone_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

phone_entry.grid(row=3, column=1, padx=10, pady=10)


# =========================
# City
# =========================

tk.Label(
    form_frame,
    text="City",
    font=("Arial", 11, "bold"),
    fg="#2E3A3A",
    bg="white"
).grid(row=3, column=2, padx=15, pady=10, sticky="w")

city_entry = tk.Entry(
    form_frame,
    width=25,
    font=("Arial", 11),
    bg="#F8FAF9",
    fg="#222222",
    relief="solid",
    bd=1
)

city_entry.grid(row=3, column=3, padx=10, pady=10)

# =========================
# Buttons
# =========================
button_frame = tk.Frame(
    main_frame,
    bg="#F4F7F6"
)

button_frame.pack(pady=15)


tk.Button(
    button_frame,
    text="Add Student",
    width=15,
    bg="#2E7D32",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#1B5E20",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=add_students
).grid(row=0, column=0, padx=6)

tk.Button(
    button_frame,
    text="Update Student",
    width=15,
    bg="#1976D2",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#0D47A1",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=update_students
).grid(row=0, column=1, padx=6)


tk.Button(
    button_frame,
    text="Delete Student",
    width=15,
    bg="#D32F2F",
    fg="white",
    font=("Arial", 10, "bold"),
    activebackground="#B71C1C",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=delete_students
).grid(row=0, column=2, padx=6)

tk.Button(
    button_frame,
    text="Clear",
    width=12,
    bg="#F9A825",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=clear_fields
).grid(row=0, column=3, padx=6)


tk.Button(
    button_frame,
    text="Refresh",
    width=12,
    bg="#30347E",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    command=clear_fields
).grid(row=0, column=3, padx=6)



# =========================
# Table
# =========================
table_frame = tk.Frame(
    main_frame,
    bg="#F4F7F6"
)

table_frame.pack(
    fill=tk.BOTH,
    expand=True,
    padx=20,
    pady=10
)


columns = (
    "ID",
    "Name",
    "Age",
    "Gender",
    "Department",
    "Email",
    "Phone",
    "City"
)

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview.Heading",
    background="#2E7D32",
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10
)

style.configure(
    "Treeview",
    background="white",
    foreground="#222222",
    fieldbackground="white",
    font=("Arial", 10),
    rowheight=32
)
style.map(
    "Treeview",
    background=[
        ("selected", "#A5D6A7")
    ],
    foreground=[
        ("selected", "#000000")
    ]
)

students_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)


for column in columns:
    students_table.heading(
        column,
        text=column
    )

    students_table.column(
        column,
        width=125
    )


students_table.column(
    "ID",
    width=50
)

students_table.pack(
    side=tk.LEFT,
    fill=tk.BOTH,
    expand=True
)


# Scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient=tk.VERTICAL,
    command=students_table.yview
)

students_table.configure(
    yscrollcommand=scrollbar.set
)

scrollbar.pack(
    side=tk.RIGHT,
    fill=tk.Y
)


# Select row
students_table.bind(
    "<ButtonRelease-1>",
    select_students
)


# Load data when application starts
load_studentss()


root.mainloop()