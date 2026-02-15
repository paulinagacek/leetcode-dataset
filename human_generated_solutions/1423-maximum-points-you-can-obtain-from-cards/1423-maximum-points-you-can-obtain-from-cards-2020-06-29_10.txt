class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        pre, suf = [arr[i] for i in range(len(arr))], [arr[i] for i in range(len(arr))]
        n = len(arr)
        for i in range(1,n):
            pre[i] += pre[i-1]
        for i in range(n-2, -1, -1):
            suf[i] += suf[i+1]
        ans = -1
        for i in range(k+1):
            left = k-i-1
            right = n-i
            curr = 0
            if (right < n):
                curr += suf[right]
            if (left >= 0):
                curr += pre[left]
            ans = max(ans, curr)
        return ans