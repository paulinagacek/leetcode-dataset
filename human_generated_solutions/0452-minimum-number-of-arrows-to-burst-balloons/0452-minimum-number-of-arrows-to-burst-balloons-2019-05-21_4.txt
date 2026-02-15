class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key = lambda x: (x[1], x[1] - x[0])) # Sort by left cordinate, then by width
        last_shot = -float(\'inf\')
        shot_count = 0

        for baloon in sorted_points:
            if baloon[0] > last_shot:
                last_shot = baloon[1]
                shot_count += 1
                
        return shot_count