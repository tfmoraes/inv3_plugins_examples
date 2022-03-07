import wx
from pubsub import pub as Publisher

from invesalius.data import styles

from . import gen_spheres_style

def load():
    style_id = styles.Styles.add_style(gen_spheres_style.GenSpheresStyle, 2)
    print(f"Style: {style_id}")

    Publisher.sendMessage("Disable actual style")
    Publisher.sendMessage("Enable style", style=style_id)
