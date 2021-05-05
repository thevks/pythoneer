def bubble_sort_basic(a):
    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j] 
    return a

def bubble_sort(a):
    l = len(a)
    is_sorted = False
    counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(l -1 - counter):
            if a[i] > a[i+1] :
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False
        counter += 1
    return a
                   
if __name__ == '__main__' :
    a = [2, 1, 9, 4, 8, 7, 5, 6, 3]
    
    print("Sorted array : ", bubble_sort(a))
    
    a = [2, 1, 9, 4, 8, 7, 5, 6, 3]
    print("Sorted array : ", bubble_sort_basic(a))
