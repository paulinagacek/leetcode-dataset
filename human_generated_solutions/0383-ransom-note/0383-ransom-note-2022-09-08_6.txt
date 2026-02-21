class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        if len(magazine) < len(ransomNote):
            return False
        
        else:
                
            for ransomNote_char in set(ransomNote):
                
                if ransomNote.count(ransomNote_char) > magazine.count(ransomNote_char):
                    return False
            
            return True