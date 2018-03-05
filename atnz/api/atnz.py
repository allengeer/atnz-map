import httplib, urllib, json, sys

this = sys.modules[__name__]

this.apiurl = "api.at.govt.nz"
this.headers = {'Ocp-Apim-Subscription-Key': ''}

def setSubscriptionKey(key):
    """
    This sets the API key for all Auckland Transport calls
    :param key: the subscription key to use
    """
    this.headers = { 'Ocp-Apim-Subscription-Key': key }

def __callApi(call):
    try:
        conn = httplib.HTTPSConnection(this.apiurl)
        conn.request("GET", call, "{body}", this.headers)
        response = conn.getresponse()
        return json.loads(response.read())
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return None

def getRoutes(callback = ""):
    """
    Returns all routes in the AT system
    :param callback: JSONP callback function wrapper
    :return: None or a dict of the response
    """
    params = urllib.urlencode({'callback': callback})
    return __callApi("/v2/gtfs/routes?%s" %params)

def getStops(callback = ""):
    """
    Returns all stops in the AT system
    :param callback: JSONP callback function wrapper
    :return: None or a dict of the response
    """
    params = urllib.urlencode({'callback': callback})
    return __callApi("/v2/gtfs/stops?%s" %params)

def getTrips(callback = ""):
    """
    Gets all trips in the AT System
    :param callback: JSONP callback function wrapper
    :return: None or a dict of the response
    """
    params = urllib.urlencode({'callback': callback})
    return __callApi("/v2/gtfs/trips?%s" %params)

def getTripsByRoute(routeId, callback = ""):
    """
    Gets all trips for a certain route
    :param routeId: the routeId to get trips for
    :param callback: JSONP callback function wrapper
    :return: None or a dict of the response
    """
    params = urllib.urlencode({'callback': callback})
    return __callApi("/v2/gtfs/trips/routeid/%s?%s" % (routeId, params))

def getRoutesByStop(stopId, callback = ""):
    """
    Get all routes that go through a certain Stop ID
    :param stopId: the stop id to get routes for
    :param callback: JSONP callback function wrapper
    :return: None or a dict of the response
    """
    params = urllib.urlencode({'callback': callback})
    return __callApi("/v2/gtfs/routes/stopid/%s?%s" % (stopId, params))

def getVehicleLocations(callback = "", tripId = "", vehicleId = ""):
    """
    Returns the location and status of all vehicles, filtered by trip and vehicleId if supplied
    :param callback: JSONP callback function wrapper
    :param tripId: Optional to filter list by vehicles on a specific tripId
    :param vehicleId: Optional to filter list by vehicleId
    :return:  None or a dict of the response
    """
    params = urllib.urlencode({
        'callback': callback,
        'tripid': tripId,
        'vehicleid': vehicleId
    })
    return __callApi("/v2/public/realtime/vehiclelocations?%s" % params)