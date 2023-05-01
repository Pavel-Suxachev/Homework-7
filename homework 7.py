# Модуль 4. Уровень 1.

def binary_search(arr,value):
    low_index=0
    high_index=(len(arr))-1
    i=1
    while low_index<=high_index:
        print(i)
        i+=1
        mid_index=(low_index+high_index)//2
        if arr[mid_index]==value:
            return mid_index
        if arr[mid_index]>value:
            high_index=mid_index-1
        else:
            low_index=mid_index+1
    return None
arr = [1,2,3,4,5,15,20,27,52,95,110]
value = 95
d = binary_search(arr, value)
print(d)

# Модуль 4. Уровень 2.

def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j]<a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

a = [20,-9,15,1,2,10,-124,1100,-1204,0]
print(a)
print(insertion_sort(a))