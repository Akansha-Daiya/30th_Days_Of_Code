class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=0
        overall_max=-inf
        for i in nums:
            curr_max=max(curr_max+i, i)
            overall_max=max(overall_max, curr_max)
        return overall_max
        
