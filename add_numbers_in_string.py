"""
	Given a string with a mix of integers and characters, find sum of all
	integers in the string and print them out in the order they are listed in
	the string. For example:  The string a1h76hj6klkllkk87654_87_ji89 would
	print out 1 + 76 + 6 + 87654 + 87 + 89 = 87913.
"""

import sys

characters = sys.argv[1]
numbers = ""

def add_ints(s):
	global numbers
	total = 0
	place = 0
	number = 0
	numprev = 0
	for i in reversed(s):
		if i.isdigit():
			total += int(i) * pow(10, place);
			place += 1
		else:
			number = total - numprev
			numprev += number
			if number != 0:
			    numbers += " + " + str(number)[::-1]
			place = 0
	return total

def show_num(s):
	nums = ""
	if len(numbers) > 0:
	    nums = numbers[3:]
	    return nums[::-1] + " = " + str(add_ints(s))
	else:
		return "No Numbers found!"

def main():
	print(str(add_ints(characters)))
	print(show_num(characters))

if __name__ == '__main__':
	main()
