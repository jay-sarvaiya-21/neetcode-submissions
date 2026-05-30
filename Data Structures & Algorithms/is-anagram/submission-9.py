class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}

        for i in range( len(s) ):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
        for i in range( len(t) ):   
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
        if freq_t.__eq__(freq_s):
            return True
        return False
       

       
        