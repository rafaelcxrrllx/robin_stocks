import robin_stocks.robinhood as r
import robin_stocks

login = r.login('', '')

my_stocks = r.build_holdings()
for key,value in my_stocks.items():
    print(key,value)

# optionData = robin_stocks.find_options_for_list_of_stocks_by_expiration_date(['fb','aapl','tsla','nflx'],
#              expirationDate='2024-06-21',optionType='call')
# for item in optionData:
#     print(' price -',item['strike_price'],' exp - ',item['expiration_date'],' symbol - ',
#           item['chain_symbol'],' delta - ',item['delta'],' theta - ',item['theta'])
