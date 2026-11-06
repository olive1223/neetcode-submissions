#optimal (memoized)
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        return self.subRob(nums, 0, {})

    def subRob(self, nums: List[int], index, memoized) -> int:
        if index in memoized:
            return memoized[index]
        if len(nums) <= 2:
            memoized[index] = max(nums)
            return max(nums)
        returnVal = max(self.subRob(nums[1:], index + 1, memoized), nums[0] + self.subRob(nums[2:], index + 2, memoized))
        memoized[index] = returnVal
        return returnVal
