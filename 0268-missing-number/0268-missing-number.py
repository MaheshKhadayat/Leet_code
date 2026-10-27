class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = 0
        s2 = 0
        i = 1
        for val in nums:
            s1 += val
            s2 += i
            i+=1

        return s2 - s1
        