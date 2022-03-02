import wx
from . import gui

def load():
    top_window = wx.GetApp().GetTopWindow()
    window = gui.HelloWorldGUI(top_window)
    window.ShowModal()
    window.Destroy()
