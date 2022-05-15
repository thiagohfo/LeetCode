class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s.strip() == '':
            return True

        result = re.sub(r'[^a-zA-Z0-9]', '', s)
        result = result.lower()

        for i in range(len(result)):
            if result[i] != result[(len(result) - 1) - i]:
                return False1

        return True