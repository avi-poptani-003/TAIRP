import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from tkintermapview import TkinterMapView

def find_location():
    address = entry.get()
    if not address:
        messagebox.showerror("Error", "Please enter a location")
        return

    geolocator = Nominatim(user_agent="geo_finder")
    location = geolocator.geocode(address)

    if location:
        result_label.config(text=f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        map_widget.set_position(location.latitude, location.longitude)
        map_widget.set_marker(location.latitude, location.longitude, text=address)
    else:
        messagebox.showerror("Error", "Location not found")

# GUI Setup
root = tk.Tk()
root.title("Location Finder")
root.geometry("500x600")

tk.Label(root, text="Enter Location:", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, font=("Arial", 12), width=40)
entry.pack(pady=5)

tk.Button(root, text="Find Location", command=find_location, font=("Arial", 12)).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Map Widget
map_widget = TkinterMapView(root, width=480, height=400, corner_radius=10)
map_widget.pack(pady=10)

root.mainloop()
