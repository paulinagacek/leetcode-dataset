class Solution:
    def trailingZeroes(self, n: int) -> int:
	# iteration -- since all zeros come from 2*5, so we count how many 2 and 5 in given n. since we have enough 2, so we only need to count how many 5 we have in n.
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res