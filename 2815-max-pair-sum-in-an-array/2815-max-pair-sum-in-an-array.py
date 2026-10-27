class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        maxsum = -1
        for i,value in enumerate(nums):
            maxval = 0
            val = value
            while val != 0:
                maxval = max(val%10,maxval)
                val = val // 10

            if maxval in map:
                maxsum = max(maxsum,map[maxval] + value)
                map[maxval] = max(map[maxval],value)
            else:
                map[maxval]=value
        return maxsum

            

        
        
                
