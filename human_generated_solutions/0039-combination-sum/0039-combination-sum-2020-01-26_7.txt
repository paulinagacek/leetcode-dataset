class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        ret = []
        
        def fn(nums, tmp):
            if sum(tmp) > target:
                return False
            elif sum(tmp) == target:
                ret.append(tmp)
                return True
            else:   # sum(tmp) < target
                for i in range(len(nums)):
                    fn(nums[i:],tmp+[nums[i]])
        
        fn(candidates,[])
        return ret