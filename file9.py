nums = [1, 2, 4, 3]
limit = 4

n = len(nums)

answer = float("inf")

for target in range(2, 2 * limit + 1):

    moves = 0

    i = 0
    j = n - 1

    while i < j:

        a = nums[i]
        b = nums[j]

        current = a + b

        # 0 move
        if current == target:
            moves += 0

        # 1 move
        elif 1 <= target - a <= limit or \
             1 <= target - b <= limit:

            moves += 1

        # 2 moves
        else:
            moves += 2

        i += 1
        j -= 1

    answer = min(answer, moves)

print(answer)