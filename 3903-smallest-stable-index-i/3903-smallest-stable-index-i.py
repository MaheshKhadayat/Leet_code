class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = -1
        for i in range(len(nums)):
            maxele = max(nums[:i+1])
            minele = min(nums[i:])
            
            if maxele - minele <= k:
                ans = i
                break
        return ans