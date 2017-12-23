import hitbtc
import polo
import time
import logging
from polo import Polo
from exchange import Exchange
from hitbtc import HitBTC
from bitstmp import Bitstmp
from bittrex_ex import Bittrex_ex


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

polo = Polo()
hitbtc = HitBTC()
bitstmp = Bitstmp()
my_bittrex = Bittrex_ex()


exchanges = []
exchanges.append(polo)
exchanges.append(hitbtc)
exchanges.append(bitstmp)
#exchanges.append(my_bittrex)

while (True):

    cryptos = ['BCH', 'ETH', 'BTC']

    for crypto in cryptos:

        #crypto = "BCH"
        sell_exchange = 0
        buy_exchange = 0
        highest_bid = -1
        lowest_ask = 10000000000000
        threshold = 0.02
        trade = {}

        for exchange in exchanges:
            ask = exchange.get_lowest_ask(crypto)
            bid = exchange.get_highest_bid(crypto)

            if bid > highest_bid:
                sell_exchange = exchange
                highest_bid = bid
            
            if ask < lowest_ask:
                buy_exchange = exchange
                lowest_ask = ask

        diff_in_price = highest_bid - lowest_ask
        perc_diff = (diff_in_price / lowest_ask)

        trade['crypto'] = crypto
        trade['sell_exchange'] = sell_exchange.get_exchange_name()
        trade['buy_exchange'] = buy_exchange.get_exchange_name()
        trade['sell_price'] = highest_bid
        trade['buy_price'] = lowest_ask
        trade['profit_perc'] = perc_diff - buy_exchange.get_make_fee() - sell_exchange.get_take_fee()

    #logger.info(trade)

    #buffer = "Calculating..."
    #buffer = buffer + "Sell on " + sell_exchange.get_exchange_name() + "... "
    #buffer = buffer + "Buy on " + buy_exchange.get_exchange_name() + "... " + str(perc_diff)
    #logger.info(buffer)

    if trade['profit_perc'] >= threshold:
        logger.info(trade)

    time.sleep(3)
