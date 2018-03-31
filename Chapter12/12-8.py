def print_mro(cls):
	print(', '.join(c.__name__ for c in cls.__mro__))

import tkinter
print_mro(tkinter.Toplevel)
print_mro(tkinter.Widget)
print_mro(tkinter.Button)
print_mro(tkinter.Entry)
print_mro(tkinter.Text)