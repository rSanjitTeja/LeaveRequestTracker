import tkinter as tk
from apply_leave import show_apply_leave
from view_leaves import show_view_leaves
from approve_reject import show_approve_reject
from delete_leave import show_delete_leave
from summary import show_summary

class LeaveTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leave Tracker - Login")
        self.root.geometry("650x450")
        self.role = None
        
        # Start by showing the login screen
        self.show_login()
        
    def show_login(self):
        # Clear root
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.root.title("Leave Tracker - Login")
            
        login_frame = tk.Frame(self.root, bg="#ecf0f1")
        login_frame.pack(fill="both", expand=True)
        
        tk.Label(login_frame, text="Welcome to Leave Tracker", font=("Arial", 22, "bold"), bg="#ecf0f1").pack(pady=40)
        tk.Label(login_frame, text="Select Your Role:", font=("Arial", 14), bg="#ecf0f1").pack(pady=10)
        
        tk.Button(login_frame, text="Client (Employee)", command=lambda: self.load_app("Client"),
                  bg="#3498db", fg="white", font=("Arial", 12, "bold"), width=20, pady=10, cursor="hand2").pack(pady=10)
        
        tk.Button(login_frame, text="Admin (Manager)", command=lambda: self.load_app("Admin"),
                  bg="#2c3e50", fg="white", font=("Arial", 12, "bold"), width=20, pady=10, cursor="hand2").pack(pady=10)

    def load_app(self, role):
        self.role = role
        
        # Clear root to load app
        for widget in self.root.winfo_children():
            widget.destroy()
            
        self.root.title(f"Leave Tracker - {self.role} Panel")
        
        # Create a sidebar frame for navigation
        self.sidebar = tk.Frame(self.root, bg="#2c3e50", width=180)
        self.sidebar.pack(side="left", fill="y", expand=False)
        
        # Create a main content frame
        self.content_frame = tk.Frame(self.root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Define role-based navigation logic
        if self.role == "Admin":
            self.nav_buttons = [
                ("View All Leaves", self.nav_view),
                ("Approve/Reject", self.nav_approve),
                ("Delete Leave", self.nav_delete),
                ("Summary Report", self.nav_summary),
                ("Logout", self.show_login)
            ]
            default_func = self.nav_view # Default screen for admin
        else: # Client
            self.nav_buttons = [
                ("Apply Leave", self.nav_apply),
                ("View Leaves", self.nav_view),
                ("Logout", self.show_login)
            ]
            default_func = self.nav_apply # Default screen for client
            
        self.create_sidebar()
        default_func()
        
    def create_sidebar(self):
        tk.Label(self.sidebar, text=f"{self.role} Menu", bg="#2c3e50", fg="white", font=("Arial", 14, "bold")).pack(pady=20)
        
        for text, command in self.nav_buttons:
            # Differentiate logout button color
            btn_bg = "#e74c3c" if text == "Logout" else "#34495e"
            
            btn = tk.Button(self.sidebar, text=text, command=command, bg=btn_bg, fg="white", 
                            font=("Arial", 11), activebackground="#1abc9c", activeforeground="white", 
                            bd=0, pady=10, cursor="hand2")
            btn.pack(fill="x", padx=10, pady=5)
            
    # Routing functions mapping to the 5 modules
    def nav_apply(self):
        show_apply_leave(self.content_frame)

    def nav_view(self):
        show_view_leaves(self.content_frame)

    def nav_approve(self):
        show_approve_reject(self.content_frame)

    def nav_delete(self):
        show_delete_leave(self.content_frame)

    def nav_summary(self):
        show_summary(self.content_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = LeaveTrackerApp(root)
    root.mainloop()
