class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x = newInterval[0]
        y = newInterval[1]
        i = 0
        if len(intervals) == 0:
            intervals.append(newInterval)
        while i < len(intervals):
            curInterval = intervals[i]
            xInInterval = x <= curInterval[1] and x >= curInterval[0]
            yInInterval = y <= curInterval[1] and y >= curInterval[0]
            coversInterval = x <= curInterval[0] and y >= curInterval[1]
            if xInInterval or yInInterval or coversInterval: 
                #in between this interval, iterate i to find the end to merge
                newY = max(curInterval[1], y)
                while i < len(intervals) - 1:
                    nextInterval = intervals[i+1]
                    if y < nextInterval[0]:
                        break
                    newY = max(nextInterval[1], y)
                    intervals.pop(i+1)
                curInterval[1] = newY
                curInterval[0] = min(curInterval[0], x)
            elif i < len(intervals) - 1 and intervals[i + 1][0] > y and curInterval[1] < x:
                # in between this interval and next
                intervals.insert(i + 1, newInterval)
            elif i == len(intervals) - 1 and curInterval[1] < x: #append to end 
                intervals.append(newInterval)
            elif i == 0 and curInterval[0] > y: #prepend to beginning
                intervals.insert(0, newInterval)
            i += 1
        return intervals