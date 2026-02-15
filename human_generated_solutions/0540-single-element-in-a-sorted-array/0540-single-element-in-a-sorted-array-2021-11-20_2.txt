class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for num, count in counts.items():
            if count == 1:
                return num
        return -1  # this will never be reached
		# return Counter(nums).most_common()[-1][0]  # one-liner, but TC O(nlogn)