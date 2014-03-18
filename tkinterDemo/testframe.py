#!/usr/bin/python

from Tkinter import Tk, Frame, Label, Button, W, E
import ttk
import os


def getOsVars(keys=[]):
    ret = {}
    for k in keys:
        ret[k] = os.environ[k]
    return ret


def setOsVars(varList={}):
    for k, v in varList:
        os.environ[k] = v


TITLE_FONT = ("Helvetica", 18, "bold")


class SelectPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.controller = controller
        self.index = -1

    def setIndex(self, value):
        self.index = value

    def selectControl(self, title="Test", item_list={}):
        self.desc = Label(self, text=title, font=TITLE_FONT)
        self.desc.grid(row=0, column=0, columnspan=2)
        self.selection = ttk.Combobox(self, values=item_list)
        self.selection.grid(row=1, column=0, columnspan=2)
        self.ok = Button(self,
                         text='Next',
                         command=self.controller.transition(self))
        self.ok.grid(row=2, column=1, sticky=W)
        self.cancel = Button(self,
                             text='Cancel',
                             command=self.controller.transition(self))
        self.cancel.grid(row=2, column=0, sticky=E)

    def confirmControl(self):
        pass


class ConfirmPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.controller = controller

    def listDown():
        pass

    def doFlash():
        pass


class FlashApp(Tk):
    def __init__(self, *args, **kwargs):
        '''
        Generate base frame and each page, bind them in a list
        '''
        container = Frame(master=self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        devicePage = SelectPage(parent=container, controller=self)
        versionPage = SelectPage(parent=container, controller=self)
        engineerPage = SelectPage(parent=container, controller=self)
        packagePage = SelectPage(parent=container, controller=self)
        self.frames = [devicePage,
                       versionPage,
                       engineerPage,
                       packagePage]
        for idx, val in self.frame:
            val.index = idx

    def transition(self, page):
        if page.index < len(self.frames):
            self.frames[page.index + 1].tkraise()

    def quit():
        '''
        Halt the program
        '''
        pass


if __name__ == '__main__':
    app = FlashApp()
    from sys import platform as _platform
    if _platform == 'darwin':
        os.system("/usr/bin/osascript -e \'tell app \"Find\
er\" to set frontmost of process \"Pyt\
hon\" to true\'")
    else:
        app.lift()
    app.mainloop()
