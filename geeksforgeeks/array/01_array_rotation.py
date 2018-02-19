'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
[1 2 3 4 5 6 7] => d = 2 => [3 4 5 6 7 1 2]



Algorithm:
1. Rotate sub-array 0 to d-1
2. Rotate sub-array d to n-1
3. Rotate the complete array
'''

def rotate_array(arr, d):
    i = 0
    j = d-1
    while(i <= j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1

    i = d
    j = len(arr) - 1
    while (i <= j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1

    i = 0
    j = len(arr)-1
    while (i <= j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1

    print(arr)

def main():
    arr = [1,2,3,4,5]
    d = 2
    rotate_array(arr, d)
    arr = [1, 2, 3, 4, 5]
    d = 3
    rotate_array(arr, d)
    arr = [1, 2, 3, 4, 5]
    d = 4
    rotate_array(arr, d)
    arr = [1, 2, 3, 4, 5]
    d = 5
    rotate_array(arr, d)
if __name__ == "__main__":
    main()