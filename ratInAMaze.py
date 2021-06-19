
def isSafe(visited, i ,j, n):
    if i >=0 and j >= 0 and i < n and j < n and visited[i][j] == 0:
        return True
    return False
def helper(A, n, i, j,ans,visited,FinalAns):
    # code here
    # base case

    if i == n-1 and j == n-1:
        FinalAns.append(ans)
        return FinalAns
    if not isSafe(visited,i,j,n):
        return FinalAns
    

    # MOVE UP
    visited[i][j] = 1

    if i-1 > 0 and A[i-1][j] == 1:
        helper(A,n,i-1,j,ans+'U',visited,FinalAns)
    # Move Down
    if i+1 < n and A[i+1][j] == 1:
        helper(A,n,i+1,j,ans+'D',visited,FinalAns)
    # Move left
    if j-1 > 0 and A[i][j-1] == 1:
        helper(A,n,i,j-1,ans+'L',visited,FinalAns)
    # Move right
    if j+1 < n and A[i][j+1] == 1:
        helper(A,n,i,j+1,ans+'R',visited,FinalAns)

    visited[i][j] = 0
    return FinalAns


print(helper([[1, 0, 0, 0],[1, 1, 0, 1],[1, 1, 0, 0],[0, 1, 1, 1]], 4, 0, 0,'',[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[]))