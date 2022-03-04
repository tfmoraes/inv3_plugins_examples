import numpy as np
import vtk
import wx
from pubsub import pub as Publisher
from six import with_metaclass

from invesalius.data import styles

from . import gui

class PixelValueStyle(styles.BaseImageInteractorStyle):
    gui = None
    def __init__(self, viewer):
        super().__init__(viewer)

        self.picker = vtk.vtkWorldPointPicker()

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
        mouse_x, mouse_y = self.GetMousePosition()
        x, y, z = self.viewer.get_voxel_coord_by_screen_pos(mouse_x, mouse_y, self.picker)
        image = self.viewer.slice_.matrix
        dz, dy, dx = image.shape
        if 0 <= x < dx and 0 <= y < dy and 0 <= z < dz:
            value = image[z, y, x]
            self.gui.set_pixel_value(value)
        else:
            self.gui.set_pixel_value(None)

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
