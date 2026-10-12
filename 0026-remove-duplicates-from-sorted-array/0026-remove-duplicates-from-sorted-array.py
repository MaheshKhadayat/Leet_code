class Solution(object):
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(1,len(arr)):
            if arr[k] != arr[i]:
                k+=1
                arr[k] = arr[i]
            
        return k+1


                