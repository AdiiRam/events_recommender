from dateutil.parser import *
from datetime import datetime

def is_future(start_date):

    try:            
        dt = parse(start_date)
        return dt > datetime.now()
    except Exception as err:
        return False

def readable_date_format(given_date):
        
        try:            
            dt = parse(given_date)
            return dt.strftime('%b %d,%Y %X')
        except Exception as err:
            return 'Not Available'