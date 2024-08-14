import os
import tkinter as tk
from tkinter import messagebox

class ExtensionManager:
    def __init__(self):
        self.commands = {
            "js": {
                "add": "reg add HKCR\\.js\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.js\\ShellNew /f"
            },
            "html": {
                "add": "reg add HKCR\\.html\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.html\\ShellNew /f"
            },
            "bat": {
                "add": "reg add HKCR\\.bat\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.bat\\ShellNew /f"
            },
            "vbs": {
                "add": "reg add HKCR\\.vbs\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.vbs\\ShellNew /f"
            },
            "reg": {
                "add": "reg add HKCR\\.reg\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.reg\\ShellNew /f"
            },
            "py": {
                "add": "reg add HKCR\\.py\\ShellNew /v NullFile /t REG_SZ /d 1 /f",
                "del": "reg delete HKCR\\.py\\ShellNew /f"
            }
        }

    def execute_command(self, extension, action):
        command = self.commands.get(extension, {}).get(action)
        if command:
            os.system(command)

    def execute_all(self, action):
        for ext in self.commands.keys():
            self.execute_command(ext, action)
        action_word = "добавлены" if action == "add" else "убраны"
        messagebox.showinfo("Успех", f"Все расширения успешно {action_word}.")

class Application(tk.Tk):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.title("Управление расширениями файлов")
        self.extensions = self.manager.commands.keys()
        self.create_widgets()

    def create_widgets(self):
        for ext in self.extensions:
            frame = tk.Frame(self)
            frame.pack(pady=5)

            label = tk.Label(frame, text=f"{ext} файл:")
            label.pack(side=tk.LEFT)

            add_button = tk.Button(frame, text="Добавить", command=lambda e=ext: self.manager.execute_command(e, "add"))
            add_button.pack(side=tk.LEFT)

            del_button = tk.Button(frame, text="Убрать", command=lambda e=ext: self.manager.execute_command(e, "del"))
            del_button.pack(side=tk.LEFT)

        # Кнопка "Добавить всё"
        add_all_button = tk.Button(self, text="Добавить всё", command=lambda: self.manager.execute_all("add"))
        add_all_button.pack(pady=5)

        # Кнопка "Убрать всё"
        del_all_button = tk.Button(self, text="Убрать всё", command=lambda: self.manager.execute_all("del"))
        del_all_button.pack(pady=5)


if __name__ == "__main__":
    manager = ExtensionManager()
    app = Application(manager)
    app.mainloop()
