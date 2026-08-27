class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        allowed = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        allowed += allowed.lower()
        allowed += "0123456789"

        for string in s:
            if string in allowed:
                filtered += string.lower()

        return filtered == filtered[::-1]