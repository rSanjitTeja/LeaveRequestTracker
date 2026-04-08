import json
import os
import tkinter as tk
from tkinter import messagebox

FILE = "leaves.json"

def show_approve_reject(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Approve / Reject Leave", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

    form_frame = tk.Frame(parent, bg="#ecf0f1")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="Enter Leave ID:", bg="#ecf0f1").grid(row=0, column=0, pady=5, padx=5)
    id_entry = tk.Entry(form_frame, width=20)
    id_entry.grid(row=0, column=1, pady=5, padx=5)

    def process_decision(decision):
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

            found = False
            for leave in data:
                if leave["id"] == leave_id:
                    leave["status"] = decision
                    found = True
                    break

            if not found:
                messagebox.showerror("Error", "Leave ID not found")
                return

            with open(FILE, "w") as f:
                json.dump(data, f, indent=4)

            messagebox.showinfo("Success", f"Leave ID {leave_id} marked as {decision}!")
            id_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Error updating status: {e}")

    btn_frame = tk.Frame(parent, bg="#ecf0f1")
    btn_frame.pack(pady=20)
    
    tk.Button(btn_frame, text="Approve", command=lambda: process_decision("Approved"), bg="#27ae60", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="left", padx=15)
    tk.Button(btn_frame, text="Reject", command=lambda: process_decision("Rejected"), bg="#c0392b", fg="white", font=("Arial", 10, "bold"), width=12).pack(side="right", padx=15)
