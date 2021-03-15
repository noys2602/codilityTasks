def buildZero (num=1) :
    str = ""
    for i in range(num):
        str += "0"
    return str

def maxZeroes (num=1) :
    binNum = bin(num)
    binNum = binNum[2:]
    oneAmmount = binNum.count("1")
    zeroAmmount = buildZero(len(binNum) - oneAmmount)
    while (len(zeroAmmount)>=1):
        if (zeroAmmount + "1") in binNum :
            return len(zeroAmmount)
        zeroAmmount = zeroAmmount[1:len(zeroAmmount)]
    return  0

a = 5
binA = bin(a)
print (binA)
print (maxZeroes(a))




