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
    