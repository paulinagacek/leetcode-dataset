class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        s=s.lower()
        a={\'0\',\'1\',\'2\',\'3\',\'4\',\'5\',\'6\',\'7\',\'8\',\'9\',\'a\',\'b\',\'c\',\'d\',\'e\',\'f\',\'g\',\'h\',\'i\',\'j\',\'k\',\'l\',\'m\',\'n\',\'o\',\'p\',\'q\',\'r\',\'s\',\'t\',\'u\',\'v\',\'w\',\'x\',\'y\',\'z\'}
        while (i<=j):
            while i<=j and s[i] not in a:
                i+=1
            while j>=i and s[j] not in a:
                j-=1
            if i<=j and s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True