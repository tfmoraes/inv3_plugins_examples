import wx
from invesalius.data import styles
from pubsub import pub as Publisher

from . import my_style


def load():
    # Adicionar o `Style` ao `StyleManager` do InVesalius:
    style_id = styles.Styles.add_style(my_style.MyStyle, 2)

    # Habilitar o `style` criado:
    Publisher.sendMessage("Enable style", style=style_id)
