class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        from collections import Counter

        group = {}

        for word in strs:
            freq = Counter(word)
            key = tuple(sorted(freq.items()))

            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]

        res = list(group.values())
        return res