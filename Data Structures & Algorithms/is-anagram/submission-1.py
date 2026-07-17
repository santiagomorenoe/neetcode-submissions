class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        h1map, h2map = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            h1map[s[i]] = 1 + h1map.get(s[i], 0)
            h2map[t[i]] = 1 + h2map.get(t[i], 0)
        for c in h1map: 
            if h1map[c] != h2map.get(c, 0):
                return False
        return True

        # return sorted(s) == sorted(t)
        # return Counter(s) == Counter(t)
 
        
        