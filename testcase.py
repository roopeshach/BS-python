from BaseCalendar import BaseCalendar
import unittest
from .ADCalendar import ADCalendar
from .BSCalendar import BSCalendar

#create tests for BaseCalendar

class TestBaseCalendar(unittest.TestCase):
    def test_add_delta(self):
        """
        Test the add_delta method of BaseCalendar
        """
        #create a BaseCalendar object
        date = BaseCalendar(2016, 12, 31)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 1
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 2
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 2)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 3
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 4
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 5
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 5)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 6
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 6)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 7
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 7)
        #add 1 day to the date
        date.add_delta(1)
        #check if the date is 2017, 1, 8
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 8)

    def test_reduce_delta(self):
        """
        Test the reduce_delta method of BaseCalendar
        """
        #create a BaseCalendar object
        date = BaseCalendar(2017, 1, 8)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 7
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 7)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 6
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 6)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 5
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 5)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 4
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 4)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 3
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 3)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 2
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 2)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2017, 1, 1
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
        #reduce 1 day to the date
        date.reduce_delta(1)
        #check if the date is 2016, 12, 31
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 12)

    def test_add_delta_month(self):
        """
        Test the add_delta_month method of BaseCalendar
        """
        #create a BaseCalendar object
        date = BaseCalendar(2016, 12, 31)
        #add 1 month to the date
        date.add_delta_month(1)
        #check if the date is 2017, 1, 31
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 31)
        #add 1 month to the date
        date.add_delta_month(1)
        #check if the date is 2017, 2, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 2)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta_month(1)
        #check if the date is 2017, 3, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 3)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta(1)
        #check if the date is 2017, 4, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 4)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta_month(1)
        #check if the date is 2017, 5, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 5)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta(1)
        #check if the date is 2017, 6, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 6)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta(1)
        #check if the date is 2017, 7, 28
        self.assertEqual(date.year, 2017)
        self.assertEqual(date.month, 7)
        self.assertEqual(date.day, 28)
        #add 1 month to the date
        date.add_delta_month(1)

    def test_reduce_delta_month(self):
        """
        Test the reduce_delta_month method of BaseCalendar
        """
        #create a BaseCalendar object
        date = BaseCalendar(2017, 1, 31)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 12, 31
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 12)
        self.assertEqual(date.day, 31)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 11, 30
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 30)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 10, 31
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 10)
        self.assertEqual(date.day, 31)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 9, 30
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 9)
        self.assertEqual(date.day, 30)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 8, 31
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 8)
        self.assertEqual(date.day, 31)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 7, 31
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 7)
        self.assertEqual(date.day, 31)
        #reduce 1 month to the date
        date.reduce_delta(1)
        #check if the date is 2016, 6, 30
        self.assertEqual(date.year, 2016)
        self.assertEqual(date.month, 6)
        self.assertEqual(date.day, 30)
        #reduce 1 month to the date
        date.reduce_delta(1)


obj = TestBaseCalendar()
obj.test_add_delta()
obj.test_reduce_delta()
obj.test_add_delta_month()
obj.test_reduce_delta_month()