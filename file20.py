from math import gcd

def gcdValues(nums):
    prefixGcd = []
    mx = 0

    for x in nums:
        mx = max(mx, x)
        prefixGcd.append(gcd(x, mx))

    prefixGcd.sort()

    ans = 0
    i, j = 0, len(prefixGcd) - 1

    while i < j:
        ans += gcd(prefixGcd[i], prefixGcd[j])
        i += 1
        j -= 1

    return ans

print(gcdValues([2,6,4]))