class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = []
        cycle = 2 * (numRows - 1)
        
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                result.append(s[j])
                
                # add diagonal element (for middle rows)
                if i != 0 and i != numRows - 1:
                    diag = j + cycle - 2 * i
                    if diag < len(s):
                        result.append(s[diag])
        
        return "".join(result)


# Usage
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))