import gi
from util import payloadItem, search

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

title = "cheapest gas locator thing"

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title = title)

        self.overallBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.overallBox)

        self.txtBoxes = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.overallBox.pack_start(self.txtBoxes, True, True, 0)

        self.city = Gtk.Entry()
        self.city.set_placeholder_text("City")
        self.city.set_margin_top(6)
        self.city.set_margin_bottom(6)
        self.city.set_margin_left(6)
        self.txtBoxes.pack_start(self.city, True, True, 0)

        self.state = Gtk.Entry()
        self.state.set_placeholder_text("State")
        self.state.set_max_length(2)
        self.state.set_margin_top(6)
        self.state.set_margin_bottom(6)
        self.state.set_margin_left(6)
        self.txtBoxes.pack_start(self.state, True, True, 0)

        self.button = Gtk.Button(label="Search")
        self.button.connect("clicked", self.searchButton)
        self.button.set_margin_top(6)
        self.button.set_margin_bottom(6)
        self.button.set_margin_left(6)
        self.button.set_margin_right(6)
        self.txtBoxes.pack_start(self.button, True, True, 0)

        self.entries = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.overallBox.pack_start(self.entries, True, True, 0)

        entry = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)
        self.entries.pack_start(entry, True, True, 0)
    def searchButton(self, widget):
        print("Search clicked")

        self.state.set_sensitive(False)
        self.city.set_sensitive(False)
        self.button.set_sensitive(False)

        res = search.parse({ "state": self.state.get_text(), "city": self.city.get_text() })

        win.destroy()

        class ResultsWindow(Gtk.Window) :
            def __init__(self):
                super().__init__(title = title)

                self.set_default_size(450,300)

                self.sw = Gtk.ScrolledWindow()
                self.add(self.sw)

                self.list = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
                self.list.set_margin_top(6)
                self.list.set_margin_bottom(6)
                self.sw.add(self.list)

                for location in res:
                    entry = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 6)

                    leftBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)
                    
                    name = Gtk.Label()
                    name.set_markup("<big>" + location["name"] + "</big>")
                    name.set_justify(Gtk.Justification.LEFT)
                    leftBox.pack_start(name, True, True, 0)

                    price = Gtk.Label()
                    price.set_markup("<i>$" + location["price"] + " Regular</i>")
                    price.set_justify(Gtk.Justification.LEFT)
                    leftBox.pack_start(price, True, True, 0)

                    dieselStr = "<b>Not</b> diesel friendly"
                    if location["diesel"] is True: dieselStr = "Diesel friendly"

                    diesel = Gtk.Label()
                    diesel.set_markup(dieselStr)
                    diesel.set_justify(Gtk.Justification.LEFT)
                    leftBox.pack_start(diesel, True, True, 0)

                    entry.pack_start(leftBox, True, True, 0)

                    rightBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 6)

                    for i, addr in enumerate(location["location"].values()):
                        if len(addr) <= 50 and len(addr) >= 5:
                            addressStr = Gtk.Label()

                            if i is 0:
                                addressStr.set_markup("<b>" + addr + "</b>")
                            else:
                                addressStr.set_markup("" + addr + "")
                            
                            addressStr.set_justify(Gtk.Justification.LEFT)
                            rightBox.pack_start(addressStr, True, True, 0)
                    
                    entry.pack_start(rightBox, True, True, 0)
                    
                    self.list.pack_start(entry, True, True, 0)

                print("-" * 40)
        
        win2 = ResultsWindow()
        win2.connect("destroy", Gtk.main_quit)
        win2.show_all()
        Gtk.main()

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()