class Solution(object):

    def lengthOfLongestSubstring(self, s):

        n = len(s)

        if n == 0:
            return 0

        dp = [0] * n

        last_seen = {}

        dp[0] = 1
        last_seen[s[0]] = 0

        ans = 1

        for i in range(1, n):

            ch = s[i]

            if ch not in last_seen:

                dp[i] = dp[i - 1] + 1

            else:

                prev = last_seen[ch]

                if i - prev > dp[i - 1]:

                    dp[i] = dp[i - 1] + 1

                else:

                    dp[i] = i - prev

            last_seen[ch] = i

            ans = max(ans, dp[i])

        return ans


s = input("Enter string: ")

obj = Solution()

print(obj.lengthOfLongestSubstring(s))