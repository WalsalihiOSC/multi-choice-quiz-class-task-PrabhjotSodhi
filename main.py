import tkinter as tk

class MultiChoiceGUI:
    def __init__(self, frame):
        self.frame = frame
    def display(self):
        tk.Label(self.frame, text="Question:").pack()
        tk.Label(self.frame, text="What is the Capital of the World?:").pack()
        self.check_label = tk.Label(self.frame, text=" ")
        for (text, value) in backend.get_options():
            tk.Radiobutton(self.frame, text=text, variable=backend.get_selection(), value=value, command=lambda: backend.check_answer(backend.get_selection(), self.check_label)).pack()
        self.check_label.pack()

class MultiChoiceClass:
    def __init__(self, frame):
        self.selection = tk.IntVar(frame)
        self.selection.set(1)
        self.options = {"Vladivostok": 1,"Astana": 2,"Ulan Bator": 3,"Lhasa": 4}
    def check_answer(self, selection, label):
        if selection.get() == 3:
            label['text']="Correct!"
        else:
            label['text']="Incorrect!"
    def get_options(self):
        return self.options.items()
    def get_selection(self):
        return self.selection
        
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x300')
    root.title("Multi Choice Quiz")
    main_frame = tk.Frame(root)
    main_frame.pack()
    backend = MultiChoiceClass(main_frame)
    MultiChoiceGUI(main_frame).display()
    root.mainloop()