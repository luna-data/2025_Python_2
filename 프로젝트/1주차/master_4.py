import tkinter as tk
# 문제 2: 할 일 관리 앱 만들기
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("할 일 관리")
        self.todos = []
        self.completed = []
        
        # 입력 영역
        frame_input = tk.Frame(root)
        frame_input.pack(pady=10)
        
        self.entry = tk.Entry(frame_input, width=30, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, padx=5)
        
        btn_add = tk.Button(frame_input, text="추가", command=self.add_todo)
        btn_add.pack(side=tk.LEFT, padx=5)
        
        # 목록 영역
        frame_list = tk.Frame(root)
        frame_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(frame_list, text="할 일 목록", font=("Arial", 14, "bold")).pack()
        
        self.listbox = tk.Listbox(frame_list, width=50, height=15, font=("Arial", 11))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # 버튼 영역
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)
        
        btn_complete = tk.Button(frame_buttons, text="완료", command=self.complete_todo)
        btn_complete.pack(side=tk.LEFT, padx=5)
        
        btn_delete = tk.Button(frame_buttons, text="삭제", command=self.delete_todo)
        btn_delete.pack(side=tk.LEFT, padx=5)
    
    def add_todo(self):
        todo = self.entry.get()
        if todo:
            self.todos.append(todo)
            self.update_listbox()
            self.entry.delete(0, tk.END)
    
    def complete_todo(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.todos):
                completed = self.todos.pop(index)
                self.completed.append(completed)
                self.update_listbox()
    
    def delete_todo(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.todos):
                self.todos.pop(index)
                self.update_listbox()
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, todo in enumerate(self.todos):
            self.listbox.insert(tk.END, f"[ ] {todo}")
        for todo in self.completed:
            self.listbox.insert(tk.END, f"[✓] {todo}")

root=tk.Tk()
TodoApp(root)
root.mainloop()