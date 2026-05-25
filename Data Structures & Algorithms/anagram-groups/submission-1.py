class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for word in strs:
            count =[0 for i in range(25)]
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            hashMap[tuple(count)].append(word)
        res = []
        for key,val in hashMap.items():
            res.append(val)
        return res
        