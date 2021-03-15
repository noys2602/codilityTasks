def solution (A):
    for i in range(len(A)):
        if (A.count(A[i])==1):
            return A[i]
    return -1

A=[]
A.append(9)
A.append(3)
A.append(9)
A.append(3)
A.append(9)
A.append(7)
A.append(9)

print(solution(A))





