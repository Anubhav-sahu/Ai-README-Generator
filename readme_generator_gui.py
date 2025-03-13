import openai
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Fetch OpenAI API key( I am using openapi, you can use others as well)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_readme():
    project_name = project_name_entry.get()
    description = description_entry.get("1.0", tk.END).strip()
    tech_stack = tech_stack_entry.get()

    if not project_name or not description or not tech_stack:
        messagebox.showerror("Error", "Please fill all fields")
        return

    prompt = f"""
    Generate a README.md for a GitHub project with:
    - Project Name: {project_name}
    - Description: {description}
    - Tech Stack: {tech_stack}
    - Include installation, usage, and contribution guidelines.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        readme_content = response["choices"][0]["message"]["content"]
        
        with open("README.md", "w") as f:
            f.write(readme_content)
        
        readme_display.delete("1.0", tk.END)
        readme_display.insert(tk.END, readme_content)
        messagebox.showinfo("Success", "README.md generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate README: {e}")

# GUI setup ( using tkinter, you can use flask or streamlit as well)
root = tk.Tk()
root.title("AI-Powered README Generator")
root.geometry("600x500")

tk.Label(root, text="Project Name:").pack()
project_name_entry = tk.Entry(root, width=50)
project_name_entry.pack()

tk.Label(root, text="Description:").pack()
description_entry = scrolledtext.ScrolledText(root, width=50, height=5)
description_entry.pack()

tk.Label(root, text="Tech Stack (comma-separated):").pack()
tech_stack_entry = tk.Entry(root, width=50)
tech_stack_entry.pack()

generate_button = tk.Button(root, text="Generate README", command=generate_readme)
generate_button.pack(pady=10)

tk.Label(root, text="Generated README:").pack()
readme_display = scrolledtext.ScrolledText(root, width=70, height=10)
readme_display.pack()

root.mainloop()
