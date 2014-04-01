#!/usr/bin/python

from Tkinter import Tk, Frame, Label, Button, OptionMenu, StringVar, Entry
import os

OsVars = {
    'FLASH_FULL': 'false',
    'FLASH_GAIA': 'false',
    'FLASH_GECKO': 'false',
    'FLASH_FULL_IMG_FILE': "",
    'FLASH_GAIA_FILE': "",
    'FLASH_GECKO_FILE': "",
    'TARGET_ID': '-1',
    'FLASH_USR_IF_POSSIBLE': 'false',
    'FLASH_ENG_IF_POSSIBLE': 'false',
    'FLASH_USER_ENG_DONE': 'false',
    'HTTP_USER': '',
    'HTTP_PWD': ''
    }


def getOsVars(keys=[]):
    ret = {}
    for k in keys:
        if k in os.environ:
            ret[k] = os.environ[k]
    return ret


def setOsVars(varList={}):
    for k, v in varList:
        os.environ[k] = v


OsVars = getOsVars(OsVars.keys())
TITLE_FONT = ("Helvetica", 18, "bold")


class BasePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.controller = controller

    def setName(self, value):
        self.name = value

    def setIndex(self, value):
        self.index = value

    def setupView(self):
        raise NotImplementedError


class SelectPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

    def setupView(self, title="Test Select Page", item_list=[], default=0):
        self.desc = Label(self, text=title, font=TITLE_FONT)
        self.desc.grid(row=0, column=0, columnspan=2)
        self.optVar = StringVar()
        self.selection = OptionMenu(self, self.optVar, *item_list)
        self.selection.grid(row=1, column=0, columnspan=2, sticky="WE")
        self.optVar.set(item_list[default])
        self.ok = Button(self,
                         text='Next',
                         command=lambda: self.controller.transition(self))
        self.ok.grid(row=2, column=1, sticky="W")
        self.cancel = Button(self,
                             text='Cancel',
                             command=lambda: self.controller.quit())
        self.cancel.grid(row=2, column=0, sticky="E")


class AuthPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

    def setupView(self, title="Test Auth Page", user='', pwd_ori=''):
        userVar = StringVar()
        pwdVar = StringVar()
        userInput = Entry(self,
                          textvariable=userVar,
                          width="30").grid(row=0,
                                           columnspan=2,
                                           sticky="WE")
        pwdInput = Entry(self,
                         textvariable=pwdVar,
                         show="*",
                         width="30").grid(row=1,
                                          columnspan=2,
                                          sticky="WE")
        userVar.set(user)
        pwdVar.set(pwd_ori)
        self.ok = Button(self,
                         text='Next',
                         command=lambda: self.
                         controller.setAuth(self,
                                            userInput.get(),
                                            pwdInput.get()))
        self.ok.grid(row=2, column=1, sticky="W")
        self.cancel = Button(self,
                             text='Cancel',
                             command=lambda: self.controller.quit())
        self.cancel.grid(row=2, column=0, sticky="E")


class buildIdPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

    def setupView(self, title="Test BuildId Page", buildId=''):
        buildIdInput = Entry(self,
                             width="40").grid(row=1,
                                              columnspan=2,
                                              sticky="WE")
        self.ok = Button(self,
                         text='Next',
                         command=lambda: self.
                         controller.setValue(self,
                                             "BUILD_ID",
                                             buildIdInput.get()
                                             )
                         )
        self.ok.grid(row=2, column=1, sticky="W")
        self.cancel = Button(self,
                             text='Cancel',
                             command=lambda: self.controller.quit())
        self.cancel.grid(row=2, column=0, sticky="E")


class ConfirmPage(BasePage):
    def __init__(self, parent, controller):
        BasePage.__init__(self, parent, controller)

    def setupView(self, title="Test Confirm Page"):
        self.ok = Button(self,
                         text='Done',
                         command=lambda: self.controller.flash(self))
        self.ok.grid(row=2, column=1, sticky="W")
        self.cancel = Button(self,
                             text='Cancel',
                             command=lambda: self.controller.quit())
        self.cancel.grid(row=2, column=0, sticky="E")


class FlashApp():
    def __init__(self, *args, **kwargs):
        '''
        Generate base frame and each page, bind them in a list
        '''
        self.flashOpts = getOsVars()

        self.root = Tk()
        self.frames = []
        container = Frame(master=self.root)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack(side="top", fill="x", expand=False)

        devicePage = SelectPage(parent=container, controller=self)
        devicePage.setupView("Select device", ["buri", "leo", "nexus4"])
        versionPage = SelectPage(parent=container, controller=self)
        versionPage.setupView("Select version",
                              [
                                  "master",
                                  "aurora",
                                  "1.2",
                                  "1.3",
                                  "1.4"
                                  ])
        engineerPage = SelectPage(parent=container, controller=self)
        engineerPage.setupView("Select type", ["user", "engineering"])
        packagePage = SelectPage(parent=container, controller=self)
        packagePage.setupView("Select package",
                              [
                                  "Gecko/gaia",
                                  "Gecko",
                                  "gaia",
                                  "full flash"
                                  ])
        authPage = AuthPage(parent=container, controller=self)
        authPage.setupView("Account Info",
                           OsVars.get('HTTP_USER', ''),
                           OsVars.get('HTTP_PWD', ''))

        self.frames = [
            devicePage,
            versionPage,
            engineerPage,
            packagePage,
            authPage,
            ]
        for idx, val in enumerate(self.frames):
            val.index = idx
            val.grid(row=0, column=0, sticky="nsew")
        self.transition()
        self.container = container

    def setAuth(self, page, user, pwd):
        OsVars['HTTP_USER'] = user.get()
        OsVars['HTTP_PWD'] = pwd.get()
        self.transition(page)

    def setPackage(self, page, optVar):
        package = optVar.get()
        if 'Gecko' in package:
            OsVars['FLASH_GECKO'] = "true"
        if 'gaia' in package:
            OsVars['FLASH_GAIA'] = "true"
        if 'full' in package:
            OsVars['FLASH_FULL'] = "true"
        self.transition(page)

    def setValue(self, page, key, optVar):
        OsVars[key] = optVar.get()
        self.transition(page)

    def transition(self, page=None):
        if page is None:
            self.frames[0].lift()
        elif page.index < len(self.frames) - 1:
            self.frames[page.index + 1].lift()

    def quit(self):
        '''
        Halt the program
        '''
        pass

    def doFlash(self):
        setOsVars(OsVars)
        #TODO: run flash here
        self.quit()


if __name__ == '__main__':
    app = FlashApp().container
    from sys import platform as _platform
    if _platform == 'darwin':
        os.system("/usr/bin/osascript -e \'tell app \"Find\
er\" to set frontmost of process \"Pyt\
hon\" to true\'")
    app.mainloop()
