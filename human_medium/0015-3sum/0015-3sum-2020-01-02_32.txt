class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        num_checked = set()
        last_indices = {n: i for i, n in enumerate(nums)} 
        for idx, num in enumerate(nums):
            target = -num
            if num in num_checked:
                continue
            num_checked.add(num)
            for i, n in itertools.islice(enumerate(nums), idx+1, None):
                # this condition ensures that 
                # third number exists and is taken from different place
                if last_indices.get(target - n, i) > i:
                    result.add(tuple(sorted([num, target-n, n])))
        return result
