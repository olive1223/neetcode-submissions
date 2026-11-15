class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in cache:
                return [cache[diff], i]
            else:
                cache[num] = i
        return [0, 0]