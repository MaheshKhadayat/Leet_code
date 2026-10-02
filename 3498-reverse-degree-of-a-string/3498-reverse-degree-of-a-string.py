class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0

        for i,ch in enumerate(s):
            rev = ord('z') - ord(ch) + 1 
    

            ans += rev*(i+1)
        return ans
        