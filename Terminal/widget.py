from tkinter import Event, Frame
from tkinter.ttk import Notebook
from typing import Any


class CTTNotebookFrame:
    def __init__(self, master: Any) -> None:
        self.dummy = Frame(master)
        self.show = Frame(master)


class CTTNotebook(Notebook):
    def __init__(self, master: Any) -> None:
        super().__init__(master)

        self.children = []
        self.current = None

        self.bind("<<NotebookTabChanged>>", self.update_tab)

    def add_tab(self, dummy: Frame, child: Frame, text: str) -> None:
        self.children.append(child)

        if self.current:
            self.current.pack_forget()

        self.current = child
        self.add(child=dummy, text=text)

    def update_tab(self, event: Event) -> None:
        index = event.widget.tab(event.widget.select(), "text")
        self.current.pack_forget()
        self.current = self.children[int(index.split(" ")[-1])]
        self.current.pack(fill="both", expand=True)
