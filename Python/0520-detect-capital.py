class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.upper(), word.lower(), word.capitalize())
#         if word.isupper():
#             return True
#         if word.islower():
#             return True
#         if word.istitle():
#             return True
#         return False

