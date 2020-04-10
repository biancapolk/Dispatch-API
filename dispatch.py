class Dispatch:
    
    #dispatchNo
    #OrderNo
    #orderType
    #orderDestination
    #vehicleNo
    #vehicleStatus
    #latitude
    #longitude
    #ETA
    #route
    
    
    def __init__(self):
        self.__dispatchNo = -1
        self.__vehicle = ""
        self.__vehicleNo = ""
        self.__latitude = ""
        self.__longitude = ""
        self.__eta = ""
    
    def setDispatchNo(self, dispatchNo):
        self.__disp_id = dispatchNo
    
    def getVehicleNo(self, vehicleNo):
        self.__vehicleNo = vehicleNo
    
    
    def setLatitiude(self, latitude):
        self.latitude = latitude
    
    def getLatitiude(self, latitude):
        self.latitude = latitude
    
    
    def setLongitude(self, longitude):
        self.longitude = longitude
    
    def getLongitude(self, longitude):
        self.__longitude = longitude
