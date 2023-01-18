import re


def decompose_date(date):

    pass


number_map = {
    "0": u"०",
    "1": u"१",
    "2": u"२",
    "3": u"३",
    "4": u"४",
    "5": u"५",
    "6": u"६",
    "7": u"७",
    "8": u"८",
    "9": u"९"
  }



def to_nepali_numbers(number):
    """
    Converts number to Nepali digits
    
    :param number: the number which needs to be converted to Nepali digits
    :type number: int or str
    :return: Nepali digits of the input number
    :rtype: str
    
    :Example:
    >>> to_nepali_numbers(123)
    '१२३'
    """
    number = str(number)
    return "".join([number_map[i] for i in number])




def weekday_abbr__a(date_obj, lang='en'):
    """
    Returns the abbreviation of the weekday of the given date_obj in the specified language.
    
    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the abbreviation of the weekday should be returned. 
    :type lang: str, optional
    :return: abbreviation of the weekday in the specified language.
    :rtype: str
    
    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)
    >>> weekday_abbr__a(date_obj)
    'Wed'
    >>> weekday_abbr__a(date_obj, lang='np')
    'बुध'
    """

    en = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    np = [u'सोम', u'मंगल', u'बुध', u'बिहि', u'शुक्र', u'शनि', u'आइत']

    if lang == 'en':
        return en[date_obj.weekday()]
    return np[date_obj.weekday()]

def weekday__A(date_obj, lang='en'):
    en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    np = [u'सोमबार', u'मंगलबार', u'बुधबार', u'बिहिबार', u'शुक्रबार', u'शनिबार', u'आइतबार']

    if lang == 'en':
        return en[date_obj.weekday()]
    return np[date_obj.weekday()]


format_functions = {
    '%a' : weekday_abbr__a,
    '%A' : weekday__A,
}