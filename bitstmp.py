
from exchange import Exchange
import bitstamp.client

import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

class Bitstmp (Exchange):

    trade = False
    public_client = 0
    trading_client = 0

    def __init__(self): 
        self.public_client = bitstamp.client.Public()
        self.trading_client = bitstamp.client.Trading(
            username=config['bitstamp']['username'], 
            key=config['bitstamp']['key'], 
            secret=config['bitstamp']['secret'])

    def get_exchange_name (self):
        return "Bitstamp"

    def get_make_fee(self):
        return 0.0025

    def get_take_fee(self):
        return 0.0025
    #def short_crypto (self, _crypto, _quantity, _price):
        #symbol = "USDT_" + _crypto
        #if trade:
        #    order = self.polon.sell(symbol, _price, _quantity)
        #logger.info ("Poloniex short " + _crypto + ". Quantity: " + Util.float_to_str(_quantity) + ", Price: " + str(_price))

    #def long_crypto (self, _crypto, _quantity, _price):
        #symbol = "USDT_" + _crypto
        #if trade:
        #    order = self.polon.buy(symbol, _price, _quantity)
        #logger.info ("Poloniex short " + _crypto + ". Quantity: " + Util.float_to_str(_quantity) + ", Price: " + str(_price))

    def get_lowest_ask (self, _crypto):
        asks = self.public_client.order_book(base=_crypto)['asks']
        lowest_ask = 1000000000
        for ask in asks:
            ask_price = float(ask[0])
            if ask_price < lowest_ask:
                lowest_ask = ask_price
        return lowest_ask

    def get_highest_bid (self, _crypto):
        bids = self.public_client.order_book(base=_crypto)['bids']
        highest_bid = 0
        for bid in bids:
            bid_price = float(bid[0])
            if bid_price > highest_bid:
                highest_bid = bid_price
        return highest_bid

    def get_balance_usd (self):
        balance = float(self.trading_client.account_balance(base="eth")['eth_balance']) * float(self.public_client.order_book(base="eth")["asks"][0][0])           
        balance = balance + float(self.trading_client.account_balance(base="btc")['btc_balance']) * float(self.public_client.order_book(base="btc")["asks"][0][0])
        balance = balance + float(self.trading_client.account_balance(base="ltc")['ltc_balance']) * float(self.public_client.order_book(base="ltc")["asks"][0][0])
        balance = balance + float(self.trading_client.account_balance(base="bch")['bch_balance']) * float(self.public_client.order_book(base="bch")["asks"][0][0])
        balance = balance + float(self.trading_client.account_balance(base="xrp")['xrp_balance']) * float(self.public_client.order_book(base="xrp")["asks"][0][0])
        return balance

#public_client = bitstamp.client.Public()
#print(public_client.ticker()['volume'])


#trading_client = 
#print(trading_client.account_balance()['fee'])

#print(trading_client.ticker()['volume'])   # Can access public methods
