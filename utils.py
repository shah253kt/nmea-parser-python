def coordinate_to_degrees(coor):
	dot_index = coor.strip().find('.')

	if dot_index == -1:
		return coor
	else:
		degree = float(coor[:dot_index - 2])
		minute = float(coor[dot_index - 2:])

		# print coor, ' ', dot_index, ' ', degree, ' ', minute

		return '%.6f' % (degree + (minute / 60))

def calculate_checksum(sentence):
	checksum = 0

	for c in sentence:
		checksum ^= ord(c)

	return checksum

def int_to_hex_string(value):
	s = str(hex(value)).split('0x')[1].upper()

	if len(s) < 2:
		s = '0' + s
		
	return s

def complete_nmea_sentence(sentence):
	checksum = int_to_hex_string(calculate_checksum(sentence))
	return '$' + sentence + '*' + checksum + '\n\r'

def create_nmea_sentence(nmeaParam):
	return complete_nmea_sentence(','.join(nmeaParam))