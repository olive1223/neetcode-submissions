class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            second = i + 1
            while second < len(nums):
                if nums[second] + num == target:
                    return [i, second]
                second += 1
        return [0, 0]