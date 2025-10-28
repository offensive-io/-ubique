import folium
import json

def show_map():
    try:
        with open("data/locations.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No location data found.")
        return

    # Create a base map centered on the first location
    first_location = data[0]["location"]
    map_obj = folium.Map(location=[27.7, 85.3], zoom_start=12)  # Default center (Kathmandu)

    for entry in data:
        folium.Marker(
            location=[27.7, 85.3],  # Replace with actual coordinates later
            popup=f"{entry['location']}<br>{entry['note']}<br>{entry['timestamp']}"
        ).add_to(map_obj)

    map_obj.save("ubique_map.html")
    print("Map saved as ubique_map.html")
