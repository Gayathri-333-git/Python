class Solution(object):

    def minimumEffort(self, tasks):

        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)

        energy = 0
        current = 0

        for actual, minimum in tasks:

            if current < minimum:
                energy += (minimum - current)
                current = minimum

            current -= actual

        return energy


# Create object
obj = Solution()

# Input
tasks = [[1, 2], [2, 4], [4, 8]]

# Function call
print(obj.minimumEffort(tasks))