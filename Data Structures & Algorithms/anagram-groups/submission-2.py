class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counter = defaultdict(list)

        for word in strs:
            alphabets = [0]* 26 
            for letter in word:
                alphabets[ord("a") - ord(letter)] += 1
            counter[tuple(alphabets)].append(word)
        print(counter.values())
        return list(counter.values())
            

