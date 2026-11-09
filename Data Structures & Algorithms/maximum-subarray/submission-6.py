import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = -math.inf
        maxsum = -math.inf
        for num in nums:
            if num > cursum + num:
                cursum = num
            else:
                cursum += num
            if cursum > maxsum:
                maxsum = cursum
        return maxsum