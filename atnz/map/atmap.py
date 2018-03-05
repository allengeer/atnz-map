from atnz.api import atnz
from gmplot import gmplot


def generateRTMap(apikey, fileout):
    """
    This function generates an HTML file containing a google map with each bus and train in auckland
    marked with a red dot.
    :param apikey: this is your API key from the Auckland Transport API
    :param fileout: this is the output file for the map
    """
    atnz.setSubscriptionKey(apikey)
    rtfeed = atnz.getVehicleLocations()['response']
    pts = []
    lats = []
    longs = []
    for vehicle in rtfeed['entity']:
        lats.append(vehicle['vehicle']['position']['latitude'])
        longs.append(vehicle['vehicle']['position']['longitude'])
        pts.append({"lat": vehicle['vehicle']['position']['latitude'], "long":vehicle['vehicle']['position']['longitude'], "color":"#FF0000"})

    midlat = min(lats) + (max(lats) - min(lats)) / 2
    midlong = min(longs) + (max(longs) - min(longs)) / 2

    # Place map
    gmap = gmplot.GoogleMapPlotter(midlat, midlong, 13)

    for point in pts:
        gmap.scatter([point["lat"]], [point["long"]], color=point["color"], size=40, marker=False)
    gmap.draw(fileout)
