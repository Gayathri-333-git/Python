class Solution(object):
    def isPalindrome(self, x):
        # negative numbers are not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        rev = 0
        
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        
        # even digits OR odd digits
        return x == rev or x == rev //10
sol = Solution()
print(sol.isPalindrome(121))   
print(sol.isPalindrome(123))   