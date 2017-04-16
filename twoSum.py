
# Given an array of numbers and a target number, return the indices of
# two numbers that add up to the target, given there is only on solution.
class Solution(object):
    def twoSum(self, nums, target):
        prevloc = 0
        nextloc = 0
        for i in range(len(nums)):
            compliment = target - nums[i]
            prevloc = i
            for j in range(i + 1, len(nums)):
                if nums[j] == compliment:
                    nextloc = j
                    return [prevloc, nextloc]
        return None

    # Not working yet
    def twoSumlinear(self, nums, target):
        prevloc = 0
        nextloc = 0
        indices = []
        coms = []
        for i in range(len(nums)):
            if nums[i] < target:
                coms += nums[i]
        for k in range(len(coms)):
            compliment = target - coms[k]
            prevloc = i
            for j in range(i + 1, len(coms)):
                if nums[j] == compliment:
                    nextloc = j
                    return [prevloc, nextloc]
        return None

if __name__ == '__main__':
    S = Solution()
    solution = S.twoSum([4,8,3,-8,2,6,], 7)
    print solution
