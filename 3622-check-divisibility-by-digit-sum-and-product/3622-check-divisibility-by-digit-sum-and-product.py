class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        p = 1
        nval = n
        while n > 0:
            rem = n % 10
            s +=rem
            p*=rem
            n = n // 10

        ans = s+p

        if nval % ans == 0:
            return True
        else:
            return False
