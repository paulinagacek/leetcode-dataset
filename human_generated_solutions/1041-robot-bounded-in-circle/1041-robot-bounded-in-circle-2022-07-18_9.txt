class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        hashmap={}
        start=[0,0]
        facing="N"
        LA={"N":"W","W":"S","S":"E","E":"N"}
        RC={"N":"E","E":"S","S":"W","W":"N"}
        res=[]
        for i in instructions:
            if i=="G":
                if facing=="N": start[1] += 1
                elif facing=="E": start[0] += 1
                elif facing=="W": start[0] -= 1
                elif facing=="S": start[1] -= 1
            elif i=="L":
                facing=LA[facing]
            elif i=="R":
                facing=RC[facing]
        if start==[0,0] or facing!="N": return True
        else: return False