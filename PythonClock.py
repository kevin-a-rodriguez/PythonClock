# Project for setting and running a calendar/clock
# class for Clock objects
class Clock:

	# function chosen by default if values are not specifically set
	def __init__(self):
		self.month = 1
		self.day = 1
		self.year = 2024
		self.hour = 12
		self.minute = 0
		self.second = 0
		self.timeofday = "AM"
		self.MONTHS = [" ", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		self.DAYSINMONTH =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
	# function for giving the main program chose a starting point
	def InputClock(self, month, day, year, hour, minute, second, TOD):
		self.month = month
		self.day = day
		self.year = year
		self.hour = hour
		self.minute = minute
		self.second = second
		self.timeofday = TOD
		self.MONTHS = [" ", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		self.DAYSINMONTH =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	# function for computing if this year is a leap year
	def IsLeapYear(self):
		if (self.year % 4 != 0):
			return 0
		if (self.year % 400 == 0):
			return 1
		if (self.year % 100 == 0):
			return 0
		return 1

	# function for updating the years
	def UpdateYear(self):
		self.year = self.year + 1
		if (self.IsLeapYear()):
			self.DAYSINMONTH[2] = self.DAYSINMONTH[2] + 1

	# function for updating the months
	def UpdateMonth(self):
		if (self.month == 12):
			self.month = 1
			self.UpdateYear()
		else:
			self.month = self.month + 1; 

	# function for updating the days
	def UpdateDay(self):
		if (self.day == self.DAYSINMONTH[self.month]):
			self.day = 1 
			self.UpdateMonth()
		else:
			self.day = self.day + 1

	# function for updating the hours
	def UpdateHour(self):
		if (self.hour == 12):
			self.hour = 1
		else:
			if (self.hour == 11):
				self.UpdateTOD()
				self.hour = self.hour + 1
			else:
				self.hour = self.hour + 1
				
	# function for updating the minutes 
	def UpdateMinute(self):
		if (self.minute == 59):
			self.minute = 0
			self.UpdateHour()
		else:
			self.minute = self.minute + 1

	# function for updating the seconds
	def UpdateSecond(self):
		if (self.second == 59):
			self.second = 0
			self.UpdateMinute()
		else:
			self.second = self.second + 1
			
	# function for switching between AM and PM
	def UpdateTOD(self):
		if (self.timeofday == "AM"):
			self.timeofday = "PM"
		else:
			self.timeofday = "AM"
			self.UpdateDay()
			
	# function for the adjusting the format of the display to the screen
	def DisplayClock(self):
		if (self.minute < 10 and self.second < 10):
			print(str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second), self.timeofday )
		elif (self.second < 10):
			print(str(self.hour) + ':' + str(self.minute) + ":0" + str(self.second), self.timeofday )
		elif (self.minute < 10):
			print(str(self.hour) + ":0" + str(self.minute) + ':' + str(self.second), self.timeofday )
		else: 
			print(str(self.hour) + ':' + str(self.minute) + ':' + str(self.second), self.timeofday )
		
		print(self.MONTHS[self.month], str(self.day) + ",",  self.year)
		
	# function for running, updating, and formatting the clock/calendar
	def RunClock(self):
		self.DisplayClock()
		self.UpdateSecond()

# main program	
import time

C1 = Clock() #default constructor call
C1.InputClock(10, 9, 2024, 11, 59, 57, "PM") # set values of attributes

while(1):
	C1.RunClock() # run the clock with given the values in C1
	time.sleep(1) #time intervals between each iteration
