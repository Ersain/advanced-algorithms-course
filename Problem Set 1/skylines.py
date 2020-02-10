def skylines(arr):
    arr.append(0)
    stack = [-1]
    res = 0
    for i in range(len(arr)):
        while arr[i] < arr[stack[-1]]:
            height = arr[stack.pop()]
            width = i - stack[-1] - 1
            res = max(res, height * width)
        stack.append(i)
    arr.pop()
    return res


print(skylines([4, 2, 3, 1]) == 6)
print(skylines([1, 3, 7, 4, 2]) == 9)
print(skylines([2, 7, 1, 8, 3, 0, 5, 4]) == 8)
