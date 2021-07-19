#Justin Baraniuk
#January 27, 2021


def time_of_day():
	import time
	gmt = time.time()

	days_since_epoch = int(gmt // 60 // 60 // 24)

	#calculate clock time 
	sec = int(gmt % 60)
	min = int(gmt // 60 % 60)
	hour = int(gmt // 60 // 60 % 24)
	period = 'AM'

	#set AM or PM
	if hour >= 12:
		hour = hour % 12
		period = 'PM'

	print("The time is {}:{}:{} {} and {} "\
		"days have passed since 'the epoch'."\
		.format(hour, min, sec, period, days_since_epoch))

time_of_day()