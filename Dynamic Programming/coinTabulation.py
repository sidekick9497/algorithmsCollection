def getNumOfCombinations(number,coinList):
    tabulationList = [0]*(number+1)
    tabulationList[0] = 1
    for coin in coinList:
        for amount in range(0,number+1):
            if(amount >= coin):
                tabulationList[amount] += tabulationList[amount-coin]
    print(tabulationList)
getNumOfCombinations(6,[2,3,6])


