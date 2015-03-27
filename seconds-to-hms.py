def convertTime(seconds):
        '''
        This function converts an amount of
        seconds and converts it into a struct
        containing [hours, minutes, seconds]
        '''
	second = seconds % 60
	minutes = seconds / 60
	hours   = minutes / 60
	Time = [hours, minutes, second]
	return Time
