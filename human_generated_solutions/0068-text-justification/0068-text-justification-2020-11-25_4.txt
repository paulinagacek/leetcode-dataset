class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(part, totalLen):
        
            if len(part) == 1:
                return justifyLeft(part, totalLen)
            
            tatalSpaces = maxWidth - totalLen
            minSpaces = tatalSpaces // (len(part) - 1)
            extraSpaces = tatalSpaces % (len(part) - 1)
            
            spaces = [\'\'] * len(words)
            for i in range(1, len(words)):
                space = \' \' * minSpaces
                if extraSpaces > 0:
                    space += \' \'
                    extraSpaces -= 1
                spaces[i] = space

            return "".join(map(lambda x: x[0] + x[1], zip(spaces, part)))
        
        def justifyLeft(part, totalLen):
            extraSpaces = len(part) - 1 if len(part) >= 2 else 0             
            return " ".join(part) + \' \' * (maxWidth - totalLen - extraSpaces)
        
        result = []
        
        currentLen = 0
        current = []
        
        for word in words:
            spaces = len(current)
            
            if currentLen + len(word) + spaces > maxWidth:
                row = justify(current, currentLen)                    
                result.append(row)

                currentLen = 0                
                current = []
                
            current.append(word)
            currentLen += len(word)

        row = justifyLeft(current, currentLen)                    
        result.append(row)
            
        return result