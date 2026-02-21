class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 1
        while True:
            cur_div = n//(5**i)
            if cur_div == 0:
                break
            count += cur_div
            i += 1
        return count