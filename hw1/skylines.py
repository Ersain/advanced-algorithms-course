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


print(skylines([1, 2, 4]))
