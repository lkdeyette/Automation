import webbrowser

# Set the starting address
start_address = '3804 139 Ave NW, Edmonton, AB T5Y 3G4'

# Set the destination address directly
destination_address = '10331 120 St NW, Edmonton, AB'

# Construct the Google Maps URL for directions
url = f'https://www.google.ca/maps/dir/?api=1&origin={start_address.replace(" ", "+")}&destination={destination_address.replace(" ", "+")}'

# Open the web browser with the constructed URL
webbrowser.open(url)
