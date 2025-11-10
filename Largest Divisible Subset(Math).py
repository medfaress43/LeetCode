class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        nums.sort()
        dp, prev = [1] * len(nums), [-1] * len(nums)

        def find_pairs(i=0, j=1):
            if i >= len(nums) - 1: return
            if j >= len(nums):
                find_pairs(i + 1, i + 2)
                return
            if nums[j] % nums[i] == 0 and dp[i] + 1 > dp[j]:
                dp[j], prev[j] = dp[i] + 1, i
            find_pairs(i, j + 1)

        find_pairs()

        idx = max(range(len(dp)), key=lambda i: dp[i])
        
        def build(idx):
            return build(prev[idx]) + [nums[idx]] if idx != -1 else []

        return build(idx)
