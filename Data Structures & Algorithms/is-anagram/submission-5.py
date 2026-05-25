class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1,map2 = {},{}

        for char in s:
            map1[char] = 1 + map1.get(char,0)
        for char in t:
            map2[char] = 1 + map2.get(char,0)

        return map1 == map2

        