from utils import *
from nmea_parser import *

if __name__ == '__main__':
	com_port = NmeaParser('COM6', 9600)
	print("Program starts")

	while True:
		try:
			data = com_port.update_com_port()
			
			if data != None:
				print (data)
				parameters = ['OK']
				com_port.send(create_nmea_sentence(parameters))
		except KeyboardInterrupt:
			com_port.close()
			print("Program ends")
			break