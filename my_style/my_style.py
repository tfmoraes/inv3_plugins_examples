from invesalius.data import styles


# `Base3DInteractorStyle` ou `DefaultInteractorStyle`
class MyStyle(styles.BaseImageInteractorStyle):
    def __init__(self, viewer):
        super().__init__(viewer)
        self.AddObserver("LeftButtonPressEvent", self.OnMouseLeftPress)
    def OnMouseLeftPress(self, obj, evt):
        print(obj, evt)
