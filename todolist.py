import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create GUI components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

        # Set up event handling
        self.task_listbox.bind("<Double-Button-1>", self.edit_task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f'Task "{task}" added successfully!')
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            removed_task = self.tasks.pop(selected_task_index[0])
            self.update_task_list()
            messagebox.showinfo("Task Removed", f'Task "{removed_task}" removed successfully!')

    def edit_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks[selected_task_index[0]]
            edited_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task)
            if edited_task:
                self.tasks[selected_task_index[0]] = edited_task
                self.update_task_list()
                messagebox.showinfo("Task Edited", f'Task edited successfully!')

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
        self.task_listbox.update_idletasks()  # Add this line to update the listbox immediately

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()



'''#second method without using the GUI tkinter
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def mark_done(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            print(f'Task "{task}" marked as done.')
            self.tasks.pop(task_index - 1)
        except IndexError:
            print('Invalid task index.')

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as done: "))
            todo_list.mark_done(task_index)
        elif choice == '4':
            print('Exiting the To-Do List application. Goodbye!')
            break
        else:
            print('Invalid choice. Please choose a valid option.')

if __name__ == "__main__":
    main()

'''