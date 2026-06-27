from collections import Counter

def maximumLength(nums):
    cnt = Counter(nums)
    ans = 1

    if 1 in cnt:
        ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

    for x in cnt:
        if x == 1:
            continue

        cur = x
        length = 0

        while cnt.get(cur, 0) >= 2:
            length += 2
            cur *= cur

        if cnt.get(cur, 0) == 1:
            length += 1
        else:
            length -= 1

        ans = max(ans, max(1, length))

    return ans

# Test cases
print(maximumLength([5, 4, 1, 2, 2])) 
print(maximumLength([1, 3, 2, 4])) 
print(maximumLength([1, 16, 49, 16, 121])) 

