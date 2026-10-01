class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] > 9:
                store = nums[i]
                s = 0

                while store != 0:
                    rem = store % 10
                    s += rem
                    store = store // 10
                
                nums[i] = s
            if i == nums[i]:
                return i

            
        return -1
                    