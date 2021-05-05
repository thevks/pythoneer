def bubble_sort(a):
    l = len(a)
    for i in range(l) :
        for j in range(1,l-i) :
            if a[j] < a[j-1] :
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
            
if __name__ == '__main__' :
    a = [2, 1, 9, 4, 8, 7, 5, 6, 3]
    bubble_sort(a)
    print("Sorted array : ")
    print(a)    