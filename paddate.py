"""
Pad a ISO-formatted date to supply missing month and day components.
Accounts for negative years (BCE) and for very large dates.
"""

import re

RE_YEARMONTHDAY = re.compile(r'^(\-?\+?)(\d+)\-(\d\d)\-(\d\d)$')
RE_YEARMONTH = re.compile(r'^(\-?\+?)(\d+)\-(\d\d)$')
RE_YEARONLY = re.compile(r'^(\-?\+?)(\d+)$')


def paddate(datestring, startend='start'):
    if startend not in ('start', 'end'):
        raise ValueError("The v parameter must be 'start' or 'end'")

    if re.match(RE_YEARMONTHDAY, datestring):  # already yyyy-mm-dd so return as-is
        return datestring

    isyearmonth = re.match(RE_YEARMONTH, datestring)
    isyearonly = re.match(RE_YEARONLY, datestring)

    if isyearmonth:
        (plusminus, yearstring, monthstring) = isyearmonth.groups()

        if not _isvalidmonth(monthstring):
            raise ValueError("Month {} is not 01 through 12".format(monthstring))

        return _padyearandmonth(plusminus, yearstring, monthstring, startend)
    elif isyearonly:
        (plusminus, yearstring) = isyearonly.groups()
        return _padyearonly(plusminus, yearstring, startend)
    else:
        raise ValueError("Cannot parse {}".format(datestring))


def _padyearandmonth(plusminus, yearstring, monthstring, startend):
    daybit = '01' if startend == 'start' else _daysinmonth(yearstring, monthstring)
    return "{}{}-{}-{}".format(plusminus, yearstring, monthstring, daybit)


def _padyearonly(plusminus, yearstring, startend):
    monthandday = ('01', '01') if startend == 'start' else ('12', '31')
    return "{}{}-{}-{}".format(plusminus, yearstring, monthandday[0], monthandday[1])


def _isvalidmonth(monthstring):
    validmonths = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
    return monthstring in validmonths


def _daysinmonth(yearstring, monthstring):
    monthdaycounts = {
        '01': 31,
        '02': 28,  # February
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31,
    }

    if _isleapyear(yearstring):
        monthdaycounts['02'] = 29

    return monthdaycounts[monthstring]


def _isleapyear(yearstring):
    yearnumber = int(yearstring)
    isleap = yearnumber % 4 == 0 and (yearnumber % 100 != 0 or yearnumber % 400 == 0)
    return isleap
