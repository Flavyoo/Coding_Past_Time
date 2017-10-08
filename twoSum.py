from hashtable import Hashtable, Item

# Brute Force Method. Quadratic time.
class Solution(object):
    # Given an array of numbers and a target number, return the indices of
    # two numbers that add up to the target, given there is only on solution.
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

    # Find the complement using a hashtable. O(n) time.
    def twoSumWithHash(self, nums, target):
        hashtable = Hashtable()
        for i in range(len(nums)):
            # Check if complement exists.
            if hashtable.contains(target - nums[i]):
                # Return it if it does.
                return [hashtable.get(target - nums[i]), i]
            else:
                hashtable.put(nums[i], i)


if __name__ == '__main__':
    S = Solution()
    solution = S.twoSumWithHash([4,8,3,-8,2,6,], 7)
    solution2 = S.twoSum([4,8,3,-8,2,6,], 7)
    print solution
    print solution2
