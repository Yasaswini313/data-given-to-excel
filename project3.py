import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox

# Sample data (replace this with your actual data)
data = [
    {"Name": "Anjali", "Roll Number": "101", "Branch": "CSE", "Phone Number": "1234567890",
     "Email ID": "chinni@example.com", "State": "California", "Country": "USA"},
    {"Name": "pandu", "Roll Number": "102", "Branch": "ECE", "Phone Number": "9876543210",
     "Email ID": "pandu@example.com", "State": "New York", "Country": "USA"},
     {"Name": "Manga", "Roll Number": "103", "Branch": "CSE", "Phone Number": "8797086789",
     "Email ID": "manga@example.com", "State": "California", "Country": "USA"},
    {"Name": "govindu", "Roll Number": "104", "Branch": "ECE", "Phone Number": "8960745632",
     "Email ID": "govindu@example.com", "State": "New York", "Country": "USA"},
    # Add more data rows as needed
]

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

def show_details():
    name = name_var.get()
    roll_number = roll_var.get()
    
    # Filter the DataFrame based on the name and roll number
    details = df[(df["Name"] == name) & (df["Roll Number"] == roll_number)]
    
    if not details.empty:
        # Create a new window to display the details
        details_window = tk.Toplevel(root)
        details_window.title("Details")
        
        # Create a Table to display the details
        table = ttk.Treeview(details_window, columns=list(details.columns), show="headings")
        for col in details.columns:
            table.heading(col, text=col)
        for _, row in details.iterrows():
            table.insert("", "end", values=list(row))
        
        table.pack(expand=True, fill="both")
   
    else:
        tk.messagebox.showerror("Error", "Details not found!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Student Details")

# Labels and Entry fields for Name and Roll Number
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.grid(row=0, column=1, padx=5, pady=5)

roll_label = tk.Label(root, text="Roll Number:")
roll_label.grid(row=1, column=0, padx=5, pady=5)
roll_var = tk.StringVar()
roll_entry = tk.Entry(root, textvariable=roll_var)
roll_entry.grid(row=1, column=1, padx=5, pady=5)

# Button to show details
show_button = tk.Button(root, text="Show Details", command=show_details)
show_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
