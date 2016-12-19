def is_leap(year):
	"""
	For a year to be a leap year three things criterias need to be looked at.
	1. The year is evenly divisible by four
	2. If the year can be divided by 100 it is not a leap year, unless it can
	also be divided by 400.
	"""
    leap = False
	if year % 4 == 0:
		leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        leap = True
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        leap = False
    return leap
