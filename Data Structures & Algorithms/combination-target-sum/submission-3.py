class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        def dfs(curSum, curCombo, curIndex):
            if curSum == target:
                combos.append(curCombo)
                return
            for num in range(curIndex, len(nums)):
                value = nums[num]
                if value + curSum <= target:
                    dfs(value+curSum, curCombo + [value], num)
            return curCombo
        dfs(0, [], 0)
        return combos