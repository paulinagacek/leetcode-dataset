class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = float("inf")
        maximum = float("-inf")
        
        i = 0
        sums = 0
        while i<len(salary):
            minimum = min(minimum, salary[i])
            maximum = max(maximum, salary[i])
            sums+=salary[i]
            i+=1
        
        return (sums - (maximum+minimum))/(i-2)