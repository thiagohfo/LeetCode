class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        num_rev = str(x)[::-1]

        if num == num_rev:
            return True
        else:
            return False