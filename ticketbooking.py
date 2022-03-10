from utilities import *
from config import train_list, seatMapping

flag = True
print('***************** Welcome to IRCTC Booking App *****************')
while flag:
    print("")
    print("Please Choose a Selection to Move Forward")
    print("1. Book Ticket")
    print("2. Search Available Trains")
    print("3. Get Train Route")
    print("")
    option = int(input())
    if option == 1:
        print('Please Enter Train Number')
        trainNumber = input()
        print('Please Enter Boarding Station')
        sourceStation = input()
        print('Please Enter Destination Station')
        destinationStation = input()
        validateDetail = validateInfo(trainNumber, sourceStation, destinationStation)
        if validateDetail != 0:
            seatMapping, seatStatus = allotSeat(seatMapping, trainNumber, sourceStation, destinationStation)
            if seatStatus == 0:
                print("Sorry ! Seats Not Available")
            else:
                print("Please Input Your Name")
                name = input()
                print("")
                print("TICKET CONFIRMED")
                print("Name : " + str(name).capitalize())
                print("Train No : " + str(trainNumber))
                print("Train Name : " + str(train_list[trainNumber]['train_name']))
                print("Boarding Station : " + str(sourceStation))
                print("Destination Station : " + str(destinationStation))
                print("Seat Number : " + str(seatStatus))
    elif option == 2:
        printTrains()
    elif option == 3:
        print("Please Enter Train No")
        trainN = input()
        printStations(trainN)
    else:
        print("Please Choose Correct Option")
