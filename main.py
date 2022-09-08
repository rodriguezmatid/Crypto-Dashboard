from binance.spot import Spot
import requests
import telebot
import gspread
import dotenv as _dotenv
import os as _os

_dotenv.load_dotenv()

##################################################################################################################################
############################################################## DATA ##############################################################
##################################################################################################################################

B_API_KEY = _os.environ["BINANCE_API_KEY"]
B_SECURITY_KEY = _os.environ["BINANCE_SECURITY_KEY"]

client = Spot(B_API_KEY, B_SECURITY_KEY)

############ BINANCE #############
BTCUSDT_BINANCE = client.ticker_price("BTCUSDT")
BTCBUSD_BINANCE = client.ticker_price("BTCBUSD")
BTCUSDC_BINANCE = client.ticker_price("BTCUSDC")

BTCUSDT_BINANCE1 = round(float(BTCUSDT_BINANCE['price']),)
BTCBUSD_BINANCE1 = round(float(BTCBUSD_BINANCE['price']),)
BTCUSDC_BINANCE1 = round(float(BTCUSDC_BINANCE['price']),)

# print("############# BINANCE #############")
# print("BTCUSDT: " f"{BTCUSDT_BINANCE1}")
# print("BTCBUSD: " f"{BTCBUSD_BINANCE1}")
# print("BTCUSDC: " f"{BTCUSDC_BINANCE1}")
# print()

############ FTX #############
api_url_FTX_BTCUSD = 'https://ftx.us/api/markets/BTC/USD'
api_url_FTX_BTCUSDT = 'https://ftx.us/api/markets/BTC/USDT'

FTX_BTCUSD = round(requests.get(api_url_FTX_BTCUSD).json()['result']['price'],)
FTX_BTCUSDT = round(requests.get(api_url_FTX_BTCUSDT).json()['result']['price'],)

# print("############# FTX #############")
# print("BTCUSD: " f"{FTX_BTCUSD}")
# print("BTCUSDT: " f"{FTX_BTCUSDT}")
# print()

############# KuCoin #############
api_url_KuCoin_BTCUSDT = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT'

KUCOIN_BTCUSDT = round(float(requests.get(api_url_KuCoin_BTCUSDT).json()['data']['price']),)

# print("############# KuCoin #############")
# print("BTCUSDT: " f"{KUCOIN_BTCUSDT}")
# print()

############# BitStamp #############
api_url_BitStamp_BTCUSDT = 'https://www.bitstamp.net/api/v2/ticker/btcusdt'
api_url_BitStamp_BTCUSD = 'https://www.bitstamp.net/api/v2/ticker/btcusd'
api_url_BitStamp_BTCUSDC = 'https://www.bitstamp.net/api/v2/ticker/btcusc'

BITSTAMP_BTCUSDT = round(float(requests.get(api_url_BitStamp_BTCUSDT).json()['last']),)
BITSTAMP_BTCUSD = round(float(requests.get(api_url_BitStamp_BTCUSD).json()['last']),)

# print("############# BitStamp #############")
# print("BTCUSDT: " f"{BITSTAMP_BTCUSDT}")
# print("BTCUSD: " f"{BITSTAMP_BTCUSD}")
# print()

############# Bitfinex #############
api_url_Bitfinex_BTCUSD = 'https://api-pub.bitfinex.com/v2/ticker/tBTCUSD'
BITFINEX_BTCUSD = requests.get(api_url_Bitfinex_BTCUSD).json()[0]

# print("############# Bitfinex #############")
# print("BTCUSD: " f"{BITFINEX_BTCUSD}")
# print()

############# Kraken #############
api_url_Kraken_XBTUSD = 'https://api.kraken.com/0/public/Ticker?pair=XBTUSD'
KRAKEN_XBTUSD = round(float(requests.get(api_url_Kraken_XBTUSD).json()['result']['XXBTZUSD']['c'][0]),)

# print("############# Kraken #############")
# print("XBTUSD: " f"{KRAKEN_XBTUSD}")
# print()

############# Coinbase #############
api_url_Coinbase_BTCUSD = 'https://api.exchange.coinbase.com/products/BTC-USD/ticker'
COINBASE_BTCUSD = round(float(requests.get(api_url_Coinbase_BTCUSD).json()['price']),)

# print("############# Coinbase #############")
# print("BTCUSD: " f"{COINBASE_BTCUSD}")
# print()

post = ("BTC Price on Exchanges\n"
        "\n"
        "############# BINANCE #############\n"
        "BTCUSDT: " f"{BTCUSDT_BINANCE1}\n"
        "BTCBUSD: " f"{BTCBUSD_BINANCE1}\n"
        "BTCUSDC: " f"{BTCUSDC_BINANCE1}\n"
        "\n"
        "############# FTX #############\n"
        "BTCUSD: " f"{FTX_BTCUSD}\n"
        "BTCUSDT: " f"{FTX_BTCUSDT}\n"
        "\n"
        "############# KuCoin #############\n"
        "BTCUSDT: " f"{KUCOIN_BTCUSDT}\n"
        "\n"
        "############# BitStamp #############\n"
        "BTCUSDT: " f"{BITSTAMP_BTCUSDT}\n"
        "BTCUSD: " f"{BITSTAMP_BTCUSD}\n"
        "\n"
        "############# Bitfinex #############\n"
        "BTCUSD: " f"{BITFINEX_BTCUSD}\n"
        "\n"
        "############# Kraken #############\n"
        "XBTUSD: " f"{KRAKEN_XBTUSD}\n"
        "\n"
        "############# Coinbase #############\n"
        "BTCUSD: " f"{COINBASE_BTCUSD}\n")

##################################################################################################################################
############################################################## TELEGRAM ##########################################################
##################################################################################################################################

T_TOKEN = _os.environ["TELEGRAM_TOKEN"]
T_CID_CHANNEL_1 = _os.environ["CID_CHANNEL_1"]

bot_telegram = telebot.TeleBot(T_TOKEN)
bot_telegram.send_message(T_CID_CHANNEL_1, post)

##################################################################################################################################
############################################################## GOOGLE SHEET ######################################################
##################################################################################################################################

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("crypto-dashboard").sheet1

# Update a range of cells using the top left corner address
wks.update('C1', [[BTCUSDT_BINANCE1],
                  [BTCBUSD_BINANCE1], 
                  [BTCUSDC_BINANCE1], 
                  [FTX_BTCUSD], 
                  [FTX_BTCUSDT], 
                  [KUCOIN_BTCUSDT], 
                  [BITSTAMP_BTCUSDT], 
                  [BITSTAMP_BTCUSD], 
                  [BITFINEX_BTCUSD],
                  [KRAKEN_XBTUSD],
                  [COINBASE_BTCUSD]])