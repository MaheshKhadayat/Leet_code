class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        inserted = False
        for interval in intervals:
            if inserted:
                res.append(interval)
            elif newInterval[1] <  interval[0]:
                res.append(newInterval)
                inserted = True
                res.append(interval)
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval[0] = min(interval[0],newInterval[0])
                newInterval[1] = max(interval[1],newInterval[1])
        
        if not inserted:
            res.append(newInterval)


        return res
