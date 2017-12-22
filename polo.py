from poloniex import Poloniex
import util as Util
from exchange import Exchange
import logging
import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

logger = logging.getLogger(__name__)

trade = True

class Polo (Exchange):

    trade = False
    polon = 0

    def __init__(self): 
        self.polon = Poloniex()
        self.polon.key = config['polo']['key']
        self.polon.secret = config['polo']['secret']
    
    def short_crypto (self, _crypto, _quantity, _price):
        symbol = "USDT_" + _crypto
        if trade:
            order = self.polon.sell(symbol, _price, _quantity)
        logger.info ("Poloniex short " + _crypto + ". Quantity: " + Util.float_to_str(_quantity) + ", Price: " + str(_price))

    def long_crypto (self, _crypto, _quantity, _price):
        symbol = "USDT_" + _crypto
        if trade:
            order = self.polon.buy(symbol, _price, _quantity)
        logger.info ("Poloniex short " + _crypto + ". Quantity: " + Util.float_to_str(_quantity) + ", Price: " + str(_price))

    def get_balance_usd (self):
        balance = float(self.polon.returnTicker()['USDT_ETH']['last']) * float (self.polon.returnBalances()['ETH'])
        balance = balance + float(self.polon.returnTicker()['USDT_DASH']['last']) * float (self.polon.returnBalances()['DASH'])
        balance = balance + float(self.polon.returnTicker()['USDT_ZEC']['last']) * float (self.polon.returnBalances()['ZEC'])
        balance = balance + float(self.polon.returnTicker()['USDT_BCH']['last']) * float (self.polon.returnBalances()['BCH'])
        balance = balance + float(self.polon.returnTicker()['USDT_BTC']['last']) * float (self.polon.returnBalances()['BTC'])
        balance = balance + float (self.polon.returnBalances()['USDT'])
        return balance  

    def get_lowest_ask (self, _crypto):
        asks = self.polon.returnOrderBook()['USDT_BCH']['asks']
        lowestAsk = 10000000
        for ask in asks:
            ask_price = float(ask[0])
            if ask_price < lowestAsk:
                lowestAsk = ask_price
        return lowestAsk

    def get_highest_bid (self, _crypto):
        bids = self.polon.returnOrderBook()['USDT_BCH']['bids']
        highest_bid = 0
        for bid in bids:
            bid_price = float(bid[0])
            if bid_price > highest_bid:
                highest_bid = bid_price
        return highest_bid

