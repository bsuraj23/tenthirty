class Solution:
    def isValid(self, word:str) -> bool:
        if len(word)<3:
            return False
        vowels=set("AEIOUaeiou")
        has_vowels=False
        has_consonants=False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.alpha():
                has_vowels=True
            else:
                has_consonants=True
        return has_vowels and has_consonants