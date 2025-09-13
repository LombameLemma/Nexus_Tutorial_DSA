class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes.
        if x < 0:
            return False

        # Convert the integer to a string.
        s = str(x)

        # Reverse the string and compare it to the original.
        return s == s[::-1]

