import sys
import os
import time
import requests

configPath = '..'
sys.path.append(os.path.abspath(configPath))
sys.path.append(os.path.abspath('../database'))
import traffic_config
# from sqlalchemy import create_engine,schema,types
# from sqlalchemy.sql import select
# from sqlalchemy.sql import and_, or_, not_
from sqlalchemy.orm import sessionmaker


from traffic_models import Routes,TrafficLog,routes_table,trafficlog_table,engine

def getTimeForTravel(sourceLat,sourceLon,destinationLat,destinationLon):
    payload = {}
    payload['origins'] = sourceLat+','+sourceLon
    payload['destinations']= destinationLat +','+destinationLon
    payload['departure_time'] = 'now'
    payload['key'] = traffic_config.config['distanceMatrixKey']
    jsonResponse = requests.get(traffic_config.config['distanceMatrixURL'], params=payload).json()
    return jsonResponse['rows'][0]['elements'][0]['duration_in_traffic']['value'];

def update(listRouteIDs):
    session = sessionmaker(bind=engine)();
    for routeID in listRouteIDs:
        result = session.query(Routes).filter(Routes.ID == routeID)
        sourceLat=''
        sourceLon=''
        destinationLat=''
        destinationLon ='';
        for row in result:
            sourceLat = row.SOURCE_LATITUDE
            sourceLon = row.SOURCE_LONGITUDE
            destinationLat = row.DESTINATION_LATITUDE
            destinationLon = row.DESTINATION_LONGITUDE
        timeOfTravelMins = getTimeForTravel(sourceLat,sourceLon,destinationLat,destinationLon);
        print TrafficLog.__module__
        print type(TrafficLog)
        newLog = TrafficLog(ROUTEID = routeID,TIMEOFLOG = int(time.time()),TRAVELTIMEMINUTES = timeOfTravelMins)
        session.add(newLog)
    session.commit()
    # connection = engine.connect()
    # for routeID in listRouteIDs:
    #     s = select([routes_table]).where(routes_table.c.ID == routeID);
    #     result = connection.execute('select * from ROUTES')
    #     for row in result:
    #         print row
    # connection.close();
    return;

if __name__ == '__main__':
    dbPath = traffic_config.config['dbPath']
    update([1,2]);