class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1,map2  = {},{}
        for ele in s:
            map1[ele] = 1 + map1.get(ele,0)
               
        for ele in t:
            map2[ele] = 1 + map2.get(ele,0)
        return map1 == map2
        
                 

        