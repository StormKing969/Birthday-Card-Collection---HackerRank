def hackerCards(collection, d):
    missingElements = []
    sortedCollection = sorted(collection)
    lastElement = int(sortedCollection[-1])
    counter = 1
    totalSum = 0
    outputList = []

    while counter < lastElement:
        if counter not in missingElements and counter not in sortedCollection:
            missingElements.append(counter)
            counter += 1
            totalSum += counter
            if totalSum > d:
                break
        else:
            counter += 1

    print(missingElements)

    # for i in missingElements:
    #     if totalSum < d:
    #         totalSum += i
    #         if totalSum < d:
    #             outputList.append(i)
    #     else:
    #         break
    #
    # if totalSum < d:
    #     outputList.append(lastElement + 1)
    #
    # while totalSum < d:
    #     totalSum += int(outputList[-1])
    #     if totalSum < d:
    #         outputList.append(int(outputList[-1]) + 1)
    #
    # print(outputList)
    # return outputList

hackerCards([1,3,4], 7)
# Answer: [2, 5]
hackerCards([4,6,12,8], 14)
# Answer: [1,2,3,5]
hackerCards([1,2,3,4], 5)
# Answer: [5]
hackerCards([2,88,999,1,3], 100)
# Answer: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
hackerCards([2,4,5,6,9,8], 7)
# Answer: [1, 3]