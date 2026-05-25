class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for words in strs:
            count = [0]* 26
            for char in words:
                count[ord("a") - ord(char)] += 1
            hmap[tuple(count)].append(words)
        return list(hmap.values())
        