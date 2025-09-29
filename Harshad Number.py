class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digit = 0
        digit = x
        while digit:
            sum_of_digit += digit%10
            digit//=10
        return sum_of_digit if x%sum_of_digit == 0 else -1
