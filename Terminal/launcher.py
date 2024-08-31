from tkinter.ttk import Button
from customtitlebar import CTT
from PIL import Image, ImageTk
from sv_ttk import set_theme
from tktermwidget import Terminal

from widget import CTTNotebook, CTTNotebookFrame

import pathlib

value = 0

def newtab():
    global value

    if value == 11:
        return
    else:
        test = CTTNotebookFrame(ex)
        terminal = Terminal(test.show)
        terminal.pack(fill="both", expand=True)
        test.show.pack(fill="both", expand=True)
        nb.add_tab(test.dummy, test.show, text="term %d" % value)
        value += 1


ex = CTT()
ex.geometry("975x525")
ex.titlebarconfig(height=40)
ex.bg = "#2f2f2f"
ex.setcolor()

set_theme(ex.theme)

path = pathlib.Path(__file__).parent / "asset"

newtab_load = Image.open(path / "newtab.png").resize((16, 16))
newtab_png = ImageTk.PhotoImage(newtab_load)
newtab = Button(ex.titlebar, image=newtab_png, command=newtab)
nb = CTTNotebook(ex.titlebar)
nb.pack(side="left", fill="x", padx = 7)
newtab.pack(side="left", fill="y", padx=3, pady=3)
ex.mainloop()
