class Solution:

    def encode(self, strs: List[str]) -> str:
        # 4#neet
        temp = ""

        for word in strs:
            temp +=  str(len(word))  + "#" +word 
        print(temp)
        return temp
        
        

    def decode(self, s: str) -> List[str]:

        l = 0
        res = []
        
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            length = int(s[l:j])
            res.append(s[j+1:j+length+1])
            print(res)
            l = j+length+1


        


        
        return res
