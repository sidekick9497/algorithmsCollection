def findMaxConsecutiveOnes(nums):
    index = 0 
    sequenceStarted = False
    maxCount = 0
    while index < len(nums):
        if(nums[index] == 1 and not sequenceStarted):
            startIndex = index
        elif(nums[index] == 0 and sequenceStarted):
            stopIndex  = index
            sequencelength = stopIndex - startIndex
            print(sequencelength)
            if(sequencelength > maxCount):
                maxCount = sequencelength
                sequenceStarted = False
        index += 1
    return maxCount
findMaxConsecutiveOnes([1,1,0,1,1,1])