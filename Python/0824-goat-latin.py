class Solution:
    def toGoatLatin(self, S: str) -> str:
        # Avoid string concatenations, they are costly in python (immutable)
        words = S.split()

        vowels = set(list("aeiouAEIOU"))
        out = []
        for num, word in enumerate(words):
            if word[0] in vowels:
                out.append(word + "ma" + ("a" * (num+1)))
            else:
                out.append(word[1:] + word[0] + "ma" + ("a" * (num+1)))

        return " ".join(out)

