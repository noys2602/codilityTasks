def difByOne (arr , num) :
    for i in range (len(arr)) :
        if ((arr[i] == num + 1) or (arr[i] == num - 1 )) :
            return True
    return  False

def solution(A) :
    for i in range (len(A)) :
        return difByOne(A, A[i])
A=[]
A.append(11)
A.append(1)
A.append(8)
A.append(12)
A.append(14)

B=A
print(B)

a= solution(A)
print (a)


