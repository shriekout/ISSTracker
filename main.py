from datetime import datetime
import requests
import tkinter
from tkintermapview import TkinterMapView

URL = "http://api.open-notify.org/iss-now.json"
ZOOM = 3
HTML = "index.html"

def receive_iss_info():
    response = requests.get(URL)
    data = response.json()

    dt = datetime.fromtimestamp(data['timestamp'])
    t = str(dt)
    pos_x = float(data['iss_position']['latitude'])
    pos_y = float(data['iss_position']['longitude'])
    print(f"{pos_x}, {pos_y}")

    return pos_x, pos_y

def update_position():
    pos_x, pos_y = receive_iss_info()
    marker1.map_widget.set_position(pos_x, pos_y, marker=True)

    window.after(60000, update_position)

pos_x, pos_y = receive_iss_info()

window = tkinter.Tk()
window.geometry(f"{800}x{600}")

map_widget = TkinterMapView(window, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
marker1 = map_widget.set_position(pos_x, pos_y, marker=True)
map_widget.set_zoom(ZOOM)

update_position()

window.mainloop()