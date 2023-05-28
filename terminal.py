""""A Terminal Window"""
from CustomTkinterTitlebar import CTT
from sv_ttk import set_theme
from tktermwidget import *
from darkdetect import isDark

class TerminalWindow(CTT):
	"""A Terminal Window"""
	def __init__(self, ):
		super().__init__()
		
		self.usetitle(False)
		self.useicon(False)
		self.useblur(True)
		self.titlebarconfig(color={"color": "#2B2B2B", "color_nf": "#2f2f2f"}, height=40)
		self.geometry("1000x515")
		
		self.term = Terminal(self)
		self.term.pack(expand = True, fill = "both")
		
if __name__ == "__main__":
	example = TerminalWindow()
	if isDark():
		set_theme("dark")
	else:
		set_theme("light")
	example.mainloop()