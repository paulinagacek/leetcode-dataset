class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter      = Counter(ransomNote)
        magazine_counter    = Counter(magazine)
        return ransom_counter == ransom_counter & magazine_counter