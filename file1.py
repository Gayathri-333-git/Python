class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        dp = []
        
        for i in range(len(strs[0])):
            ch = strs[0][i]
            
            for s in strs:
                if i >= len(s) or s[i] != ch:
                    return "".join(dp)
            
            dp.append(ch)
        
        return "".join(dp)
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  
print(sol.longestCommonPrefix(["dog","racecar","car"]))     