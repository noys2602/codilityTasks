import math
def solution (X , Y , D):
    print(((Y-X)/D))
    if (((Y-X)/D).is_integer()):
        return (((Y - X) / D))
    else:
        return (((Y - X) // D)) + 1



print (solution(1, 5, 2))