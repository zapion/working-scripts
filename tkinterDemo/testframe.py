#!/usr/bin/python

from Tkinter import *
import ttk
import os

class testframe(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.selectControl()

    def selectControl(self):
        self.desc = Label(self)
        self.desc["text"] = 'test'
        self.desc.grid(row=0, column=0, columnspan=2)
        self.selection = ttk.Combobox(self)
        self.selection.grid(row=1, column=0, columnspan=2)
        self.ok = Button(self)
        self.ok['text'] = 'Next'
        self.ok.grid(row=2, column=1, sticky=W)
        self.cancel = Button(self)
        self.cancel['text'] = 'Cancel'
        self.cancel.grid(row=2, column=0, sticky=E)

    def confirmControl(self):
        pass
if __name__ == '__main__':
    root = Tk()
    app = testframe(master=root)
    from sys import platform as _platform
    if _platform == 'darwin':
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    else:
        root.lift()
    app.mainloop()
