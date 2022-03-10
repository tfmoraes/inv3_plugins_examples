import numpy as np
import vtk
import wx
from pubsub import pub as Publisher
from six import with_metaclass


from invesalius.data import styles_3d

from . import gui

class PixelValueStyle(styles_3d.DefaultInteractorStyle):
    gui = None
    def __init__(self, viewer):
        super().__init__(viewer)

        self.picker = vtk.vtkPropPicker()

        self.AddObserver("MouseMoveEvent", self.OnMouseMovePixel)

    def SetUp(self):
        print("SetUP")
        if self.gui is None:
            self.create_gui()

    def CleanUp(self):
        print("CleanUp")
        if self.gui is not None:
            self.destroy_gui()

    def OnMouseMovePixel(self, obj, evt):
        x, y = self.viewer.get_vtk_mouse_position()
        self.picker.Pick(x, y, 0, self.viewer.ren)
        x, y, z = self.picker.GetPickPosition()
        if self.picker.GetActor():
            print(x, y, z)

    @classmethod
    def create_gui(cls):
        if cls.gui is None:
            top_window = wx.GetApp().GetTopWindow()
            cls.gui = gui.PixelValueGUI(top_window)
            cls.gui.Show()

    @classmethod
    def destroy_gui(cls):
        if cls.gui is not None:
            cls.gui.Destroy()
            cls.gui = None
