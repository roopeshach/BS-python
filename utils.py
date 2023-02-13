import re


def decompose_date(date):
    """
        Gives tuple of year, month, day if format is valid else raise InvalidFormatException
        :param date:
        :return:
        """
    re_date_format = r'(\d{4})[\-\/](\d{1,2})[\-\/](\d{1,2})'

    valid_date = re.match(re_date_format, date)
    if not valid_date:
        raise ValueError("Invalid date format! Date should be of format yyyy-mm-dd")
    
    year, month, day = map(int, valid_date.groups())

    return year,month,day



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
    """
    Returns the full name of the weekday of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the full name of the weekday should be returned.
    :type lang: str, optional
    :return: full name of the weekday in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)
    >>> weekday__A(date_obj)
    'Wednesday'

    >>> weekday__A(date_obj, lang='np')
    'बुधबार'
    """


    en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    np = [u'सोमबार', u'मंगलबार', u'बुधबार', u'बिहिबार', u'शुक्रबार', u'शनिबार', u'आइतबार']

    if lang == 'en':
        return en[date_obj.weekday()]
    return np[date_obj.weekday()]

def weekday_as_dec__w(date_obj, lang='en'):
    """
    Returns the weekday of the given date_obj as a decimal number in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the weekday should be returned.
    :type lang: str, optional
    :return: weekday of the given date_obj as a decimal number in the specified language.

    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)
    >>> weekday_as_dec__w(date_obj)
    '2'

    >>> weekday_as_dec__w(date_obj, lang='np')
    '२'
    """
    if lang == 'en':
        return str(date_obj.weekday())
    return to_nepali_numbers(str(date_obj.weekday()))

def day_of_month__d(date_obj, lang='en'):
    """
    Returns the day of the month of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the day of the month should be returned.
    :type lang: str, optional
    :return: day of the month of the given date_obj in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> day_of_month__d(date_obj)
    '02'

    >>> day_of_month__d(date_obj, lang='np')
    '०२'
    """

    en = "%02d" % date_obj.day
    if lang == 'en':
        return en
    return to_nepali_numbers(en)

def month_abbr_b(date_obj, lang='en'):
    """
    Returns the abbreviation of the month of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the abbreviation of the month should be returned.
    :type lang: str, optional
    :return: abbreviation of the month of the given date_obj in the specified language.

    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> month_abbr_b(date_obj)
    'Nov'

    >>> month_abbr_b(date_obj, lang='np')
    'असो'
    """


    en = ['Bai', 'Jes', 'Ashr', 'Shr', 'Bhad', 'Ashoj', 'Kart', 'Mangs', 'Pous', 'Magh', 'Fal', 'Chait']
    ne = [u'बै', u'जेष्', u'आष', u'श्रा', u'भा', u'असो', u'कार्', u'मं', u'पौ', u'माघ', u'फा', u'चै']

    if lang == 'en':
        return en[date_obj.month - 1]
    return ne[date_obj.month - 1]

def month__B(date_obj, lang='en'):
    """
    Returns the full name of the month of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the full name of the month should be returned.
    
    :type lang: str, optional
    :return: full name of the month of the given date_obj in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> month__B(date_obj)
    'November'

    >>> month__B(date_obj, lang='np')
    'असोज'
    """

    en = ['Baishakh', 'Jestha', 'Ashad', 'Shrawan', 'Bhadra', 'Ashoj', 'Kartik', 'Mangsir', 'Poush', 'Magh', 'Falgun', 'Chaitra']
    ne = [u'बैशाख', u'जेष्ठ', u'आषाढ़', u'श्रावण', u'भाद्र', u'असोज', u'कार्तिक', u'मंसिर', u'पौष', u'माघ', u'फाल्गुन', u'चैत्र']

    if lang == 'en':
        return en[date_obj.month - 1]
    return ne[date_obj.month - 1]


def month_as_int__m(date_obj, lang='en'):
    """
    Returns the month of the given date_obj as a decimal number in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the month should be returned.
    :type lang: str, optional
    :return: month of the given date_obj as a decimal number in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> month_as_int__m(date_obj)
    '11'

    >>> month_as_int__m(date_obj, lang='np')
    '११'
    """
    en = "%02d" % date_obj.month
    if lang == 'en':
        return en
    return to_nepali_numbers(en)

