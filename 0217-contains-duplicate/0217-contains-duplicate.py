class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}

        for val in nums:
            if val in map:
                return True
            else:
                map[val] = 1
        return False
        