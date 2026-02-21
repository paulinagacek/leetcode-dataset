from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # store the count of each sum in dictionary so we can check for specific values in O(1)
        sum_count = defaultdict(int)
        # initialize counter and sum
        count = 0
        current_sum = 0
        # loop over numbers in list
        for num in nums:
            # calculate sum until current number
            current_sum += num
            # check if we have seen a number x that could be subtracted from the current value to result in k
            # k = current_sum - x  --( x -k)-->  x = current_Sum - k
            # add number of occurrences of x to counter, or 0 if no such sum exists
            count += sum_count[current_sum - k]
            # update sum counter
            sum_count[current_sum] += 1
        # check if any of the sums from the first to any other position in the list match k
        count += sum_count[k]
        # return count value
        return count