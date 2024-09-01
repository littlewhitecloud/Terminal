from ctypes import windll
from tkinter import Toplevel
from tkinter.ttk import Button
from typing import Literal
from tkinter import PhotoImage

from asset.sv_ttk import set_theme
from constant import GWL_STYLE, WS_THICKFRAME, WS_VISIBLE
from customtitlebar import CTT
from tktermwidget import Terminal
from utils import ExtendFrameIntoClientArea
from widget import CTTNotebook, CTTNotebookFrame
from win32material import ApplyMica


class MenuWindow(Toplevel):
    def __init__(self) -> None:
        super().__init__()

        self.title("menuwindow")
        self.iconbitmap("")
        self.hwnd = windll.user32.GetParent(self.winfo_id())
        windll.user32.SetWindowLongW(self.hwnd, GWL_STYLE, WS_VISIBLE | WS_THICKFRAME)

        self.geometry("225x400")

        self.update()


class TerminalWindow(CTT):
    def __init__(self, theme: Literal["light", "dark", "auto"] = "auto") -> None:
        super().__init__(theme)

        self.title("Terminal")
        self.geometry("975x525")
        self.titlebarconfig(height=40)
        self.infogroup.pack_forget()

        self.value = 0

        set_theme(self.theme)

        if self.theme == "dark":
            ApplyMica(self.hwnd, True)
            ExtendFrameIntoClientArea(self.hwnd, 0, 0, 40, 0)

        self.popupmenu = MenuWindow()
        self.notebook = CTTNotebook(self.titlebar)
        self.addtab = Button(self.titlebar, text="\uE109", command=self.newtab)
        self.moreop = Button(self.titlebar, text="\uE015", command=self.showmenu)
        self.notebook.pack(side="left", fill="x")
        self.addtab.pack(side="left", fill="y", padx=3, pady=5)
        self.moreop.pack(side="left", fill="y", pady=5)

        self.popupmenu.withdraw()

        self.popupmenu.bind("<FocusOut>", self.hidemenu)

        self.newtab()

    def newtab(self) -> None:
        terminalframe = CTTNotebookFrame(self)
        terminal = Terminal(terminalframe.show)
        terminal.pack(fill="both", expand=True)
        terminalframe.show.pack(fill="both", expand=True)
        self.notebook.add_tab(
            terminalframe.dummy, terminalframe.show, text="Terminal %d" % self.value
        )

        self.value += 1

    def showmenu(self) -> None:
        self.popupmenu.geometry(f"+{self.winfo_pointerx()}+{self.winfo_pointery()}")
        self.popupmenu.deiconify()
        self.popupmenu.focus_force()

    def hidemenu(self, _) -> None:
        self.popupmenu.withdraw()


test = TerminalWindow()
test.mainloop()
