def isValid(self, s: str) -> bool:
        l = list()
        
        d = {\'}\':\'{\', \')\':\'(\', \']\':\'[\'}
        b_open = d.values()
        
        for b in s:
            if b in b_open:
                l.append(b)
            else:
                if len(l) > 0 and l[-1] == d[b]:
                        l.pop()
                else:
                    return False
        
        return len(l) == 0