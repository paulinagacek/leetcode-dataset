class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        for key, times in ransom_counter.items():
            if key not in magazine_counter: return False
            if magazine_counter[key] < times: return False
        return True