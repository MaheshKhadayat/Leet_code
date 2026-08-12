class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()

        cookie = 0
        child = 0
        ans = 0
        while child < len(g) and cookie < len(s):
            if g[child] > s[cookie]:
                cookie+=1
                continue
            cookie+=1
            ans+=1
            child+=1

                
            
        return ans

            
        