def selection_sort(a):
    l = len(a)
    for i in range(l-1):
        min_idx = i
        for j in range (i+1, l):
            if a[min_idx] > a[j] :
                min_idx = j
        #Swap 
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == '__main__':
    a = [8,4,2,1,5,9,3,5]
    print("Unsorted Array : ", a)
    print("Unsorted Array : ", selection_sort(a))