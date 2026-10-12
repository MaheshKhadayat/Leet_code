class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j+=1
        
        while j < len(arr):
            arr[j] = 0
            j+=1
        
        