
# Python BSDATE - A Python module for the BSDATE format

BSDATE is a simple date format that is easy to read and write. 
It provides a simple way to represent dates in BS format.

## Approach

Create a BaseCalendar which will distinguish between the two calendars. (AD and BS)

AD Calendar and BS Calendar will be implemented which inherits the BaseCalendar

The BaseCalendar will have the following methods:

- `add_delta()`
- `reduce_delta()`
- `count_year_days()`
-  `get_days_in_month()`
- `get_month_days_in_year()`
- `validate_date()`

The BaseCalendar will have the following properties: (year, month, day) from which a calendar is initialized.

### AD Calendar





