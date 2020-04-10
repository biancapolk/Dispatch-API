#/supply/api/dispatch/vehicle
import pymysql


class Vehicle (object):
    
    def dbConnect():
        # Connects to MySQL with the database name as the parameter
        db = pymysql.connect (
                              host="localhost",
                              user="team13",
                              password="donaldduck",
                              db="team13_wego"
                              )
        return db



#vehicleNo
#vehicleType
#vehicleStatus
#vehicleData


# team13_wego (DB) -> order_record (table)
def getVehicle(vehicleNo, vehicleType, vehicleStatus, latitude, longitude):
    conn = dbConnect()
    cursor = conn.cursor()
    
    try:
        sql = "INSERT INTO `vehicleAccount` (`vehicleNo`, `vehicleType`, `vehicleStatus`, `latitude`, `longitude`))"
        cursor.execute(sql, (1, type, waiting, 45.366130, -84.667950))
        conn.commit()
        cursor.close()
        conn.close()
        
        result = {'result': True, 'message': "Vehicle " + vehicleNo + " has been registered successfully"}
    except:
        result = {"result": False, "message": "Exception: Could not add vehicle to DB or Vehicle is already in DB"}
    
    return result
# update vehicel status to active


#def setVehicleNo
def getVehicleData():
    conn = dbConnect("team13_wego")
    cursor = conn.cursor()
    
    sql = "SELECT vehicleNo, vehicleType, vehicleStatus, latitude, longitude FROM vehicle WHERE vehicleStatus = 'waiting'"
        
    cursor.execute(sql)
    
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    data = []
    
    if (cursor.rowcount > 0):
        data.append(result[0])
        data.append(result[1])
        data.append(result[2])
        data.append(float(result[3]))
        data.append(float(result[4]))
    
        vehicleSelected = True
        #was found
    else:
        vehicleSelected = False

    print(data)
    
    data = {"data": data, "avaliable vehicle": vehicleSelected}
        
    return data



def updateVehicleStatus(vehicleNo):
    conn = dbConnect("team13_wego")
    cursor = conn.cursor()
    
    print("updating vehicle " + vehicleNo)
        
    sql = "UPDATE Vehicle SET  = 'vehicle_status' to 'active' WHERE vehicleNo = %s"
    
    cursor.execute(sql, str(vehicleNo))
    
    conn.commit()
    
    cursor.close()
    conn.close()
    
    
    # get the dispatch lat and longs of user and vehicle from database id
    def getDispatchRecord(vehicleNo):
        conn = dbConnect("team13_wego")
        cursor = conn.cursor()
        
        sql = "SELECT * FROM dispatchrecord"
        
        cursor.execute(sql, vehicleNo)
        
        location = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        print(location)
        
        return location


