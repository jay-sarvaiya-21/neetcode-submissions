class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        merge = newInterval
        for i in range(len(intervals)):
            start,end = merge
            curr_start, curr_end = intervals[i]
            if curr_end <  start:
                res.append(intervals[i])
                
            elif end < curr_start:
                res.append(merge)
                return res + intervals[i:]
            else:
                merge = [min(start,curr_start),max(end,curr_end)]

           
        res.append(merge)
        
        return res
            
        