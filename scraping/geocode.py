import googlemaps
import json
import os
import sys

# Don't put your Google Maps API Key in github, of course.
key = os.environ['API_KEY']
if key is None:
    print("Set Google Maps API key in API_KEY environment variable.")
    sys.exit(1)
    
gmaps = googlemaps.Client(key=key)

center = gmaps.geocode('Loyal Heights Playfield, Seattle, WA')
print(center)

with open('parks-and-rec.json', 'r') as f:
    parks = json.load(f)
    park = parks[0]
    
    address = park['address']
