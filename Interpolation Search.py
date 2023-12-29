# Interpolation Search was invented by W. W. Peterson in 1957.



function interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
while low <= high:
    pos = low + ((target - arr[low]) * (high - low)) / (arr[high] - arr[low])
if pos < low or pos > high:
    if target < arr[low]:
        high = low - 1
    else:
        low = low + 1
else:
    if arr[pos] == target:
        return pos
    elif arr[pos] < target:
        low = pos + 1
    else:
        high = pos - 1
return -1