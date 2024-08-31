from tkinter.ttk import Button
from typing import Literal
from customtitlebar import CTT
from asset.sv_ttk import set_theme
from tktermwidget import Terminal

from widget import CTTNotebook, CTTNotebookFrame


class TerminalWindow(CTT):
    def __init__(self, theme: Literal["light", "dark", "auto"] = "auto") -> None:
        super().__init__(theme)

        self.value = 0

        self.geometry("975x525")
        self.titlebarconfig(height=40)

        set_theme(self.theme)

        self.nb = CTTNotebook(self.titlebar)
        self.addtab = Button(self.titlebar, text=u'\uE109', command=self.newtab)
        self.moreop = Button(self.titlebar, text=u'\uE015')
        self.nb.pack(side="left", fill="x", padx=7)
        self.addtab.pack(side="left", fill="y", padx=3, pady=5)
        self.moreop.pack(side="left", fill="y", pady=5)

        self.mainloop()

    def newtab(self):
        if self.value == 11:
            return
        else:
            test = CTTNotebookFrame(self)
            terminal = Terminal(test.show)
            terminal.pack(fill="both", expand=True)
            test.show.pack(fill="both", expand=True)
            self.nb.add_tab(test.dummy, test.show, text="term %d" % self.value)
            self.value += 1

test = TerminalWindow()
test.mainloop()
