def summaryRanges(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [str(nums[0])]
    res = []
    curr = []
    curr.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] - curr[-1] == 1:
            curr.append(nums[i])
        else:
            if len(curr) > 1:
                res.append(str(curr[0]) + \'->\' + str(curr[-1]))
                curr = []
                curr.append(nums[i])
            else:
                res.append(str(curr[-1]))
                curr = []
                curr.append(nums[i])
        if i == len(nums) - 1 and len(curr) == 1:
            res.append(str(nums[-1]))
        if i == len(nums) - 1 and len(curr) > 1:
            res.append(str(curr[0]) + \'->\' + str(curr[-1]))
    return res