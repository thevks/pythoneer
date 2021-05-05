def insertion_sort(a) :
    l = len(a)
    for i in range(1, l) :
        key = a[i]
        j = i-1
        while j>= 0 and key < a[j] :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

if __name__ == '__main__':
    a = [8,4,2,1,5,9,3,5]
    print("Unsorted Array : ", a)
    print("Unsorted Array : ", insertion_sort(a))