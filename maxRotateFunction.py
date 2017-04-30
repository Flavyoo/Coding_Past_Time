# Given an array of numbers find the maximum number that can be created by
<<<<<<< Updated upstream
# multiplying the indices with the value after each rotation of the array.
=======
# multiply the indices with the value after each rotation of the array.

>>>>>>> Stashed changes
# O(n) time.
class MaxRotate(object):
    # Takes an array of numbers and a boolean--True to print, False to not print.
    def maxRotateFunction(self, A, printRotation):
        s = float("-inf")
        l = len(A)
        temp = 0
        j = 0
        if len(A) == 0: return 0
        count = 0
        for i in range(l * l):
            temp += j * A[j]
            j += 1
            # reset j to start the index count all over again.
            if j > l - 1:
                # rotate the array
                A = [A[-1]] + A[:l - 1]
                if printRotation:
                    print A
                j = 0
                # compare the current total to the previous total to find max.
                if temp > s:
                    s = temp
                temp = 0
        return s

if __name__ == '__main__':
    mr = MaxRotate()
    solution = mr.maxRotateFunction([4,3,2,6], True)
    print solution
