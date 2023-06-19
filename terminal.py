""""A Terminal Window"""
from tkinter.ttk import Button, Frame, Notebook

from CustomTkinterTitlebar import CTT, Image, ImageTk
from darkdetect import isDark
from sv_ttk import set_theme
from tktermwidget import *


class TerminalWindow(CTT):
    """A Terminal Window"""

    def __init__(
        self,
    ):
        super().__init__()

        self.usetitle(False)
        self.useicon(False)
        # self.useblur(True)
        self.titlebarconfig(
            color={"color": "#2B2B2B", "color_nf": "#2f2f2f"}, height=40
        )
        self.geometry("1000x515")

        self.notebook = Notebook(self.titlebar)
        newtab_load = Image.open("newtab.png")
        newtab_png = ImageTk.PhotoImage(newtab_load)
        self.newtab = Button(self.titlebar, image=newtab_png, command=self.newtab)
        self.term = Terminal(self)

        self.term.pack(expand=True, fill="both")
        self.notebook.pack(side="left", fill="x")
        self.newtab.pack(side="left", fill="y", padx=3, pady=3)

    def newtab(self):
        newframe = Frame(self.notebook)
        newframe.pack(fill="x", side="top")
        self.notebook.add(newframe, text="New Tab")


if __name__ == "__main__":
    example = TerminalWindow()
    if isDark():
        set_theme("dark")
    else:
        set_theme("light")
    example.mainloop()
