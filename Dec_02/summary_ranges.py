class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        range_list = []
        range_start = nums[0]
        range_end = nums[0]
        nums_len = len(nums)
        counter = 0
        for i, num in enumerate(nums):
            if range_start+counter == num:
               counter += 1
            else:
                if i-1 < 0:
                   range_end = num
                else:
                   range_end = nums[i-1]
                range_list.append( (range_start, range_end))
                range_start = num
                range_end = num
                counter = 1

            if i+1 == nums_len:
               range_list.append( (range_start, num))

        results_str = [ str(x)+"->"+str(y) if x != y else str(x) for (x,y) in range_list ]
        return results_str
        
