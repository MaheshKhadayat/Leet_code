class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        freq = [0] * 26

        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        for i,ch in enumerate(s):
            if freq[ord(ch)-ord('a')] == 1:
                return i

        return -1