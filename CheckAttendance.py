# A = Absent L = Late P = present. If there are two or more L's in a row or
# more than one A student gets penalty.
class CheckAttendance(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s + "1"
        Acount = 0
        lcount = 0
        for i in range(len(s)):
            if Acount > 1 or lcount > 2:
                return False
            if s[i] == "A":
                Acount += 1
            if s[i] == "L" and s[i + 1] == "L" and s[i + 2] == "L":
                lcount += 1
                return False
        return True
        
if __name__ == '__main__':
    CA = CheckAttendance()
	CA.checkRecord("ALLLP")
