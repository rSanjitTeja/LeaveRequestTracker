import json
import os
import tkinter as tk
from tkinter import messagebox

FILE = "leaves.json"

def show_summary(parent):
    for widget in parent.winfo_children():
        widget.destroy()

    tk.Label(parent, text="Summary Report", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=20)

    stats_frame = tk.Frame(parent, bg="#fff", bd=2, relief="groove", padx=30, pady=20)
    stats_frame.pack(pady=10)

    try:
        if not os.path.exists(FILE):
            data = []
        else:
            with open(FILE, "r") as f:
                data = json.load(f)

        total = len(data)
        approved = sum(1 for l in data if l.get("status") == "Approved")
        pending = sum(1 for l in data if l.get("status") == "Pending")
        rejected = sum(1 for l in data if l.get("status") == "Rejected")

        tk.Label(stats_frame, text=f"Total Requests: {total}", font=("Arial", 14), bg="#fff").pack(anchor="w", pady=5)
        tk.Label(stats_frame, text=f"Approved: {approved}", font=("Arial", 14, "bold"), fg="#27ae60", bg="#fff").pack(anchor="w", pady=5)
        tk.Label(stats_frame, text=f"Pending: {pending}", font=("Arial", 14, "bold"), fg="#f39c12", bg="#fff").pack(anchor="w", pady=5)
        tk.Label(stats_frame, text=f"Rejected: {rejected}", font=("Arial", 14, "bold"), fg="#c0392b", bg="#fff").pack(anchor="w", pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"Error loading data: {e}")

    tk.Button(parent, text="Refresh", command=lambda: show_summary(parent), bg="#2980b9", fg="white", font=("Arial", 10, "bold"), width=15).pack(pady=20)
