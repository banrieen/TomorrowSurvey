# -*- coding: utf-8 -*-


"""
   System doctor
"""

import wx

class Phonix(wx.Frame):
    def __init__(self,*args,**kw):
        super(Phonix,self).__init__(*args,**kw)
        pnl = wx.Panel(self)
        st = wx.StaticText(pnl,label="Phonix",pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        
        # Creat a menu bar
        self.makeMenuBar()
        
        # Create status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to phnix debuger")

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)


    def main(self): 
        #main_frame = wx.Frame(None, -1, "wxPython - App debuger", pos = (10,10), size = (300,200), style = wxDEFAULT_FRAME_STYLE, name = "frame") 
        main_frame = wx.Frame(None, -1, "wxPython - App debuger") 

        panel = wx.Panel(main_frame) 
        label = wx.StaticText(panel, label = "Phonix", pos = (100,100)) 
        
        main_frameindow.Show(True) 
        return True
        #app.MainLoop() 



if __name__ == "__main__":
    app = wx.App()
    frm = Phonix(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()

