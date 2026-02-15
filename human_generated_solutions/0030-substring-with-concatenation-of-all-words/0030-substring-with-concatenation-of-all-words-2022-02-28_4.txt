class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        counter = collections.Counter(words)
        window_size = len(words) * word_len
        ans = []
        for i in range(len(s) - window_size + 1):
            temp = s[i:i+window_size]
            temp = [temp[j:j+word_len] for j in range(0, window_size, word_len)]
            if collections.Counter(temp) == counter:
                ans.append(i)
        return ans