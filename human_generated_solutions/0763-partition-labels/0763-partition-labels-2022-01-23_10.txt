class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 1
        count = 0
        res = []
        while (i <len(s)+1):
            count += 1 # increasing count with every letter
            if not (set(s[:i]).intersection(set(s[i:]))):  # converting the blocks of string to sets and checking their intersection with the other set
                res.append(count) # storing the count when we get no intersection between sets
                count = 0 # resetting count to zero
            i += 1
        return res