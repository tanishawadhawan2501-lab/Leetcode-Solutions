class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        n = num
        count = 0

        while n > 0:
            digit = n % 10

            if digit != 0 and num % digit == 0:
                count += 1

            n //= 10

        return count