from hitbtc_client import Client
import uuid
import util as Util
import logging
from exchange import Exchange
import json

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

logger = logging.getLogger(__name__)

trade = True

class HitBTC (Exchange):

    hit_client = 0

    def __init__(self): 
        self.hit_client =  Client("https://api.hitbtc.com", config["hitbtc"]["key"], config["hitbtc"]["secret"])
    
    def get_balance_usd (self):
        balances = self.hit_client.get_trading_balance()
        usd_balance = 0
        for balance in balances:
          
            if balance['currency'] == 'ETH':
                usd_balance = usd_balance + float(balance['available']) * float(self.hit_client.get_orderbook("ETHUSD")['bid'][0]['price'])
            elif balance['currency'] == 'BCH':
                usd_balance = usd_balance + float(balance['available']) * float(self.hit_client.get_orderbook("BCHUSD")['bid'][0]['price'])
            elif balance['currency'] == 'ZEC':
                usd_balance = usd_balance + float(balance['available']) * float(self.hit_client.get_orderbook("ZECUSD")['bid'][0]['price'])
            elif balance['currency'] == 'DASH':
                usd_balance = usd_balance + float(balance['available']) * float(self.hit_client.get_orderbook("DASHUSD")['bid'][0]['price'])
            elif balance['currency'] == 'BTC':
                usd_balance = usd_balance + float(balance['available']) * float(self.hit_client.get_orderbook("BTCUSD")['bid'][0]['price'])
            elif balance['currency'] == 'USD':
                usd_balance = usd_balance + float(balance['available'])
        return usd_balance


    def get_balance (self, _crypto):
        balances = self.hit_client.get_trading_balance()
        for balance in balances:
            if balance['currency'] == _crypto:
                return float(balance['available'])


    def get_lowest_ask (self, _crypto):
        asks = self.hit_client.get_orderbook(_crypto + "USD")['ask']
        lowestAsk = 10000000
        for ask in asks:
            ask_price = float(ask["price"])
            if ask_price < lowestAsk:
                lowestAsk = ask_price
        return lowestAsk

    def get_highest_bid (self, _crypto):
        bids = self.hit_client.get_orderbook(_crypto + "USD")['bid']
        highest_bid = 0
        for bid in bids:
            bid_price = float(bid["price"])
            if bid_price > highest_bid:
                highest_bid = bid_price
        return highest_bid


