class Clock:

	def __init__(self):
		self.month = 10
		self.day = 9
		self.year = 2024
		self.hour = 8 
		self.minute = 0
		self.second = 0
		self.timeofday = "PM"
		self.MONTHS = [" ", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
		self.DAYSINMONTH =  [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

	def IsLeapYear(self):
		if (self.year % 4 != 0):
			return 0
		if (self.year % 400 == 0):
			return 1
		if (self.year % 100 == 0):
			return 0
		return 1
	
	def UpdateYear(self):
		self.year = self.year + 1
		if (self.IsLeapYear()):
			self.DAYSINMONTH[2] = self.DAYSINMONTH[2] + 1

	def UpdateMonth(self):
		if (self.month == 12):
			self.month = 1
			self.UpdateYear()
		else:
			self.month = self.month + 1; 

	def UpdateDay(self):
		if (self.day == self.DAYSINMONTH[self.month]):
			self.day = 1 
			self.UpdateMonth()
		else:
			self.day = self.day + 1

	def UpdateHour(self):
		if (self.hour == 12):
			self.hour = 1
		else:
			if (self.hour == 11):
				self.UpdateTOD()
				self.hour = self.hour + 1
			else:
				self.hour = self.hour + 1

	def UpdateMinute(self):
		if (self.minute == 59):
			self.minute = 0
			self.UpdateHour()
		else:
			self.minute = self.minute + 1

	def UpdateSecond(self):
		if (self.second == 59):
			self.second = 0
			self.UpdateMinute()
		else:
			self.second = self.second + 1

	def UpdateTOD(self):
		if (self.timeofday == "AM"):
			self.timeofday = "PM"
		else:
			self.timeofday = "AM"
			self.UpdateDay()

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
	
	def RunClock(self):
		self.DisplayClock()
		self.UpdateSecond()

	
import time

C1 = Clock() #default constructor call
C1.InputClock(10, 9, 2024, 11, 59, 57, "PM") # set values of attributes

while(1):
	C1.RunClock()
	time.sleep(1)