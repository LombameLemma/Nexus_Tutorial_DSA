class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        def compare(x: str, y: str) -> int:
            # Return -1 to place x before y
            if x + y > y + x:
                return -1
            # Return 1 to place y before x
            elif x + y < y + x:
                return 1
            else:
                return 0

        sorted_nums = sorted(str_nums, key=cmp_to_key(compare))

        # Handle the edge case where all numbers are zero
        if sorted_nums and sorted_nums[0] == "0":
            return "0"

        return "".join(sorted_nums)
