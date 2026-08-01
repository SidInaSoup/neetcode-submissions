class Solution:
    def isPalindrome(self, s: str) -> bool:
         cleaned = []

         for char in s:
            if char.isalnum():
                cleaned.append(char.lower())

         cleaned_string = "".join(cleaned)

         return cleaned_string == cleaned_string[::-1]