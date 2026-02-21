class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        res=0
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=arr[j]
                if (j-i)%2==0: #checking even because indexes starts from 0 as its even
                    res+=s
        return res