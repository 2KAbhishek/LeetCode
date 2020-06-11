class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1, count2, l1, l2 = Counter(s1), Counter(s2[:len(s1)]), len(s1), len(s2)

        for i in range(l1, l2):
            if count1 == count2: return True

            count2[s2[i]] += 1
            count2[s2[i-l1]] -= 1
            if count2[s2[i-l1]] == 0:
                del count2[s2[i-l1]]


        return count1 == count2

