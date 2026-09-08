class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        maxele = nums[0]
        for i in range(n):
            minele = min(nums[i:])
            maxele = max(maxele,nums[i])

            if maxele-minele <= k:
                return i

        return -1

        

        return ans