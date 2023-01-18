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

    
    
class addate(datetime.date):
    def __init__(self, year, month , day):
        self.bs_year, self.bs_month, self.bs_day = _ad_to_bs(year, month, day)
    
    @property
    def bsdate(self):
        return bsdate(self.bs_year, self.bs_month, self.bs_day)
