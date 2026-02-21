class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #check if some words in magazine matches ransomNote
        if ransomNote in magazine:
            return True
        
        #create a dictionary to store the frequency of char in ransomNote
        chars = dict()
        
        #write done how many times each char appears
        for i in ransomNote:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 0
                
        #check if frequency of each char in magazine is greater than in ransomNote
        for i in chars:
            if magazine.count(i) <= chars[i]: 
                return False
            
        return True