import gi
from util import payloadItem, search

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title = "cheapest gas locator thing")

        self.overallBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.overallBox)

        txtBoxes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.overallBox.pack_start(txtBoxes, True, True, 0)

        self.city = Gtk.Entry()
        self.city.set_placeholder_text("City")
        self.city.set_margin_top(6)
        self.city.set_margin_bottom(6)
        self.city.set_margin_left(6)
        txtBoxes.pack_start(self.city, True, True, 0)

        self.state = Gtk.Entry()
        self.state.set_placeholder_text("State")
        self.state.set_max_length(2)
        self.state.set_margin_top(6)
        self.state.set_margin_bottom(6)
        self.state.set_margin_left(6)
        txtBoxes.pack_start(self.state, True, True, 0)

        self.button = Gtk.Button(label="Search")
        self.button.connect("clicked", self.searchButton)
        self.button.set_margin_top(6)
        self.button.set_margin_bottom(6)
        self.button.set_margin_left(6)
        self.button.set_margin_right(6)
        txtBoxes.pack_start(self.button, True, True, 0)
    def searchButton(self, widget):
        print("Search clicked")

        info = {
            "state": self.state.get_text(),
            "city": self.city.get_text()
        }

        print(info)

        self.state.set_sensitive(False)
        self.city.set_sensitive(False)

        res = search.parse(info)

        self.entries = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        for location in res:
            entry = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)

            name = Gtk.Label()
            name.set_text(location["name"])
            self.entries.pack_start(name, True, True, 0)

            print("-" * 40)
            print("| Name: " + location["name"])
            print("| Price: $" + location["price"])
            print("| Sells diesel? " + str(location["diesel"]))

            for addr in location["location"].values():
                print("| - " + addr)
            
            self.entries.pack_start(entry, True, True, 0)

        print("-" * 40)

        self.overallBox.pack_start(self.entries, True, True, 0)

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()