class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
    
        days = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]

        total = 0
        for y in range(1971, year):
            if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                total += 366
            else:
                total += 365
        month_days = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

        for m in range(1, month):
            total += month_days[m - 1]
            if m == 2 and (year % 400 == 0 or
                           (year % 4 == 0 and year % 100 != 0)):
                total += 1
        total += day - 1
        return days[(5 + total) % 7]   