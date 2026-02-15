class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        s = text.split(" ")
        
        while "" in s :
            s.remove("")
            
        if len(s) == 1:
            return s[0] + " "*spaces
        
        #min no of spaces between each word
        nsw = spaces//(len(s)-1)
        #no. of spaces left 
        nsl = spaces%(len(s)-1)
        result = ""
        for i in range(len(s)) :
            if i != len(s)-1 :
                result += s[i] + (" ")*nsw
                if nsl > 0:
                    result += " "
                    nsl -= 1
            else:
                result += s[i]  
        return result
            

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        result = []
        
        last = words.pop(0)
        while words:
            if len(last) + len(words[0])  >= maxWidth :
                t = last + (" ")*(maxWidth-len(last))
                last = words.pop(0)
                result.append(t)
            
            elif len(last) + len(words[0]) < maxWidth :
                last = last + " " + words.pop(0)             
        result.append(last + (" ")*(maxWidth-len(last)))
        
        for i in range(len(result)-1):
            result[i] = self.reorderSpaces(result[i])
            
            
        return result