import tkinter as tk
from tkinter import messagebox
import sqlite3

def submit_signup():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        return
    
    if not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email address.")
        return
    
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)')
        cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Sign up successful. You can now login.")
    except sqlite3.Error as e:
        print("SQLite error:", e)
        messagebox.showerror("Error", "An error occurred while signing up. Please try again later.")


root.mainloop()