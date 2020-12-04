#%%
# "https://stackoverflow.com/questions/9539921/how-do-i-create-a-python-function-with-optional-arguments"
# "https://www.programiz.com/python-programming/args-and-kwargs" 

import json
import datetime

def get_front_date(date_delta):
        dates_list = []
        for i in range(0, date_delta):
            d = datetime.date.today()
            d += datetime.timedelta(i)
            if d.weekday() == 4:
                dates_list.append(str(d))
        #print(dates_list[-2])
        return dates_list[-2]

def get_back_date(date_delta):
    dates_list = []
    for i in range(0, date_delta):
        d = datetime.date.today()
        d += datetime.timedelta(i)
        if d.weekday() == 4:
            dates_list.append(str(d))
    #print(dates_list[-1])
    return dates_list[-1]

def user_filter_json(**data): ## pass in multiple paramters
    print('in user filter json')
    #print(data)
    date_delta = data['date_delta']
    goldenRatio = data['goldenRatio']
    totalVolume = data['totalVolume']
    openInterest = data['openInterest']
    print(data)
    with open('callie_scripts/option_chains_list.json') as f:
        option_chains_list = json.load(f) 
    option_dates = list(option_chains_list[0]['callExpDateMap'].keys())
    front_date = get_front_date(date_delta)
    back_date = get_back_date(date_delta)
    option_dates_filter = []
    option_filter_list = []
    ## new option dates using get date functions 
    for option_date in option_dates:
        if front_date in option_date:
            option_dates_filter.append(option_date)
        if back_date in option_date:
            option_dates_filter.append(option_date)
    print(option_dates_filter)
    for option in option_chains_list:
        try:
            option_dict = {}
            name = option['underlying']['symbol']
            option = option['callExpDateMap']
            first_date = option[option_dates_filter[0]]
            second_date = option[option_dates_filter[1]]
            strikes = list( first_date.keys() ) ## list of strikes  given date

            option_dict['ticker']  = name
            option_dict['strikes'] = []
            option_dict['goldenRatio'] = []

            for strike in strikes:
                # variables to filter calendar 
                first_date_strike = first_date[strike][0]
                second_date_strike = second_date[strike][0]

                golden_ratio = first_date_strike['mark'] / second_date_strike['mark'] ## bid, ask, mark, last ['']
                total_volume = first_date_strike['totalVolume'] + second_date_strike['totalVolume']
                open_interest = first_date_strike['openInterest'] + second_date_strike['openInterest']

                volatility = first_date_strike['volatility']
                theoreticalOptionValue = first_date_strike['theoreticalOptionValue']

                if golden_ratio >= goldenRatio and total_volume >= totalVolume and open_interest >= openInterest: 
                    option_dict['strikes'].append(strike) 
                    option_dict['goldenRatio'].append(round(golden_ratio, 3)) 
                    option_dict['dates'] = [option_dates_filter[0], option_dates_filter[1]]
            if option_dict['strikes']:
                option_filter_list.append(option_dict)
        except:
            #print("error iterating in option_chains_list")
            pass
    return option_filter_list 
# %%
