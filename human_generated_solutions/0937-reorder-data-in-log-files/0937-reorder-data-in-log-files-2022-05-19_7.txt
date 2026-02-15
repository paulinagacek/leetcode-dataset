class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def sorting_algorithm(log):
            left_id, right_resting = log.split(" ", 1)

            if right_resting[0].isalpha():
                return (0, right_resting, left_id)
            else:
                return (1, None, None)

        return sorted(logs, key=sorting_algorithm)