class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        running_line = []
        line_length = 0
        res = []
        for word in words:
            if line_length + len(running_line) + len(word) <= maxWidth:
                line_length += len(word)
                running_line.append(word)
            else:
                res.append(self._format(running_line, maxWidth))
                line_length = len(word)
                running_line = [word]
        if len(running_line):
            res.append(self._formatLast(running_line, maxWidth))
        return res

    def _format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        
        length = sum([len(word) for word in line])
        gaps = len(line) - 1
        s = line[0]
        for index, word in enumerate(line[1:]):
            if index < (maxWidth - length) % gaps:
                s = s + " " * ((maxWidth - length) // gaps) + " " + word
            else:
                s = s + " " * ((maxWidth - length) // gaps) + word
        return s
        
    def _formatLast(self, line, maxWidth):
        s = " ".join(line)
        return s + " " * (maxWidth - len(s))