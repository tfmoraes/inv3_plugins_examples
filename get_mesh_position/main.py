import wx
from pubsub import pub as Publisher

from invesalius.data import styles_3d

from . import pixel_value_style

def load():
    style_id = styles_3d.Styles.add_style(pixel_value_style.PixelValueStyle, 2)
    print(f"Style: {style_id}")

    Publisher.sendMessage("Disable actual style")
    Publisher.sendMessage("Enable style", style=style_id)
