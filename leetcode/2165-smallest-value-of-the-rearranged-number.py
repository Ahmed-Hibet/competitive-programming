class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = False
        if num < 0:
            is_negative = True
            num *= -1

        sorted_num = sorted(str(num))
        if is_negative:
            return -1 * int(''.join(sorted_num[::-1]))

        for i in range(len(sorted_num)):
            if sorted_num[i] != '0':
                sorted_num[0], sorted_num[i] = sorted_num[i], sorted_num[0]
                break
        return int(''.join(sorted_num))
