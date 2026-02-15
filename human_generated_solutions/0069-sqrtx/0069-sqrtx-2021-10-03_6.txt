class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x // 2
        while start <= end:
            mid = start + ((end - start) // 2)
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid < x:
                start = mid + 1
            else:
                end = mid - 1
        return start