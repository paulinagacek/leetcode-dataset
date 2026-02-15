class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from itertools import permutations
        mylist = [1, 22, 122, 333, 1333, 4444, 14444, 22333, 55555, 122333, 155555, 224444, 666666,1224444]
        res=[]
        def digit_combination(a,length):
            a = list(str(a))
            comb = permutations(a, length)
            for each in comb:
                s = [str(i) for i in each]
                result = int("".join(s))
                res.append(result)
        for every in mylist:
            digit_combination(every,len(str(every)))
        res.sort()
        print(res)
        for idx in res:
            if(idx>n):
                return idx