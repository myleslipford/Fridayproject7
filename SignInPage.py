import tkinter as tk
from tkinter import messagebox
import sqlite3


root = tk.Tk()
root.title("Sign In")

email_label = tk.Label(root, text="Email:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
email_entry = tk.Entry(root)
email_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)