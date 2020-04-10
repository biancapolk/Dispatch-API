import requests
import json
import pymysql

key = "access_token=pk.eyJ1IjoiY2xhdWdobGkiLCJhIjoiY2pzNTd6NzR5MGQyOTN5cXB1cG5xZ3llNSJ9.VnjbmQPCRGAQUROSYRpEUQ"
basePath = "https://api.mapbox.com"
endpointDirections = "/directions/v5/mapbox/driving/"
endpointForAddres = "/geocoding/v5/mapbox.places/"
testAddress = "3001 S Congress Ave, Austin, Texas, 78704"

#vehicle hub location
# lat1 = 30.157130
# long1 = -97.869910

#stedwards lat and long
# lat2 = 30.229991
# long2 = -97.753847

city = "Austin"
state = "TX"
zip = "78704"
addr = "3001 S Congress Ave"

# generates the first part of the request with inputed coordinates
# returns the combined base path end point and coordinates
def generatebasePathEndpoint(coordinates, basePath, endPoint):
    path = basePath + endPoint + coordinates + ".json?"
    return path

# adds the key to the established path
# return usable link to send as a request to the api
def generateAPIRequest(path, key):
    return path + key

# takes in two sets of coordinates
# return the coordinates as one string
def latAndLongToString(lat1, long1, lat2, long2):
    coordinates = str(long1) + "%2C" + str(lat1) + "%3B" + str(long2) + "%2C" + str(lat2)
    return coordinates

# send the request to the external api
# returns a response that is loaded into dictionary from a json object
def sendRequest(request):
    response = requests.get(request)
    response = json.loads(response.text)
    return response

# creates the proper format for the address to be sent
def createAddressURL(addr, city, state, zip):
    addressurl = addr + " " + city + " " + state + " " + zip
    addressurl = addressurl.replace(" ", "%20")
    return addressurl


    #gets the center coordinates of the entered address
def getCoordinatesOfAddress(addr, city, state, zip):
    addressurl = createAddressURL(addr, city, state, zip)
    path = generatebasePathEndpoint(addressurl, basePath, endpointForAddres)

    request = generateAPIRequest(path, key)
    request = request + "&autocomplete=true&types=address"
    apiResponse = sendRequest(request)

    coordinatesOfAddress = apiResponse["features"][0]["center"]

    #returns [long, lat]
    return coordinatesOfAddress

# gets distance in meter
# returns in feet if meter is < .5mi else
# returns in miles
def getRouteDistance(lat1, long1, lat2, long2):

    coordinates = latAndLongToString(lat1, long1, lat2, long2)
    path = generatebasePathEndpoint(coordinates, basePath, endpointDirections)
    request = generateAPIRequest(path, key)
    apiResponse = sendRequest(request)

    meterDistance = apiResponse["routes"][0]['distance']
    milesDistance = meterDistance / 1609.34

    if meterDistance < 804:
        feetDistance = meterDistance * 3.281
        return round(feetDistance, 2)

    return round(milesDistance, 2)


# get duration of route in seconds
# returns duration in minuets
def getRouteDuration(lat1, long1, lat2, long2):
    coordinates = latAndLongToString(lat1, long1, lat2, long2)
    path = generatebasePathEndpoint(coordinates, basePath, endpointDirections)
    request = generateAPIRequest(path, key)
    apiResponse = sendRequest(request)

    durationInSec = apiResponse['routes'][0]['duration']
    durationInMin = durationInSec / 60

    return round(durationInMin)


# returns all intersections and their coordinates of the first routes of lat1,long1, to lat2,long2
def getRouteOnly(lat1, long1, lat2, long2):
    coordinates = latAndLongToString(lat1, long1, lat2, long2)

    path = generatebasePathEndpoint(coordinates, basePath, endpointDirections)

    request = generateAPIRequest(path, key + "&steps=true&alternatives=false")

    apiResponse = sendRequest(request)

    numOfLegs = 0
    legs = apiResponse['routes'][0]['legs']
    numOfSteps = 0
    numOfIntersections = 0



    arrayOfRouteIntersectionCoordinates = []

    for leg in range(len(apiResponse['routes'][0]['legs'])):
        numOfLegs += 1
        for step in range(len(apiResponse['routes'][0]['legs'][leg]['steps'])):
            numOfSteps += 1
            for intersection in range(len(apiResponse['routes'][0]['legs'][leg]['steps'][step]['intersections'])):
                numOfIntersections += 1
                arrayOfRouteIntersectionCoordinates.append(legs[leg]['steps'][step]['intersections'][intersection]['location'])

    # arrayOfRouteIntersectionCoordinates = apiResponse['routes'][0]['legs'][0]['steps'][0]['intersections'][0]['location']
    # print(arrayOfRouteIntersectionCoordinates)
    # print("numOfLegs: ", numOfLegs, "\nnumOfSteps: ", numOfSteps, "\nnumOfIntersections: ", numOfIntersections)

    return arrayOfRouteIntersectionCoordinates

# def main():
    # print('https://api.mapbox.com/directions/v5/mapbox/driving/-73.989%2C40.733%3B-74%2C40.733.json?access_token=pk.eyJ1IjoiY2xhdWdobGkiLCJhIjoiY2pzNTd6NzR5MGQyOTN5cXB1cG5xZ3llNSJ9.VnjbmQPCRGAQUROSYRpEUQ')

    # print(getRouteDuration(lat1, long1, lat2, long2))
    # print(getRouteDistance(lat1, long1, lat2, long2))

    # print(createAddressURL())
    # print(getCoordinatesOfAddress(addr,city,state,zip))

    # getAvailableVehicleCoordiantes()

    # getRouteOnly(lat1,long1,lat2,long2)

# main()


