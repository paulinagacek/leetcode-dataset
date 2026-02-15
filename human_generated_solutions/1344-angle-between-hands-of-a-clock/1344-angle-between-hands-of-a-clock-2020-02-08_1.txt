class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs(30 * hour - 5.5 * minutes)
        return diff if diff <= 180 else 360 - diff