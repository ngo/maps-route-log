from __future__ import print_function
from datetime import datetime
import sys
import pytz

import googlemaps

gmaps = googlemaps.Client(key=open('gooma.key', 'r').read().strip())

directions = gmaps.directions(
	sys.argv[1],
	sys.argv[2],
	mode="driving",
	departure_time='now',
        avoid=['tolls']
)[0]

now = datetime.utcnow().replace(tzinfo = pytz.utc)
tz = pytz.timezone('Europe/Moscow')
now = now.astimezone(tz)

duration = 0.0
distance = 0.0
for leg in directions['legs']:
    duration += leg['duration_in_traffic']['value']
    distance += leg['distance']['value']


print(
        '''%d.%d,%s,%d,%d,"%s",%d,%f''' %(
            now.day, now.month, now.strftime('%A'),now.hour, now.minute,
            directions['summary'], int(duration / 60), distance / 1000
        )
)