def year_without_century__y(date_obj, lang='en'):
    """
    Returns the year of the given date_obj without the century in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the year should be returned.
    :type lang: str, optional
    :return: year of the given date_obj without the century in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> year_without_century__y(date_obj)
    '22'

    >>> year_without_century__y(date_obj, lang='np')
    '२२'
    """


    if lang == 'en':
        return str(date_obj.year)[2:]
    return to_nepali_numbers(str(date_obj.year[2:]))

def am_pm__p(date_obj, lang='en'):
    """
    Returns the AM/PM of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the AM/PM should be returned.
    :type lang: str, optional
    :return: AM/PM of the given date_obj in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2, 10, 30)

    >>> am_pm__p(date_obj)
    'AM'

    >>> am_pm__p(date_obj, lang='np')
    'पूर्वाह्न'
    """


    if lang == 'en':
        if date_obj.hour < 12:
            return 'AM'
        return 'PM'
    if date_obj.hour < 12:
        return u'पूर्वाह्न'
    return u'अपराह्न'

def hour_12__I(date_obj, lang='en'):
    """
    Returns the hour of the given date_obj in 12-hour format in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the hour should be returned.
    :type lang: str, optional
    :return: hour of the given date_obj in 12-hour format in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2, 10, 30)

    >>> hour_12__I(date_obj)
    '10'
    >>> hour_12__I(date_obj, lang='np')
    '१०'

    >>> date_obj = datetime(2022,11,2, 22, 30)
    >>> hour_12__I(date_obj)
    '10'
    >>> hour_12__I(date_obj, lang='np')
    '१०'

    """

    if lang == 'en':
        return "%02d" % (date_obj.hour % 12)
    return to_nepali_numbers("%02d" % (date_obj.hour % 12))

def hour_24__H(date_obj, lang='en'):
    """

    Returns the hour of the given date_obj in 24-hour format in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the hour should be returned.
    :type lang: str, optional
    :return: hour of the given date_obj in 24-hour format in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2, 10, 30)

    >>> hour_24__H(date_obj)
    '10'
    >>> hour_24__H(date_obj, lang='np')
    '१०'

    >>> date_obj = datetime(2022,11,2, 22, 30)
    >>> hour_24__H(date_obj)
    '22'
    >>> hour_24__H(date_obj, lang='np')
    '२२'

    """

    if lang == 'en':
        return "%02d" % date_obj.hour
    return to_nepali_numbers("%02d" % date_obj.hour)

def minute__M(date_obj, lang='en'):
    """
    Returns the minute of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the minute should be returned.
    :type lang: str, optional
    :return: minute of the given date_obj in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2, 10, 30, 45)

    >>> minute__M(date_obj)
    '30'
    >>> minute__M(date_obj, lang='np')
    '३०'
    """

    if lang == 'en':
        return "%02d" % date_obj.minute
    return to_nepali_numbers("%02d" % date_obj.minute)


def year__Y(date_obj, lang='en'):
    """
    Returns the year of the given date_obj in the specified language.

    :param date_obj: a Python `datetime` object representing a specific date
    :type date_obj: datetime
    :param lang: a string representing the language in which the year should be returned.
    :type lang: str, optional
    :return: year of the given date_obj in the specified language.
    :rtype: str

    :Example:
    >>> from datetime import datetime
    >>> date_obj = datetime(2022,11,2)

    >>> year__Y(date_obj)
    '2022'

    >>> year__Y(date_obj, lang='np')
    '२०२२'
    """

    if lang == 'en':
        return str(date_obj.year)
    return to_nepali_numbers(str(date_obj.year))

format_functions = {
    '%a' : weekday_abbr__a,
    '%A' : weekday__A,
    '%w' : weekday_as_dec__w,
    '%d' : day_of_month__d,
    '%b' : month_abbr_b,
    '%B' : month__B,
    '%m' : month_as_int__m,
    '%y' : year_without_century__y,
    '%p' : am_pm__p,
    "%Y" : year__Y,
    "%I" : hour_12__I,
    "%H" : hour_24__H,
    "%M" : minute__M,
    "%S" : lambda _ , __ : '00',
    "%f" : lambda _ , __ : '000000',
    "%X" : lambda _ , __ : '00:00:00',
    "%%" : lambda _ , __ : "%",

}