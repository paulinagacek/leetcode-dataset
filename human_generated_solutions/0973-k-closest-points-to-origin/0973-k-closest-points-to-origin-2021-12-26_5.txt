class Solution(object):
    def kClosest(self, points, k):
        def quickSelect(points, k):
            less, equal, greater = [], [], []
            pivot = random.choice(points)
            pivot_l2 = pivot[0] ** 2 + pivot[1] ** 2
            for p in points:
                p_l2 = p[0] ** 2 + p[1] ** 2
                if p_l2 < pivot_l2:
                    less.append(p)
                elif p_l2 > pivot_l2:
                    greater.append(p)
                else:
                    equal.append(p)
            if len(less) < k <= len(less) + len(equal):
                return less + equal[:k - len(less)]
            elif k <= len(less):
                return quickSelect(less, k)
            else:
                return less + equal + quickSelect(greater, k - len(less) - len(equal))
				
        return quickSelect(points, k)