def findNextGreaterElements(numbers):
    nums=numbers
    n = len(nums)
    ans = [-1] * n
    stack = []
    for k in range(2 * n):
        i = k % n
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            ans[idx] = nums[i]
        if k < n:
            stack.append(i)

    return ans