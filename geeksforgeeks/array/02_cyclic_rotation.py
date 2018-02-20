'''
Given an array, cyclically rotate the array clockwise by one.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}


Algorithm:
1. Save last element into a temp var
2. Move elements to the right by 1
3. Copy temp to arr[0]
'''

def rotate(arr, n):
    tmp = arr[n-1]

    for i in reversed(range(0, n-1)):
        arr[i+1] = arr[i]
    arr[0] = tmp
    print(arr)



def main():
    arr = [1,2,3,4,5]
    rotate(arr, 5)
    arr = [1, 4, 5]
    rotate(arr, 3)
    arr = [1, 2, 3, 4, 5,7]
    rotate(arr, 6)
    arr = [1]
    rotate(arr, 1)


if __name__ == "__main__":
    main()