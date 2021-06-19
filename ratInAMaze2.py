def isSafe(visited, i ,j, n):
    if i >=0 and j >= 0 and i < n and j < n and visited[i][j] == 0:
        return True
    return False
def helper(A, n, i, j,ans,visited):
    # code here
    # base case

    if i == n-1 and j == n-1:
        print(ans)
        return
    if not isSafe(visited,i,j,n):
        return
    

    # MOVE UP
    visited[i][j] = 1

    if i-1 > 0 and A[i-1][j] == 1:
        helper(A,n,i-1,j,ans+'U',visited)
    # Move Down
    if i+1 < n and A[i+1][j] == 1:
        helper(A,n,i+1,j,ans+'D',visited)
    # Move left
    if j-1 > 0 and A[i][j-1] == 1:
        helper(A,n,i,j-1,ans+'L',visited)
    # Move right
    if j+1 < n and A[i][j+1] == 1:
        helper(A,n,i,j+1,ans+'R',visited)

    visited[i][j] = 0
n = int(input("Size of grid: "))
visited =[]
grid =[]
for i in range(n):
    visited.append([])
    for j in range(n):
        visited[i].append(0)

for i in range(n):
    grid.append([])
    for j in range(n):
        grid[i].append(int(input()))
helper(grid, n, 0, 0,'',visited)