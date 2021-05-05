def binary_search_1(array, target):
    start = 0
    end = len(array) -1
    found = 0
    while (start <= end):
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        else:
            start = start + 1
    return -1
      
def binary_search_2(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if target == a[mid]:
        return mid
    elif target < a[mid]:
        return binary_search_2(array, start, mid-1, target)
    else:
        return binary_search_2(array, mid+1, end, target)

if __name__ == '__main__':
    a = [0,1,21,33,45,45,61,71,72,73]
    target = 33
    binary_search_1(a, target)
    index = binary_search_2(a, 0, len(a)-1, target)
    if (index != -1):
         print("Found element %d " % a[index])
