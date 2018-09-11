# cyclically rotate an array by one

# Method for rotation
def rotate(arr, n):
    x = arr[n - 1]
    # print(x)

    for i in range(n-1 , 0, -1):
        print(arr[i],"start")
        arr[i] = arr[i - 1]
        print(arr[i], "end")

    arr[0] = x;


# Driver function
arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array is")
for i in range(n):
    print(arr[i], end=' ')

rotate(arr, n)

print("\nRotated array is")
for i in range(n):
    print(arr[i], end=' ')

# This article is contributed
# by saloni1297