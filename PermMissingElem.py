def sigma(num) :
    sum = 0
    for i in range (num + 1):
        sum+=i
    return sum

def solution(A):
    sum(A)
    return sigma(len(A)+1) - sum(A)


A=[]
A.append(1)
A.append(2)
A.append(3)
A.append(5)

print(sum(A))
print (sigma(5))
print(solution(A))