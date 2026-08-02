class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        alice_score = bob_score = 0

        st = 0
        end = len(piles)-1
        i = 0
        while st < end:
            stones = max(piles[st],piles[end])
            if piles[st] >= piles[end]:
                st+=1
            else:
                end-=1
            if i % 2 == 0:
                alice_score+=stones
            else:
                bob_score+=stones
            
        return True if alice_score > bob_score else False
            