class Solution:
    def trailingZeroes(self, n: int) -> int:
        pw = 5
        cnt = 0
        while n >= pw:
            cnt += n // pw
            pw *= 5
        return cnt
