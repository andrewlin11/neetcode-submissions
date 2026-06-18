class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        return clean_s.upper() == clean_s[::-1].upper()