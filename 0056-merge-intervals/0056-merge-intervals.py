class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        current_interval = intervals[0]
        if len(intervals) == 1:
            return intervals
        i = 0
        result = []
        while i < len(intervals):
            if len(result) == 0:
                result.append(intervals[i])
            else:
                current_interval = result[-1]
                if current_interval[0] <= intervals[i][0] and current_interval[1] >= intervals[i][1]:
                    current_interval = [current_interval[0], current_interval[1]]
                    result.pop()
                    result.append(current_interval)
                elif current_interval[1] >= intervals[i][0]:
                    current_interval = [current_interval[0], intervals[i][1]]
                    result.pop()
                    result.append(current_interval)
                else:
                    result.append(intervals[i])
            i += 1 
        return result
