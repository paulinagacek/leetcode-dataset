def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
     
        pm = int(math.log2(m))
        pn = int(math.log2(n))

        if pm != pn:
            return 0

        newm = 1 << pm
        return newm + self.rangeBitwiseAnd(m & (newm-1), n & (newm-1))