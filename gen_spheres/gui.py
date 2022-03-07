import wx
from pubsub import pub as Publisher


class GenSpheresGUI(wx.Dialog):
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
        self.spin_radius = wx.SpinCtrl(self, -1, value="5", min=1, max=100)
        btn_close = wx.Button(self, wx.ID_CLOSE)

        btn_close.Bind(wx.EVT_BUTTON, self.OnClickClose)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.spin_radius, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn_close, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def OnClickClose(self, evt):
        self.Close()

    def OnClose(self, evt):
        Publisher.sendMessage("Disable actual style")
        self.Destroy()
