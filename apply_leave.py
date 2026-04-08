import json
import os
import tkinter as tk
from tkinter import messagebox

FILE = "leaves.json"

def show_apply_leave(parent):
    # Clear parent
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Apply for Leave", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

    form_frame = tk.Frame(parent, bg="#ecf0f1")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Employee Name:", bg="#ecf0f1").grid(row=0, column=0, pady=5, padx=5, sticky="e")
    name_entry = tk.Entry(form_frame, width=30)
    name_entry.grid(row=0, column=1, pady=5, padx=5)

    tk.Label(form_frame, text="Number of Leave Days:", bg="#ecf0f1").grid(row=1, column=0, pady=5, padx=5, sticky="e")
    days_entry = tk.Entry(form_frame, width=30)
    days_entry.grid(row=1, column=1, pady=5, padx=5)

    def submit_leave():
        name = name_entry.get().strip()
        days_str = days_entry.get().strip()
        
        if not name or not days_str:
            messagebox.showerror("Error", "Please fill all fields")
            return
            
        try:
            days = int(days_str)
        except ValueError:
            messagebox.showerror("Error", "Days must be an integer")
            return

        leave = {
            "id": None,
            "name": name,
            "days": days,
            "status": "Pending"
        }

        if not os.path.exists(FILE):
            data = []
        else:
            try:
                with open(FILE, "r") as f:
                    data = json.load(f)
            except Exception:
                data = []

        # Find max id to avoid duplication on delete
        max_id = 0
        if data:
            max_id = max(item.get("id", 0) for item in data)
            
        leave["id"] = max_id + 1
        data.append(leave)

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo("Success", "Leave applied successfully!")
        name_entry.delete(0, tk.END)
        days_entry.delete(0, tk.END)

    tk.Button(parent, text="Submit", command=submit_leave, bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=20)
