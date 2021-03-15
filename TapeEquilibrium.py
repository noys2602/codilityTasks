def solution(A):
    leftSum = A[0]
    rightSum = sum(A) - A[0]
    minAbs = abs(rightSum - leftSum )
    for i in range(1,len(A)) :
        if(abs(leftSum - rightSum) < minAbs):
            minAbs = abs(leftSum - rightSum)
        leftSum += A[i]
        rightSum -= A[i]
    return minAbs

A=[]
A.append(3)
A.append(1)
A.append(2)
A.append(4)
A.append(3)

print (solution(A))