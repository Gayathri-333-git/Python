class Solution(object):
    def reverse(self, x):
        def helper(n):
            if n < 10:
                return n, 10
            
            small, place = helper(n // 10)
            return (n % 10) * place + small, place * 10
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev, _ = helper(x)
        rev *= sign
        
        # 32-bit check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev

sol = Solution()
print(sol.reverse(123))   