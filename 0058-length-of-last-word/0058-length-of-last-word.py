class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        text = s.strip()
        ans = 0
        for i in range(len(text)-1,-1,-1):
            if text[i] == " ":
                break
            ans+=1
        return ans
            
        