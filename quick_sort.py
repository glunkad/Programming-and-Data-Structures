def quick_sort(A:list , left: int, right:int) -> list:
    i = left 
    j = right 
    x = A[(left + right) // 2]

    while i <= j:
        
        while A[i] < x:
            i += 1 
        
        while x < A[j]:
            j -= 1 

        if i <= j:
            A[i],A[j] = A[j], A[i] # swapping
            i += 1
            j -= 1 

    if left < j:
        quick_sort(A, left, j) 

    if i < right:
        quick_sort(A, i, right) 

    return A 

def main():
    A = [44, 55, 12, 42, 94, 18, 7, 17]
    n = len(A) 
    print(f"unsorted array: {A}")
    sorted_A = quick_sort(A, 0, n-1) 
    print(f"sorted array after quicksort: {sorted_A}")

if __name__ == "__main__":
    main()

# Time Complexity
# O(nlogn)
