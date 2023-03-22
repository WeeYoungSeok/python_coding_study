n = input()

if len(n) == n.count("0") or len(n) == n.count("1"):
    print("0")
else:
    isZero = False
    isOne = False
    zeroCount = 0
    oneCount = 0
    for i in n:
        if i == "0":
            if isZero == False:
                isZero = True
                zeroCount += 1
                isOne = False
        else:
            if isOne == False:
                isOne = True
                oneCount += 1
                isZero = False
    print(min(zeroCount, oneCount))
        
    