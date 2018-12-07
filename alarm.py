"""
alarm.py
program to set the alarm for x minute
or for particular time

"""

import pyglet
import winsound
import time
from os.path import abspath, isfile

path = abspath("C:/Windows/media/Alarm01.wav")
def alarm(hh,mm):
	"""
	function to set alarm for the value hh - hour
	mm - minute
	
	"""
	while True:
		cur_time = list(time.localtime())
		hour = cur_time[3]
		minute = cur_time[4]

		if hour == hh and minute == mm:
			sound = pyglet.media.load(path)
			sound.play()
			pyglet.app.run()
			break

def main():

	while True:
		try:

			choice = int(input("Enter your as 1 or 2 \n1.Want to set alarm after x minutes:  \
								\n2.Want to set alarm for particular time:\n ::"))
		except:

			print("Please enter the value in integer 1 or 2")
			continue

		else:

			if choice == 1:

				while True:

					try:

						minutes = int(input("Enter the minutes you want set the alarm for : "))

					except:

						print("please enter the minute value in integers")
						continue

					else:
						cur_time = list(time.localtime())
						
						hh = minutes // 60
						mm = minutes % 60

						hh = (cur_time[3] + hh) % 24
						mm = (cur_time[4] + mm) % 60

						alarm(hh,mm)

					break

			elif choice == 2:
				while True:

					try:

						hh = int(input("please enter the hour value 0 - 23 : "))
						mm = int(input("please enter the minutes value in 0 - 59: "))

					except:
						print("please enter the value in integer")
						continue
					else:
						alarm(hh,mm)

					break

			else:

				print("Please select your input from either 1 or 2")
				continue

			break

if __name__ == '__main__':
	main()