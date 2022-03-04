import wx
from pubsub import pub as Publisher


class PixelValueGUI(wx.Dialog):
    def __init__(
        self,
        parent,
        title="Hello World GUI",
        style=wx.DEFAULT_DIALOG_STYLE | wx.FRAME_FLOAT_ON_PARENT | wx.STAY_ON_TOP,
    ):
        super().__init__(parent, -1, title=title, style=style)
        self.pixel_value = 0
        self._init_gui()

    def _init_gui(self):
        self.lbl_pixel_value = wx.StaticText(self, -1, f"Value: {self.pixel_value}.")
        btn_close = wx.Button(self, wx.ID_CLOSE)

        btn_close.Bind(wx.EVT_BUTTON, self.OnClickClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbl_pixel_value, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn_close, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def OnClickClose(self, evt):
        self.Close()

    def OnClose(self, evt):
        Publisher.sendMessage("Disable actual style")
        self.Destroy()

    def set_pixel_value(self, pixel_value):
        self.pixel_value = pixel_value
        self.lbl_pixel_value.SetLabel(f"Value: {self.pixel_value}.")
