class Solution(object):
    def twoSumDP(self, nums, target):
        dp = {}  # sum -> (i, j)

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                current_sum = nums[i] + nums[j]
                dp[current_sum] = (i, j)

        if target in dp:
            return list(dp[target])

        return []

# Usage
sol = Solution()
nums = [2, 7, 11, 15]
target = 9

print(sol.twoSumDP(nums, target))



