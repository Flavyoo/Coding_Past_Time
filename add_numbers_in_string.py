
import sys

characters = sys.argv[1]
numbers = ""

def add_ints(s):
	"""
	Function add_ints takes in a string for it's parameter. It searches the string for
	positive numbers and returns the total sum of all the numbers found.
	For example: The string a1h76hj6klkllkk87654_87_ji89 would
	print out 1 + 76 + 6 + 87654 + 87 + 89 = 87913.
	Takes one command line input which is the string to read.
	"""
	# Prepend extra character to prevent bug of not adding numbers in front.
	global numbers
	total = 0
	place = 0
	number = 0
	numprev = 0
	for i in reversed(" " + s):
		if i.isdigit():
			total += int(i) * pow(10, place);
			place += 1
		else:
			# Current number found.
			number = total - numprev
			# Keep track of total numbers found so far.
			numprev += number
			if number != 0:
			    # Appends the reverse of the number to numbers
			    numbers += " + " + str(number)[::-1]
			place = 0
	return total

def show_num(s):
	"""
	Returns a string of all the numbers found in the string s through an
	addition and sum representation.
	"""
	nums = ""
	if len(numbers) > 0:
	    # Reverse the reverse number.
	    # We do not need the first three characters of " + ".
	    nums = numbers[3:]
	    return nums[::-1] + " = " + str(add_ints(s))
	else:
		return "No Numbers found!"

def main():
	print(add_ints(characters))
	print(show_num(characters))

if __name__ == '__main__':
	main()
