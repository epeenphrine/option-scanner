#%%
# "https://stackoverflow.com/questions/9539921/how-do-i-create-a-python-function-with-optional-arguments"
# "https://www.programiz.com/python-programming/args-and-kwargs" 

import json
import datetime

json_file_path_test = '/tmp/optionChainsList.json'
json_file_path = '/tmp/json/optionChainsList.json'

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

def get_callies(**data): ## pass in multiple paramters
    '''
    get_callies(days, ratio, volume, openinterest)
    use option_chains_list.json to filter for calendars with good ratios
    and return a dictionary  
    '''
    print('in filter json')
    #print(data)
    date_delta = data['date_delta']
    goldenRatio = data['goldenRatio']
    totalVolume = data['totalVolume']
    openInterest = data['openInterest']
    print(data)
    with open(json_file_path) as f:
        option_chains_list = json.load(f)['optionChainsList']
    # print(option_chains_list)
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
    if len(option_dates_filter) != 2:
        message = "we only have one date from option_dates_filter ... maybe holiday on next friday?"
        return message 

    for option in option_chains_list:
        try:
            option_dict = {}
            name = option['underlying']['symbol']
            underlying_price =  option['underlyingPrice']
            option = option['callExpDateMap']
            first_date = option[option_dates_filter[0]]
            second_date = option[option_dates_filter[1]]
            strikes = list( first_date.keys() ) ## list of strikes  given date

            option_dict['ticker']  = name
            option_dict['strikes'] = []
            option_dict['goldenRatio'] = []
            option_dict['prices'] = []
            option_dict['underlyingPrice'] = round(underlying_price, 2)

            for strike in strikes:
                # variables to filter calendar 
                first_date_strike = first_date[strike][0]
                second_date_strike = second_date[strike][0]

                golden_ratio = first_date_strike['mark'] / second_date_strike['mark'] ## bid, ask, mark, last ['']
                price = second_date_strike['mark'] - first_date_strike['mark']
                total_volume = first_date_strike['totalVolume'] + second_date_strike['totalVolume']
                open_interest = first_date_strike['openInterest'] + second_date_strike['openInterest']

                volatility = first_date_strike['volatility']
                theoreticalOptionValue = first_date_strike['theoreticalOptionValue']

                if golden_ratio >= goldenRatio and total_volume >= totalVolume and open_interest >= openInterest: 
                    option_dict['strikes'].append(strike) 
                    option_dict['goldenRatio'].append(round(golden_ratio, 3)) 
                    option_dict['dates'] = [option_dates_filter[0], option_dates_filter[1]]
                    option_dict['prices'].append(round(price, 3))
            if option_dict['strikes']:
                option_filter_list.append(option_dict)
        except:
            print("error iterating in option_chains_list")
    return option_filter_list 