class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        freq = defaultdict(int)
        maxlen = 0
        st = 0

        for i,ch in enumerate(s):
            freq[ch]+=1

            while freq[ch] == 3:
                freq[s[st]]-=1
                st+=1
            maxlen = max(i-st+1,maxlen)
            
        return maxlen




            