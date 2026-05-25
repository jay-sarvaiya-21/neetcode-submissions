class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang=collections.defaultdict(list)

        for word in strs:
            count=[0] * 26
            print(count)
            for letter in word:
                count[ord(letter)-ord("a")]+=1
            ang[tuple(count)].append(word)
        return ang.values()


