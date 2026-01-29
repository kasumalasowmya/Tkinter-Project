import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import scrolledtext


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Header
        header = tk.Frame(self, bg="#06A77D")
        header.pack(fill="x")

        tk.Label(
            header,
            text="📝 MIST Dashboard",
            font=("Helvetica", 24, "bold"),
            bg="#06A77D",
            fg="white"
        ).pack(pady=20)

        # Form frame
        form_frame = ttk.Frame(self)
        form_frame.pack(fill="both", expand=True, padx=40, pady=20)

        # First Name
        ttk.Label(form_frame, text="FIRST NAME:", font=("Helvetica", 11)).pack(anchor="w")
        self.firstname_entry = ttk.Entry(form_frame, width=35)
        self.firstname_entry.pack(anchor="w", pady=(0, 12))

        # Last Name
        ttk.Label(form_frame, text="LAST NAME:", font=("Helvetica", 11)).pack(anchor="w")
        self.lastname_entry = ttk.Entry(form_frame, width=35)
        self.lastname_entry.pack(anchor="w", pady=(0, 12))

        # Section
        ttk.Label(form_frame, text="SECTION:", font=("Helvetica", 11)).pack(anchor="w")
        self.section_var = tk.StringVar()

        section_combo = ttk.Combobox(
            form_frame,
            textvariable=self.section_var,
            values=[
                "Select",
                "Computer Science and Engineering",
                "Artificial Intelligence and Machine Learning",
                "Other"
            ],
            state="readonly"
        )
        section_combo.pack(anchor="w", pady=(0, 15), fill="x")
        section_combo.set("Select")

        # Description
        ttk.Label(form_frame, text="DESCRIPTION:", font=("Helvetica", 11)).pack(anchor="w")
        self.description_text = scrolledtext.ScrolledText(
            form_frame,
            height=6,
            wrap="word"
        )
        self.description_text.pack(fill="x", pady=(0, 15))

        # Upload Image
        ttk.Button(
            form_frame,
            text="📸 Upload Image",
            command=self.upload_image
        ).pack(anchor="w", pady=5)

        # Percentage
        ttk.Label(form_frame, text="PERCENTAGE:", font=("Helvetica", 11)).pack(anchor="w")
        self.percentage_entry = ttk.Entry(form_frame, width=35)
        self.percentage_entry.pack(anchor="w", pady=(0, 12))

        # Buttons
        button_frame = ttk.Frame(form_frame)
        button_frame.pack(fill="x", pady=10)

        ttk.Button(
            button_frame,
            text="SUBMIT",
            command=self.signup
        ).pack(side="left", padx=5)

        ttk.Button(
            button_frame,
            text="RETURN TO LOGIN",
            command=self.back_to_home
        ).pack(side="right", padx=5)

    def upload_image(self):
        filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

    def signup(self):
        firstname = self.firstname_entry.get().strip()
        lastname = self.lastname_entry.get().strip()
        section = self.section_var.get()
        description = self.description_text.get("1.0", tk.END).strip()

        if not all([firstname, lastname, section != "Select", description]):
            messagebox.showerror("Error", "Please fill all fields!")
            return

        messagebox.showinfo("Success", "Signup successful!")

    def back_to_home(self):
        messagebox.showinfo("Navigation", "Back to Login Page")


# ================= EXECUTION =================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Blog App - Signup")
    root.geometry("450x650")

    signup_page = SignupPage(root, root)
    signup_page.pack(fill="both", expand=True)

    root.mainloop()
