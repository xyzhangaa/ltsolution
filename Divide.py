
###Divide two integers without using multiplication, division and mod operator.
# Time:  O(logn)
# Space: O(1)

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0:
            return False
        if dividend == 0:
            return 0
        if (dividend < 0 and divisor >0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        count = 0
        res = 0
        max_int = 2147483647; min_int=-2147483648
        a=abs(divisor); b=abs(dividend)
        while b>=a:
            sum = a
            count =1
            while sum*2 <= b:
                sum += sum
                count += count
            b -= sum
            res += count
        if (dividend < 0 and divisor >0) or (dividend > 0 and divisor < 0):
            if res*(-1) < min_int:
                return min_int
            else:
                return res*(-1)
        else:
            if res > max_int:
                return max_int
            else:
                return res

if __name__ == "__main__":
    print Solution().divide(123, 12)
    print Solution().divide(123, -12)
    print Solution().divide(-123, 12)
    print Solution().divide(-123, -12)
