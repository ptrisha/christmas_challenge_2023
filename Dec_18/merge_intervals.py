# Leetcode problem Day 18
# Problem description:
# https://leetcode.com/problems/merge-intervals

# This solution is rather slow.  
# A second version might be called for, time permitting.

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            if interval2[0] <= interval1[1]:
                return True
            return False

        def merge_2intervals(interval1: List[int], interval2: List[int]) -> List[int]:
            if interval2[1] > interval1[1]:
                return [ interval1[0], interval2[1] ]
            return interval1
        
        # sort the list in ascending order of the starting times and then of the
        # end times (where there are ties for starting times)
        sorted_intervals = sorted(intervals, key = lambda x: (x[0], x[1]))

        merged = []

        while sorted_intervals:
            
            working_interval = sorted_intervals.pop(0)

            num_merged = 0
            for interval in sorted_intervals:
                if overlap(working_interval, interval):
                    working_interval = merge_2intervals(working_interval, interval)
                    num_merged += 1
                else:
                    break

            sorted_intervals = sorted_intervals[num_merged:]

            merged.append(working_interval)

        return merged
    