class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        freq = defaultdict(int)

        st = 0
        s = 0
        maxsum = 0
        
        for i,val in enumerate(nums):

            while val in freq:
                s-=nums[st]
                del freq[nums[st]]
                st+=1
                
            s+=val
            freq[val]+=1


            if len(freq) == k:
                maxsum = max(s,maxsum)
                s-=nums[st]
                del freq[nums[st]]
                st+=1
                
        return maxsum




                
