from .BaseCalendar import BaseCalendar


class ADCalendar(BaseCalendar):
    """
        ADCalendar class inherits from BaseCalendar class and provides methods to determine the number of days in a month for a given year in the AD calendar.

        Attributes:
        year_ (int): the year of the calendar
        month_ (int): the month of the calendar
        day_ (int): the day of the calendar

        Methods:
        get_month_days_in_year(year: int) -> List[int]: Returns a list of integers representing the number of days in each month of the given year. If the year is a leap year, February will have 29 days.
        is_leap_year(year: int) -> bool: Returns True if the given year is a leap year, False otherwise. A leap year is a year that is divisible by 4, except for end-of-century years which must be divisible by 400.
    """
    def __iit__(self, year_, month_ , day_):
        super(ADCalendar, self).__init__(year_, month_, day_)

    def get_month_days_in_year(self, year):
        if self.is_leap_year(year):
            return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year):
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    return True
                return False
            return True
        return False