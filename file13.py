nums = [999, 19, 199]

def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

minimum = float('inf')

for num in nums:
    minimum = min(minimum, digit_sum(num))

print(minimum)