import hitbtc
import polo
import time
import logging
from polo import Polo
from exchange import Exchange
from hitbtc import HitBTC
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

polo = Polo()
#init_polo_balance = polo.get_balance_usd()
#logger.info ("Poloniex: " + '${:,.2f}'.format(init_polo_balance))

hitbtc = HitBTC()
#init_hit_balance = hitbtc.get_balance_usd()
#logger.info ("HitBTC: " + '${:,.2f}'.format(init_hit_balance) )
#logger.info ("Total: " + '${:,.2f}'.format(init_hit_balance + init_polo_balance))


while (True):

    polo_ask = polo.get_lowest_ask("BCH")
    hit_bid = hitbtc.get_highest_bid("BCH")
    if polo_ask < hit_bid:
        logger.INFO("Found..." + "POLO ASK: " + str(polo_ask) + ".... HIT BID: " + str(hit_bid))
    time.sleep(5)
