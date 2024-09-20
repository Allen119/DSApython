def ascendingSort(arr,n):
    swap_count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap_count += 1
    return swap_count

def descendingSort(arr, n):
    swap_count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return swap_count

def main():
    arr=[]
    print("Enter the size of elements")
    n = int(input().strip())
    for i in range(n):
        element = int(input().strip())
        arr.append(element)
    asc=arr.copy()
    desc=arr.copy()

    ascswpnum=descendingSort(asc, n)
    descswpnum=ascendingSort(desc, n)
    print(ascswpnum,descswpnum)
    print(min(ascswpnum,descswpnum))

if __name__ == "__main__":
    main()



