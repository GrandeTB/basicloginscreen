import tkinter as tk
from tkinter import messagebox

user_database = [
{"username" : "user1", "password": "pass1"},
{"username": "user2", "password": "pass2"}
]

def verify_login(): 
    username = username_entry.get()
    password = password_entry.get()

    for user in user_database:
        if user["username"] ==username and user["password"] == password:
            messagebox.showinfo("Login success", f"Welcome {username}!")
            return
        

    messagebox.showerror("Login failed", "Invalid username or password")


def create_login_page():
    global username_entry, password_entry

    window = tk.Tk()
    window.title("Login Page")

   
    tk.Label(window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

   
    tk.Label(window, text="Password").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

   
    login_button = tk.Button(window, text="Login", command=verify_login)
    login_button.grid(row=2, columnspan=2, pady=10)

   
    window.mainloop()


create_login_page()