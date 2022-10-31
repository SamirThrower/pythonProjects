def binarySearch(list, findMe):
    startIndex = 0
    endIndex = len(list) - 1

    while startIndex <= endIndex:

        midIndex = startIndex + (endIndex - startIndex) // 2
        mid_value = list[midIndex] 

        if mid_value == findMe:
            return "This value exists at index " + str(midIndex)

        elif findMe < mid_value:
            endIndex = midIndex - 1

        elif findMe > mid_value:
            startIndex = midIndex + 1

    return "This value does not exist"

list = [3, 5, 6, 7, 9, 11, 12, 13, 18, 19, 21, 22, 25]

print( binarySearch(list, 6 )) # returns 2
print( binarySearch(list, 11)) # returns 5
print( binarySearch(list, 14)) # returns does not exist
