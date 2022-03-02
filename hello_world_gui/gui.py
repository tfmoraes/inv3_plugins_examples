import wx

class HelloWorldGUI(wx.Dialog):
    def __init__(
        self,
        parent,
        title="Hello World GUI",
        style=wx.DEFAULT_DIALOG_STYLE | wx.FRAME_FLOAT_ON_PARENT | wx.STAY_ON_TOP,
    ):
        super().__init__(parent, -1, title=title, style=style)
        self._init_gui()

    def _init_gui(self):
        lbl_hello = wx.StaticText(self, -1, "Hello, world!")
        btn_close = wx.Button(self, wx.ID_CLOSE)

        btn_close.Bind(wx.EVT_BUTTON, self.OnClickClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_hello, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn_close, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def OnClickClose(self, evt):
        self.Close()
