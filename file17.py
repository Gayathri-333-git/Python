class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        end = 0

        for start, finish in intervals:
            if finish > end:
                count += 1
                end = finish

        return count

intervals = [[1,4],[3,6],[2,8]]

sol = Solution()
print(sol.removeCoveredIntervals(intervals))