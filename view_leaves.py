import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

FILE = "leaves.json"

def show_view_leaves(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Leave Requests", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

    # Creating a Treeview
    columns = ("id", "name", "days", "status")
    tree = ttk.Treeview(parent, columns=columns, show="headings", height=12)
    
    # Configure headings
    tree.heading("id", text="ID")
    tree.heading("name", text="Employee Name")
    tree.heading("days", text="Days")
    tree.heading("status", text="Status")
    
    # Configure columns
    tree.column("id", width=50, anchor="center")
    tree.column("name", width=150, anchor="w")
    tree.column("days", width=80, anchor="center")
    tree.column("status", width=100, anchor="center")
    
    tree.pack(pady=10, fill="both", expand=True, padx=20)

    try:
        if not os.path.exists(FILE):
            data = []
        else:
            with open(FILE, "r") as f:
                data = json.load(f)

        if not data:
            tk.Label(parent, text="No leave records found.", bg="#ecf0f1").pack(pady=10)
        else:
            for leave in data:
                tree.insert("", tk.END, values=(leave.get("id"), leave.get("name"), leave.get("days"), leave.get("status")))
                
    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")
