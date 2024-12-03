import tkinter as tk
from tkinter import filedialog, messagebox
import openai
import os

class ResumeBuilder:
    def __init__(self, frame,show_home_callback):
        self.frame = frame
        self.show_home_callback = show_home_callback
        self.api_key = os.getenv("OPENAI_API_KEY")  
        if not self.api_key:
            raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
        openai.api_key = self.api_key
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.frame, text="Resume Builder", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.frame, text="Enter Job Description:").pack()
        self.job_description_input = tk.Text(self.frame, height=5, width=50)
        self.job_description_input.pack(pady=10)
        tk.Button(self.frame, text="Generate Resume", command=self.generate_resume).pack(pady=10)
        tk.Label(self.frame, text="Generated Resume:").pack()
        self.resume_output = tk.Text(self.frame, height=15, width=50)
        self.resume_output.pack(pady=10)
        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Save Resume", command=self.save_resume).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_all).grid(row=0, column=1, padx=5)
         # Back to Home Button
        tk.Button(self.frame, text="Back to Home", command=lambda: self.show_home_callback("Home")).pack(pady=20)




    def generate_resume(self):
        job_description = self.job_description_input.get("1.0", "end-1c").strip()
        if not job_description:
            messagebox.showwarning("Input Error", "Please enter a job description.")
            return
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer."},
                    {"role": "user", "content": f"Create a professional resume based on the following job description:\n\n{job_description}"}
                ]
            )
            generated_resume = response["choices"][0]["message"]["content"].strip()
            self.resume_output.delete("1.0", "end")
            self.resume_output.insert("1.0", generated_resume)
        except Exception as e:
            messagebox.showerror("API Error", f"An error occurred: {e}")

    def save_resume(self):
        resume_content = self.resume_output.get("1.0", "end-1c").strip()
        if not resume_content:
            messagebox.showwarning("Save Error", "No resume content to save.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(resume_content)
            messagebox.showinfo("Success", f"Resume saved to {file_path}")

    def clear_all(self):
        self.job_description_input.delete("1.0", "end")
        self.resume_output.delete("1.0", "end")