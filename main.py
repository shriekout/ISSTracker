from datetime import datetime
import requests
import folium
import webview

URL = "http://api.open-notify.org/iss-now.json"
ZOOM = 3
HTML = "index.html"

response = requests.get(URL)
data = response.json()

dt = datetime.fromtimestamp(data['timestamp'])
when = str(dt)
where = [data['iss_position']['latitude'], data['iss_position']['longitude']]

m = folium.Map(location=where, zoom_start=ZOOM)
folium.Marker(where, tooltip=when).add_to(m)
m.save(HTML)

webview.create_window("pywebview", HTML)
webview.start()