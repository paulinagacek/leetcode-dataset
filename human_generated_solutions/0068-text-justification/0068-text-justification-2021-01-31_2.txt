class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, cur = [], []
        chars = 0
        
        for word in words:
            # if cur is empty or the total chars + total needed spaces + next word fit
            if not cur or (len(word) + chars + len(cur)) <= maxWidth:
                cur.append(word)
                chars += len(word)
            else:
                # place spaces, append the line to the ans, and move on
                line = self.placeSpacesBetween(cur, maxWidth - chars)
                ans.append(line)
                cur.clear()
                cur.append(word)
                chars = len(word)
        
        # left justify any remaining text, which is easy
        if cur:
            extra_spaces = maxWidth - chars - len(cur) + 1
            ans.append(\' \'.join(cur) + \' \' * extra_spaces)
            
        return ans
    
    
    def placeSpacesBetween(self, words, spaces):
        if len(words) == 1: return words[0] + \' \' * spaces
        
        space_groups = len(words)-1
        spaces_between_words = spaces // space_groups
        extra_spaces = spaces % space_groups
        
        cur = []
        for word in words:
            cur.append(word)
            
            # place the min of remaining spaces or spaces between words plus an extra if available
            cur_extra = min(1, extra_spaces)
            spaces_to_place = min(spaces_between_words + cur_extra, spaces)

            cur.append(\' \' * spaces_to_place)
            
            if extra_spaces: extra_spaces -= 1
            spaces -= spaces_to_place
        
        return \'\'.join(cur)