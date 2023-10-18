class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(letter.lower() for letter in s if letter.isalnum())


        if word == word[::-1]:
            return True
        
        return False
