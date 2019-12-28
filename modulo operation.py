
def isEVen(num):
	if num% 2==0:
		return 'True'
	else:
		return 'False'

print(isEVen(3))

def convertToHM(mins):
	hours = mins/60
	minutes = mins %60
	return str(hours) + ':' + str(minutes)

print(convertToHM(60))