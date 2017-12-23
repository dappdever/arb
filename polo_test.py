from polo import Polo
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

polo = Polo()

while (True) :

    print ("Highest BCH bid: " + str(polo.get_highest_bid("BCH")))
    print ("Lowest BCH ask: " + str(polo.get_lowest_ask("BCH")))

    time.sleep (0.5)