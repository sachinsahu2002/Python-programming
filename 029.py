# Tried to solve the leet code problem
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = len(nums)
        for i in range(b):
            for j in range(i+1,b):
                if (j - i == nums[j] - nums[i]):
                    a = a+1
        return((b*(b-1)/2)-a)
    