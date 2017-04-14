# Works for rotations of string that are 998 charactes long. > 998, there is
# maximum recursion depth exceeded
# sorted
# aabracadabr
# abraabracad
# abracadabra
# acadabraabr
# adabraabrac
# braabracada
# bracadabraa
# cadabraabra
# dabraabraca
# raabracadab
# racadabraab

# Unsorted
# aabracadabr
# raabracadab
# braabracada
# abraabracad
# dabraabraca
# adabraabrac
# cadabraabra
# acadabraabr
# racadabraab
# bracadabraa
# abracadabra

import sys
string = str(sys.argv[1])

# Works on string of lengths <= 998.
# takes in the string, count variable i, and list p to store the rotations
def rotateStringR(string, i, p):
    if i == len(string):
        return perms
    tempString = string[-1] + string[:len(string) - 1]
    p += [tempString]
    return rotateStringR(tempString, i + 1, perms)

# Works on any length string.
def rotateString(string):
    perms = []
    for i in range(len(string)):
        tempString = string[-1] + string[:len(string) - 1]
        perms += [tempString]
        string = perms[i]
    return perms


if __name__ == '__main__':
    perms = []
    rotations = rotateString(string)
    rotations2 = rotateStringR(string, 0, perms)
    i = 1
    for string in zip(rotations, rotations2):
        print str(i) + " " + string[1] + " " + string[0]
        i += 1
