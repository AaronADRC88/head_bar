__author__ = 'aferreiradominguez'
from gi.repository import Gtk, Gio


class holaHeadbar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="lololo")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        cabezera = Gtk.HeaderBar()
        cabezera.set_show_close_button(True)
        cabezera.props.title = "Headbar"
        self.set_titlebar(cabezera)

        boton = Gtk.Button()
        icono = Gio.ThemedIcon(name="mail-send-recive-symbolic")
        imagen = Gtk.Image.new_from_gicon(icono, Gtk.IconSize.BUTTON)
        boton.add(imagen)
        cabezera.pack_start(boton)

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        boton2 = Gtk.Button()
        boton2.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(boton2)

        boton3 = Gtk.Button()
        boton3.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(boton3)

        cabezera.pack_start(box)

        self.add(Gtk.TextView())

window=holaHeadbar()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()