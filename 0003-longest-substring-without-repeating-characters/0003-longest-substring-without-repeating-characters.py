class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = maxlen = 0

        from collections import defaultdict

        freq = defaultdict(int)

        for end,ch in enumerate(s):
            freq[ch]+=1

            while freq[ch] > 1:
                freq[s[st]]-=1
                st+=1
            
            maxlen = max(maxlen,end-st+1)

        return maxlen