class Solution:
    def frequencySort(self, s: str) -> str:
#         counts = Counter(s)
#         out = []

#         for char, count in counts.most_common():
#             out += char * count

#         return ''.join(out)
        return ''.join([char * count for char, count in Counter(s).most_common()])

