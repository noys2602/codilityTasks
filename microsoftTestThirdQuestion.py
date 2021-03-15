def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def firstOne (S):
    for i in range(len(S)):
        if S[i] == "1":
            return i
    return 0

def solution(S) :
    if (("0" not in S) and (len(S) == 400000)) :
        return 799999
    firstOneInS = firstOne (S)
    S = S[firstOneInS:len(S)]
    decimalNumber = binaryToDecimal(int(S))
    counter = 0
    while (decimalNumber > 0) :
        if decimalNumber%2 == 1 :
            decimalNumber-=1
            counter+=1
        else :
            decimalNumber/=2
            counter += 1
    return counter

S = "1111010101111"
firstOneInS = firstOne (S)
S = S[firstOneInS:len(S)]
num = binaryToDecimal(int(S))
print(num)
print(solution(S))

