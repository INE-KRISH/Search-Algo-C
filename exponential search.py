# exponential search is an algorithm created by Jon Bentley and Andrew Chi-Chih Yao in 1976.


function exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    low = 0
    high = min(1, n - 1)

    while high < n and arr[high] < target:
        low = high + 1
        high = min(2 * high, n - 1)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
return -1