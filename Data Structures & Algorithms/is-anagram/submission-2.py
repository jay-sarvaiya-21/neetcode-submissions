class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counterS={}
        counterT={}
        for n in s:
            if n not in counterS:
                counterS[n]=1
            else:
                counterS[n]+=1
        for n in t:
            if n not in counterT:
                counterT[n]=1
            else:
                counterT[n]+=1
        for key in counterS:
            if key not in counterT:
                return False
            if counterS[key]!= counterT[key]:
                return False
        return True


        