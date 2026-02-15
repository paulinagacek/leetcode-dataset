class Solution:
    def backwardDistribution(self, ratings, start, end, candies):
        # Assign the max of current candies and one more then the next student candies to the current student if ratings of current student is more then the ratings of next student.
        for i in range(end - 1, start - 1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
    
    def forwardDistribution(self, ratings, start, end, candies):
        # Assign 1 candy more then the previous student to the current student if the ratings of current student is more then the previous student.
        for i in range(start, end):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        self.forwardDistribution(ratings, 1, n, candies)
        self.backwardDistribution(ratings, 0, n - 1, candies)
        return sum(candies)