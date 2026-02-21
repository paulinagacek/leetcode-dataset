class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = []
        d = []
        for i in logs:
            if i.split()[1].isdigit():
                d.append(i)
            else:
                l.append(i)
        l.sort(key = lambda x : x.split()[0])
        l.sort(key = lambda x : x.split()[1:])
        return l + d