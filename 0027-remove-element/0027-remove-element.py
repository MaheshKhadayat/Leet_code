class Solution(object):
    def removeElement(self, arr, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 


        for i in range(len(arr)):
            if arr[i] != val:
                arr[k] = arr[i]
                k+=1
        return k