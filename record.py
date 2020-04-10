class Record:

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


    def createDispatchRecord(dispatchNo, OrderNo, orderType, orderDestination, vehicleNo, vehicleStatus, latitude, longitude, ETA, route):
        value = None
        
        conn = dbConnect("team13_wego")
        cursor = conn.cursor()
        
        sql = "INSERT INTO `dispatchRecords` (`dispatchNo`,`OrderNo`,`orderType`,`orderDestination`,`vehicleNo`,`latitude`,`ETA`, `route`)"
        #VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (value, dispatchNo, OrderNo, orderType, value, vehicleNo, value, value, value))
        conn.commit()
        dispatchNo = cursor.lastrowid
        
        cursor.close()
        conn.close()
        
        return dispatchNo
    
    
    # get the dispatch lat and longs of user and vehicle from database id
    def getDispatchRecord(vehicleNo):
        conn = dbConnect("team13_wego")
        cursor = conn.cursor()
        
        sql = "SELECT * FROM dispatchRecords"
        
        cursor.execute(sql, vehicleNo)
        
        vehicleNo = cursor.fetchone()
        
        cursor.close( )
        conn.close()
        
        print(vehicleNo)
        
        returnvehicleNo
    
    
    
    # Connects to MySQL with the database name as the parameter
    def dbConnect(team13_wego):
        db = pymysql.connect(
                             host="localhost",
                             user="team13",
                             password="donaldduck",
                             db=team13_wego
                             )
        return db

