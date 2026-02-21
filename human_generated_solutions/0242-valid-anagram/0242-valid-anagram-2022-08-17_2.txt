class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) != len(t): 
            flag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    flag = False
                    break
        return flag