import json
import os
import tkinter as tk
from tkinter import messagebox

FILE = "leaves.json"

def show_delete_leave(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Delete Leave Request", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

    form_frame = tk.Frame(parent, bg="#ecf0f1")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Enter Leave ID:", bg="#ecf0f1").grid(row=0, column=0, pady=5, padx=5)
    id_entry = tk.Entry(form_frame, width=20)
    id_entry.grid(row=0, column=1, pady=5, padx=5)

    def perform_delete():
        leave_id_str = id_entry.get().strip()
        if not leave_id_str:
            messagebox.showerror("Error", "Please enter Leave ID")
            return
            
        try:
            leave_id = int(leave_id_str)
        except ValueError:
            messagebox.showerror("Error", "Leave ID must be an integer")
            return

        if not os.path.exists(FILE):
            messagebox.showwarning("Warning", "No data found")
            return
            
        try:
            with open(FILE, "r") as f:
                data = json.load(f)

            original_length = len(data)
            data = [leave for leave in data if leave.get("id") != leave_id]

            if len(data) == original_length:
                messagebox.showerror("Error", "Leave ID not found")
                return

            with open(FILE, "w") as f:
                json.dump(data, f, indent=4)

            messagebox.showinfo("Success", "Leave deleted successfully!")
            id_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Error deleting leave: {e}")

    tk.Button(parent, text="Delete", command=perform_delete, bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=20)
