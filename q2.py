from typing import List

def findlucky(arr:List[int]) -> int:
    arr.sort(reverse=True)
    for i in range(len(arr)):
        current = arr.count(arr[i])
        if current == arr[i]:
            return current
    return -1
    


input = [7,7,7,7,7,7,7]
print(findlucky(input))