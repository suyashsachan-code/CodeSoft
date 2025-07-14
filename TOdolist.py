import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("500x500")
        self.root.configure(bg="#d0f0fd")  # light sky blue background
        self.tasks = []

        # Heading
        self.heading = tk.Label(root, text="📝 To-Do List", font=("Helvetica", 18, "bold"), bg="#d0f0fd", fg="#034078")
        self.heading.pack(pady=10)

        # Entry Frame
        entry_frame = tk.Frame(root, bg="white", padx=10, pady=10, bd=2, relief="groove")
        entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(entry_frame, width=35, font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_button = tk.Button(entry_frame, text="Add Task", width=10, bg="#4CAF50", fg="white", activebackground="#45a049", command=self.add_task)
        self.add_button.grid(row=0, column=1)

        # Listbox Frame
        list_frame = tk.Frame(root, bg="white", padx=10, pady=10, bd=2, relief="groove")
        list_frame.pack(pady=10, fill="both", expand=True)

        self.task_listbox = tk.Listbox(list_frame, width=50, height=10, font=("Helvetica", 12), selectbackground="#a2d2ff", selectforeground="black", bg="white", activestyle="none")
        self.task_listbox.pack(pady=5)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#d0f0fd")
        button_frame.pack(pady=5)

        self.mark_done_button = tk.Button(button_frame, text="✔ Mark as Done", width=15, bg="#2196F3", fg="white", activebackground="#1e88e5", command=self.mark_done)
        self.mark_done_button.grid(row=0, column=0, padx=10)

        self.delete_button = tk.Button(button_frame, text="🗑 Delete Task", width=15, bg="#f44336", fg="white", activebackground="#e53935", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=10)

        self.update_listbox()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✅ Done" if task["done"] else "❌ Not Done"
            self.task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["done"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
