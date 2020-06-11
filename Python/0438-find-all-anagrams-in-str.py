class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        cs, cp = Counter(s[:len(p) -1]), Counter(p)

        for i in range(len(p)-1,len(s)):
            cs[s[i]] += 1

            if cs == cp:
                out.append(i - len(p)+1)
            cs[s[i - len(p)+1]] -= 1

            if cs[s[i - len(p)+1]] == 0:
                del cs[s[i - len(p)+1]]

        return out

