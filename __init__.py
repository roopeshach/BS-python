from .DateConverter import _ad_to_bs, _bs_to_ad

def BS2AD(year, month, day):
    """
    Converts the given date in BS to AD.

    Args:
        year: int, Year in BS.
        month: int, Month in BS.
        day: int, Day in BS.

    """
    return _bs_to_ad(year, month, day)

def AD2BS(year, month, day):
    """
    Converts the given date in AD to BS.

    Args:
        year: int, Year in AD.
        month: int, Month in AD.
        day: int, Day in AD.

    """
    
    return _ad_to_bs(year, month, day)
