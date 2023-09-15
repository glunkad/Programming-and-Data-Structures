def bubble_sort(A, n):
    i = 0 
    f = False 
    while (i < n) and (not f):
        f = True 
        i += 1  
        for j in range(0,n-i):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j] 
                f = False 
    return A

def main():
    A = [30,12,18,8,14,41,3,39]
    n = len(A)
    new_A = bubble_sort(A,n)
    print(new_A)

if __name__ == "__main__":
    main() 

