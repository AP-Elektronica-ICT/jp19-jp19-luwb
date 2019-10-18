from pypozyx import PozyxSerial, get_first_pozyx_serial_port, Coordinates
from configparser import ConfigParser

#read setup file
parser = ConfigParser()
parser.read('config.ini')
connectedDevice = parser.get('default','connected_id')

#change the ID's for setting coordinates of devices from config file
anchor1 = parser.get('default','anchor1_id') if connectedDevice != parser.get('default','anchor1_id') else None
anchor2 = parser.get('default','anchor2_id') if connectedDevice != parser.get('default','anchor2_id') else None
anchor3 = parser.get('default','anchor3_id') if connectedDevice != parser.get('default','anchor3_id') else None
anchor4 = parser.get('default','anchor4_id') if connectedDevice != parser.get('default','anchor4_id') else None

#Setup variables
coordinatesAnchor1 = Coordinates()
coordinatesAnchor2 = Coordinates()
coordinatesAnchor3 = Coordinates()
coordinatesAnchor4 = Coordinates()

#Check if connected
serial_port = get_first_pozyx_serial_port()
if serial_port is not None:
    pozyx = PozyxSerial(serial_port)
    print("Connection success!")
else:
    print("No Pozyx port was found")
    exit()

try:
    #Set the coordinates in the device
    pozyx.setCoordinates(Coordinates(parser.get('default','anchor1_coordinates')), anchor1)
    pozyx.setCoordinates(Coordinates(parser.get('default','anchor2_coordinates')), anchor2)
    pozyx.setCoordinates(Coordinates(parser.get('default','anchor3_coordinates')), anchor3)
    pozyx.setCoordinates(Coordinates(parser.get('default','anchor4_coordinates')), anchor4)
    print("Coordinates set.")

    #get the coordinates of the device
    pozyx.getCoordinates(coordinatesAnchor1, anchor1)
    print(coordinatesAnchor1)
    pozyx.getCoordinates(coordinatesAnchor2, anchor2)
    print(coordinatesAnchor2)
    pozyx.getCoordinates(coordinatesAnchor3, anchor3)
    print(coordinatesAnchor3)
    pozyx.getCoordinates(coordinatesAnchor4, anchor4)
    print(coordinatesAnchor4)

#Exception exit
except:
    print("")
    print("Exit program")
