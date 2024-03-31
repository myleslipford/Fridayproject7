import tkinter as tk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('users.db')
cursor = conn.cursor()

def check_credentials(email, password):
    cursor.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    return cursor.fetchone() is not None

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

login_button = tk.Button(root, text="Login", command=handle_login)
login_button.grid(row=2, columnspan=2, padx=5, pady=5)

login_success_label = tk.Label(root, text="", fg="green")
login_success_label.grid(row=3, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()

# Close database connection when application exits
conn.close()
