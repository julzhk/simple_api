from __future__ import with_statement
import csv
import datetime


COLUMN_LABELS = ['Date', 'Symbol', 'TimeStamp', 'QuoteCount', 'TradeCount', 'OpenPx', 'ClosePx', 'HighPx', 'LowPx']
DATA_FILE = 'test_dataset.csv'


def TS_to_date(datestring):
    try:
        # convert with hours/mins/secs
        return datetime.datetime.strptime(datestring, "%Y-%m-%d %I:%M:%S")
    except ValueError:
        pass
    try:
        # convert without hours/mins/secs
        return datetime.datetime.strptime(datestring, "%Y-%m-%d")
    except ValueError:
        pass
    return ''


def conform_input_data(rowdict):
    """
        coerce data in each data row to format/type required
    """
    # rowdict['Value'] = float(rowdict['Value'])
    rowdict['TimeStamp'] = TS_to_date(rowdict['TimeStamp'][:19])
    for floatcolumn in ['LowPx','OpenPx','ClosePx','QuoteCount','HighPx','TradeCount']:
        if floatcolumn in rowdict:
            rowdict[floatcolumn] = float(rowdict[floatcolumn])
    return rowdict


def removed_fields(fields_to_show, rowdict):
    r = rowdict.copy()

    for rowcol in rowdict:
        if rowcol not in fields_to_show:
            del r[rowcol]
    return r


def conform_output_data(rowdict,fields_to_show=''):
    """
        coerce data in each data row to format/type required
    """
    rowdict['TimeStamp'] = str(rowdict['TimeStamp'])
    if fields_to_show:
        rowdict= removed_fields(fields_to_show, rowdict)
    return rowdict


def readdata(filename=DATA_FILE):
    """
        simple csv reader into a list of dicts; coerces some fields
    """
    with open(filename, 'rb') as f:
        datareader = csv.DictReader(f, delimiter=',')
        r = [conform_input_data(row) for row in datareader]
    return r


def date_compare(data, after_date=None, before_date=None):
    r = data
    if after_date:
        r = [d for d in r if d['TimeStamp'] > after_date]
    if before_date:
        r = [d for d in r if d['TimeStamp'] < before_date]
    return r

