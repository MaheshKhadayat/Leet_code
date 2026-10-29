class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if arr[-1] == 0 or arr[0] == n-1:
            return 1
        max_chunk = 0
        chunk = 0
        for i,val in enumerate(arr):
            max_chunk =  max(max_chunk,val)

            if max_chunk == i:
                chunk+=1

        return chunk

