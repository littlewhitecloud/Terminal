from tkinter.ttk import Notebook
from tkinter import Frame, Event

class CTTNotebookFrame():
    def __init__(self, master) -> None:
        self.dummy = Frame(master)
        self.show = Frame(master)

class CTTNotebook(Notebook):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.childs = []
        self.current = None

        self.bind("<<NotebookTabChanged>>", self.update_tab)

    def add_tab(self, dummy, child, text):
        self.childs.append(child)

        if self.current:
            self.current.pack_forget()

        self.current = child
        self.add(child = dummy, text = text)

    def update_tab(self, event: Event):
        index = event.widget.tab(event.widget.select(), "text")
        self.current.pack_forget()
        self.current = self.childs[int(index.split(" ")[-1])]
        self.current.pack(fill="both", expand=True)

