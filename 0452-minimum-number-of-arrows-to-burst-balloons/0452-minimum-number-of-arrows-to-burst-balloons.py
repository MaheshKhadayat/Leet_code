class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()

        MaxPoint = None
        ans = 1
        for point in points:
            if not MaxPoint:
                MaxPoint = point[1]
                continue
            if MaxPoint >= point[0]:
                MaxPoint = min(point[1],MaxPoint)
            else:
                MaxPoint = max(point)
                ans+=1
            

        return ans
        

        