def moveOnce(A):
    B=[]
    if (len(A) == 0) :
        return A
    B.append(A[len(A)-1])
    for i in range (len(A)-1) :
        B.append(A[i])
    return B

def solution(A, K) :
    for i in range(K) :
        A = moveOnce(A)
    return A

A = [3, 8, 9, 7, 6]
K = 3
B = solution(A,K)
for i in B :
    print(i)







