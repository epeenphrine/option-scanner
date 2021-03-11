#%%
import re, json, datetime
from datetime import date
from yahoo_earnings_calendar import YahooEarningsCalendar
from config import date_delta

def get_earnings():
    '''
        get earnings date and ticker from yahoo calendar library
        save as format:
        [
            {
            ticker: 'string',
            date: 'string',
            },
            ...
        ]


    '''
    print('earnings date script started.......')
    def get_front_date(date_delta):
        dates_list = []
        for i in range(0, date_delta):
            d = datetime.date.today()
            d += datetime.timedelta(i)
            if d.weekday() == 4:
                dates_list.append(str(d))
        #print(dates_list[-2])
        return dates_list[-1]


    front_date = get_front_date(15)
    print(front_date)

    # ========= check earnings calendar ==========
    date_from = datetime.datetime.strptime(date.today().strftime('%Y-%m-%d') + " 05:00:00",  '%Y-%m-%d %X')
    date_to = datetime.datetime.strptime(front_date + " " + "18:00:00", '%Y-%m-%d %X')
    yec = YahooEarningsCalendar()
    earnings_list= []
    earnings_calendar = yec.earnings_between(date_from, date_to)

    if earnings_calendar:
        for company in earnings_calendar:
            earnings_dict = {}
            earnings_dict['ticker'] = company['ticker']
            earnings_dict['date'] = re.findall('\d\d\d\d-\d\d-\d\d',company['startdatetime'])[0]
            earnings_list.append(earnings_dict)
        with open('/tmp/json/companies_earnings.json', 'w') as f:
            json.dump(earnings_list, f)
    print('earnings date script finished !')
    print('check /tmp/json/ for earnings_date')
if __name__ == '__main__':
    get_earnings()
    print('script finished')