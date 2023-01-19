import datetime

from .utils import format_functions
from .DateConverter import _ad_to_bs, _bs_to_ad

class bsdate(datetime.date):
    def __new__(cls, year, month, day):
        ad_year, ad_month, ad_day = _bs_to_ad(year, month, day)
        return datetime.date.__new__(cls, ad_year, ad_month, ad_day)
    
    def __init__(self, year, month, day):
        self.bs_year, self.bs_month , self.bs_day = year, month, day
    
    @property
    def year(self):
        return self.bs_year
    
    @property
    def month(self):
        return self.bs_month

    @property
    def day(self):
        return self.bs_day
    
    @property
    def addate(self):
        ad_year, ad_month, ad_day = _bs_to_ad(self.bs_year, self.bs_month, self.bs_day)
        return addate(ad_year, ad_month, ad_day)

    def strftime(self, format, lang="en"):
        for key in format_functions:
            format = format.replace(key, format_functions[key](self, lang))
        
        return format
    
    def ctime(self, lang="en"):
        return self.strftime(u"%a %b %d 00:00:00 %Y", lang)
    
    def isoformat(self, lang="en"):
        return self.strftime(u"%Y-%m-%d", lang)
    
    def timetuple(self):
        return self.addate.timetuple()
    
    def toordinal(self):
        return self.addate.toordinal()
    
    def replace(self, year=None, month=None, day=None):
        self.bs_year = year or self.bs_year
        self.bs_month = month or self.bs_month
        self.bs_day = day or self.bs_day

        return bsdate(self.bs_year, self.bs_month, self.bs_day)
    

    @classmethod
    def fromordinal(cls, n):
        ordinal_date = super(bsdate, cls).fromordinal(n)
        return cls.fromdateobj(ordinal_date)
    
    @classmethod
    def fromdateobj(clas, d):
        bs_year, bs_month, bs_day = _ad_to_bs(d.year, d.month, d.day)
        return bsdate(bs_year, bs_month, bs_day)

    @classmethod
    def fromtimestamp(cls, n):
        timestamp_date = super(bsdate, cls).fromtimestamp(n)
        return cls.fromdateobj(timestamp_date)
    
    @classmethod
    def today(cls):
        return cls.fromdateobj(datetime.date.today())
    

    
class addate(datetime.date):
    def __init__(self, year, month , day):
        self.bs_year, self.bs_month, self.bs_day = _ad_to_bs(year, month, day)
    
    @property
    def bsdate(self):
        return bsdate(self.bs_year, self.bs_month, self.bs_day)
