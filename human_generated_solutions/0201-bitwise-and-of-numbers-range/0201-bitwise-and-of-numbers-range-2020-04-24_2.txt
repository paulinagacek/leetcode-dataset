class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mbin, nbin = bin(m)[2:], bin(n)[2:] # take out the "0b" format
        ml, nl = len(mbin), len(nbin)
		# pre-pad the shorter one of mbin, nbin with zeros to make them equal in length
		# optim: directly return 0 if detect ml != nl, beats 98% Python solutions
        if ml < nl:
            mbin = \'0\' * (nl-ml) + mbin
        elif nl < ml:
            nbin = \'0\' * (ml-nl) + nbin
		# at this point, mbin and nbin are aligned at least significant bit, len(mbin) = len(nbin)
        
		# find out the length of longest common prefix
        common_prefix_length = 0
        for mbit, nbit in zip(mbin, nbin):
            if mbit == nbit:
                common_prefix_length += 1
            else: # detect the first different bit, the end of common prefix 
                break

		# the result has the common prefix mbin[:common], and 0 as remaining bits. Total length should be max(ml,nl)
        res = mbin[:common_prefix_length] + \'0\'*(max(ml,nl)-common_prefix_length)
        return int(res, 2)