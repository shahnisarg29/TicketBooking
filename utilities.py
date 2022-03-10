from config import *


def validateInfo(train_no, source, destination):
    if train_no not in train_list.keys():
        print("Please Enter Correct Train Number")
        return 0
    station_list = train_list[train_no]['stations']
    if source in station_list and destination in station_list:
        sourceindex = station_list.index(source)
        destindex = station_list.index(destination)
        if destindex > sourceindex:
            return 1
        else:
            print("Please Check Journey Details")
            return 0
    else:
        print("Please Choose Correct Stations")
        print(station_list)
        return 0


def printStations(train_no):
    if train_no not in train_list.keys():
        print("Please Enter Correct Train Number")
        return
    station_list = train_list[train_no]['stations']
    print('Route for Train No : ' + str(train_no))
    for station in station_list:
        print(station)


def printTrains():
    for train in train_list.keys():
        print('Train No : ' + str(train) + ' - ' + str(train_list[train]['train_name']))


def allotSeat(seatMap, train_no, source, dest):
    currentTrainMap = seatMap[train_no]
    for seat in currentTrainMap.keys():
        lstStations = currentTrainMap[seat]
        newlstStations = checkCompletePathAvailable(lstStations, source, dest)
        if newlstStations != 0:
            seatMap[train_no][seat] = newlstStations
            print(train_list)
            # print('SEAT NO : ' + str(seat))
            return seatMap, seat
    return seatMap, 0


def checkCompletePathAvailable(stationsList, source, dest):
    start = -1
    for st in stationsList:
        if st == source:
            start = stationsList.index(st)
        else:
            if start != -1 and st == 'END':
                # print('Not Available')
                return 0
            if start != -1 and st == dest:
                # print("Route Available")
                for i in range(start, stationsList.index(dest)):
                    stationsList[i] = 'END'
                return stationsList
    return 0
