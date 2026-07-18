nums = [2, 5, 6, 9, 10]

a = min(nums)
b = max(nums)

while b:
    a, b = b, a % b

print(a)