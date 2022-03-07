import numpy as np
import vtk
import wx
from pubsub import pub as Publisher
from six import with_metaclass

from invesalius.data import styles

from . import gui

class GenSpheresStyle(styles.DefaultInteractorStyle):
    gui = None
    def __init__(self, viewer):
        super().__init__(viewer)

        self.picker = vtk.vtkWorldPointPicker()

        self.AddObserver("LeftButtonPressEvent", self.OnPressLeftButtonGenSphere)

    def SetUp(self):
        print("SetUP")
        if self.gui is None:
            self.create_gui()

    def CleanUp(self):
        print("CleanUp")
        if self.gui is not None:
            self.destroy_gui()

    def OnPressLeftButtonGenSphere(self, obj, evt):
        mouse_x, mouse_y = self.GetMousePosition()
        x, y, z = self.viewer.get_voxel_coord_by_screen_pos(mouse_x, mouse_y, self.picker)
        r = self.gui.spin_radius.GetValue()
        image = self.viewer.slice_.matrix
        mask = self.viewer.slice_.current_mask
        dz, dy, dx = image.shape
        if 0 <= x < dx and 0 <= y < dy and 0 <= z < dz:
            iz, iy, ix = np.ogrid[0: dz, 0: dy, 0:dx]
            sphere = ((iz - z)**2 + (iy - y)**2 + (ix - x)**2) <= r**2
            mask.matrix[0] = 1
            mask.matrix[:, 0, :] = 1
            mask.matrix[:, :, 0] = 1
            mask.matrix[1:, 1:, 1:][sphere] = 254
            mask.was_edited = True
            mask.modified()
            mask.clear_history()
            self.viewer.discard_mask_cache(all_orientations=True, vtk_cache=True)
            Publisher.sendMessage('Reload actual slice')


    @classmethod
    def create_gui(cls):
        if cls.gui is None:
            top_window = wx.GetApp().GetTopWindow()
            cls.gui = gui.GenSpheresGUI(top_window)
            cls.gui.Show()

    @classmethod
    def destroy_gui(cls):
        if cls.gui is not None:
            cls.gui.Destroy()
            cls.gui = None
