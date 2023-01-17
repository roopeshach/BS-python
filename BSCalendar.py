from .BaseCalendar import BaseCalendar
from .map import DATE_MAP


class BSCalendar(BaseCalendar):
    def __init__(self, year_, month_, day_):
        super(BSCalendar, self).__init__(year_, month_, day_)
    
    def get_month_days_in_year(self, year):
        month_days = DATE_MAP.get(str(year), {})
        if not month_days:
            raise LookupError("Date range is not supported")
        return month_days['daysonmonth']
    
