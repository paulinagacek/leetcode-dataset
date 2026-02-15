class Solution:
    def isHappy(self, n: int) -> bool:
        total = 0
        for digit_str in str(n):
            digit = int(digit_str)
            total += digit * digit

        if total == 1 or total == 7:
            return True
        else:
            if total < 10 or total == 0:
                return False
            else:
                return self.isHappy(total)