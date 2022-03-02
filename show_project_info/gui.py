import wx

from invesalius.project import Project
from invesalius.data.slice_ import Slice

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
        prj = Project()
        slc = Slice()

        lbl_name = wx.StaticText(self, -1, f"Nome do projeto: {prj.name}")
        lbl_image_size = wx.StaticText(self, -1, f"Tamanho da imagem: {slc.matrix.shape}")
        lbl_image_min_max = wx.StaticText(self, -1, f"Menor e maior valor: {slc.matrix.min()}, {slc.matrix.max()}")
        lbl_number_masks = wx.StaticText(self, -1, f"Número de máscaras: {len(prj.mask_dict)}")

        btn_close = wx.Button(self, wx.ID_CLOSE)

        btn_close.Bind(wx.EVT_BUTTON, self.OnClickClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl_name, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(lbl_image_size, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(lbl_image_min_max, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(lbl_number_masks, 0, wx.EXPAND | wx.ALL, 5)
        sizer.Add(btn_close, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()

    def OnClickClose(self, evt):
        self.Close()
