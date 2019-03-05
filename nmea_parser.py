import serial
from utils import *

class NmeaParser:
	def __init__(self, port, baudrate):
		self.data = ''

		try:
			self.comPort = serial.Serial(port, baudrate)
		except serial.SerialException:
			print ('Cannot open serial port: ' + port)

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.close()

	def close(self):
		try:
			self.comPort.flush()
			self.comPort.close()
		except (AttributeError, serial.SerialException):
			pass
	
	def update_com_port(self):
		try:
			if self.comPort.inWaiting():
				self.data += self.comPort.read().decode()
				
				if '\r\n' in self.data:
					nmeaData = self.data.split('*')
					self.data = ''
					checksum = int(nmeaData[1], 16)
					calcChecksum = 0

					for c in nmeaData[0]:
						if c != '$':
							calcChecksum ^= ord(c)

					if calcChecksum == checksum:
						return nmeaData[0].split(',')
		except (AttributeError, serial.SerialException):
			print("Error updating COM port")
			# pass

	def send(self, str):
		try:
			message = str.encode('utf-8')
			self.comPort.write(message)
			print (message)
		except (serial.SerialTimeoutException, serial.SerialException, AttributeError):
			return False

		return True

