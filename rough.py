# Optimized recursion
def max_min(A, beg, end):
    if beg == end:
        return [A[beg],A[end]]
    if beg == end - 1:
        if A[beg] >= A[end]:
            return [A[beg],A[end]]
        else:
            return [A[end],A[beg]]


    # Recursive Approach
    mid = (beg + end)//2
    MM_1 = max_min(A,beg,mid-1)
    MM_2 = max_min(A,mid,end)
    # Self Work 
    return [max(MM_1[0], MM_2[0]), min(MM_1[1], MM_2[1])]
print(max_min([1,2,3,4],0,3))