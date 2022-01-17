#!/usr/bin/python3
year = 2021
# Your code should be below this line
if (( year % 4) == 0):
	if (( year % 100) == 0):
		if (( year % 400) == 0):
			#prints True for the provided value of year
			print("True")

		else: 
			#prints False for the provided value of year 
			print("False")
	else:
		#prints True for the provided value of year 		
		print("True")
else:
	#prints False for the provided value of year 
	print("False")
