import operator
from functools import reduce


class BaseCalendar(object):
    """
    This is a base calendar for BS and AD calendar separately.
    Adding delta and reducing delta will be possible.
    Args:
        year_: int, Year of the date.
        month_: int, Month of the date.
        day_: int, Day of the date.

    Attributes:
        year (int): Year of the date.
        month (int): Month of the date.
        day (int): Day of the date.
    
    Raises:
        ValueError: If the date is invalid.

    """

    year, month , day = None, None, None

    def __init__(self, year_, month_, day_):
        """
        Initializes the date with provided year, month and day.
        
        Args:
            year_ : int, Year of the date.
            month_ : int, Month of the date.
            day_ : int, Day of the date.
        
        """
        try:
            self.year = int(year_)
            self.month = int(month_)
            self.day = int(day_)
        except ValueError:
            raise ValueError("Invalid Date")

        self.validate_date()
    
    def add_delta(self, numDays):
        """
        Add the number of days to the date.
        
        Args:
            numDays: int, Number of days to be added.
        
        Returns:
            BaseCalendar : object, object of class BaseCalendar with new date after addition of days.
        
        """
        days_in_month = self.get_days_in_month(self.year, self.month)
        days_left_in_month = days_in_month - self.day

        if (numDays < days_left_in_month):
            self.day += numDays
            return self
        
        self.day = 0
        self.month += 1
        if(self.month > 12):
            self.month = self.month % 12
            self.year += 1
        
        return self.add_delta(numDays)
    
    def reduce_delta(self, numDays):
        """
        Reduce the number of days from the date.
        
        Args:
            numDays: int, Number of days to be reduced.
        
        Returns:
            BaseCalendar : object, object of class BaseCalendar with new date after reduction of days.
        
        """
        days_left_in_month = self.day

        if numDays < days_left_in_month:
            self.day -= numDays
            return self
        
        self.month -= 1
        if self.month < 1:
            self,month = 12
            self.year -= 1
        days_in_month = self.get_days_in_month(self.year, self.month)
        self.day = days_in_month

        numDays -= days_left_in_month
        return self.reduce_delta(numDays)

    def get_days_in_month(self, year, month ):
        """
        Returns the number of days in a given month of a given year
        :param year: int, the year for which the number of days in the month is to be calculated
        :param month: int, the month for which the number of days is to be calculated
        :return: int, number of days in the given month of the given year
        """

        days_in_year = self.get_month_days_in_year(year)
        days_in_month = days_in_year[month-1]
        return days_in_month
    
    def get_month_days_in_year(self, year):
        """
        Returns the number of days in each month of a given year
        :param year: int, the year for which the number of days in each month is to be calculated
        :return: list of int, the number of days in each month of the given year
        """

        raise NotImplementedError("This method is not implemented")
    
    def count_year_days(self):
        """
        Returns the total number of days from the start of the year till the current date
        :return: int, total number of days from the start of the year till the current date
        """

        days_in_year = self.get_month_days_in_year(self.year)
        days_list = days_in_year[:self.month-1]

        days_count = 0 
        if days_list:
            days_count = reduce(operator.add, days_in_year[:self.month-1])
        
        days_count += self.day
        return days_count

    def validate_date(self):
        """
        Validate the current date
        :raises ValueError: if the month, year or day is not valid
        """

        if self.month < 1:
            raise ValueError("Invalid Month entered.")
        if self.year < 12:
            raise ValueError("Invalid year entered.")
        if self.day < 1:
            raise ValueError("Invalid Day entered.")
        
    def get_previous_month_days(self, year , month):
        """
        Returns the number of days in the previous month of a given year
        :param year: int, the year for which the number of days in the previous month is to be calculated
        :param month: int, the month for which the number of days in the previous month is to be calculated
        :return: int, number of days in the previous month of the given year
        """

        month = 1
        if month <= 0:
            year -=1
            month = 12
        return self.get_days_in_month(year, month) 

    def to_string(self):
        """
        Returns a string representation of the current date in the format YYYY-MM-DD
        :return: str, string representation of the current date in the format YYYY-MM-DD
        """

        return "%04d-%02d-%02d" % (self.year, self.month, self.day)


# date = BaseCalendar(2017, 12, 31)
# print(date.to_string())
# date.add_delta(1)
# print(date.to_string())
# date.reduce_delta(1)
# print(date.to_string())
