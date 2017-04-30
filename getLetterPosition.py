import sys

def getNumLettersBefore(string, c):
    position = 0
    for i in range(len(string)):
        if string[i] == c:
            position = i
    return position

string = sys.argv[1]
c = sys.argv[2]
a = getNumLettersBefore(string, c)
print a
