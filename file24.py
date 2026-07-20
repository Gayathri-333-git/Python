grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1

m = len(grid)
n = len(grid[0])
total = m * n

k %= total

arr = []
for row in grid:
    arr.extend(row)

arr = arr[-k:] + arr[:-k]

ans = []
idx = 0
for i in range(m):
    ans.append(arr[idx:idx+n])
    idx += n

print(ans)
