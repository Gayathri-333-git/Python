from bisect import bisect_left

def gcdValues(nums, queries):
    max_val = max(nums)

    freq = [0] * (max_val + 1)
    for num in nums:
        freq[num] += 1

    count = [0] * (max_val + 1)
    for g in range(1, max_val + 1):
        for multiple in range(g, max_val + 1, g):
            count[g] += freq[multiple]

    exact = [0] * (max_val + 1)
    for g in range(max_val, 0, -1):
        pairs = count[g] * (count[g] - 1) // 2
        multiple = 2 * g
        while multiple <= max_val:
            pairs -= exact[multiple]
            multiple += g
        exact[g] = pairs

    prefix = []
    values = []
    total = 0
    for g in range(1, max_val + 1):
        if exact[g]:
            total += exact[g]
            prefix.append(total)
            values.append(g)

    ans = []
    for q in queries:
        idx = bisect_left(prefix, q + 1)
        ans.append(values[idx])

    return ans


# Direct Output
nums = [2, 3, 4]
queries = [0, 2, 2]

print(gcdValues(nums, queries))