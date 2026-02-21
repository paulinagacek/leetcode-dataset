class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line, width = [], 0
        
        for word in words: 
            if width + len(line) + len(word) > maxWidth: 
                n, k = divmod(maxWidth - width, max(1, len(line)-1))
                for i in range(max(1, len(line)-1)): 
                    line[i] += " " * (n + (i < k))
                ans.append("".join(line))
                line, width = [], 0
            line.append(word)
            width += len(word)
            
        ans.append(" ".join(line).ljust(maxWidth))
        return ans