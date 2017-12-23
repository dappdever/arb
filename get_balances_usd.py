import hitbtc
import polo
import time
import logging
from polo import Polo
from exchange import Exchange
from hitbtc import HitBTC
from bitstmp import Bitstmp

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

init_balance = 0

polo = Polo()
init_polo_balance = polo.get_balance_usd()
logger.info ("Poloniex: " + '${:,.2f}'.format(init_polo_balance))

bitstmp = Bitstmp()
init_bitstmp_balance = bitstmp.get_balance_usd()
logger.info ("Bitstamp: " + '${:,.2f}'.format(init_bitstmp_balance))

hitbtc = HitBTC()
init_hit_balance = hitbtc.get_balance_usd()
logger.info ("HitBTC: " + '${:,.2f}'.format(init_hit_balance) )
logger.info ("Total: " + '${:,.2f}'.format(init_hit_balance + init_polo_balance + init_bitstmp_balance))


while (True):

    balance = 0

    polo_balance = polo.get_balance_usd()
    perc_diff = (polo_balance - init_polo_balance) / init_polo_balance
    logger.info ("Poloniex: " + '${:,.2f}'.format(polo_balance) + " -- Change: " + str("{0:.2f}".format(perc_diff * 100) + "%"))

    bitstmp_balance = bitstmp.get_balance_usd()
    perc_diff = (bitstmp_balance - init_bitstmp_balance) / init_bitstmp_balance
    logger.info ("Bitstamp: " + '${:,.2f}'.format(bitstmp_balance) + " -- Change: " + str("{0:.2f}".format(perc_diff * 100) + "%"))

    hit_balance = hitbtc.get_balance_usd()
    perc_diff = (hit_balance - init_hit_balance) / init_hit_balance
    logger.info ("HitBTC: " + '${:,.2f}'.format(hit_balance) + " -- Change: " + str("{0:.2f}".format(perc_diff * 100) + "%"))

    perc_diff = ( ((hit_balance + polo_balance + bitstmp_balance) - (init_hit_balance+init_polo_balance+init_bitstmp_balance)) / (init_hit_balance+init_polo_balance+init_bitstmp_balance) )
    logger.info ("Total: " + '${:,.2f}'.format(hit_balance + polo_balance + bitstmp_balance)+ " -- Change: " + str("{0:.2f}".format(perc_diff * 100) + "%"))

    time.sleep(5)
