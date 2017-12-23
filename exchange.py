import logging

logger = logging.getLogger(__name__)

class Exchange:

    def get_exchange_name(self):
        logging.info ("get_exchange_name not implemented")

    def short_crypto (self, _symbol, _quantity, _price):
        logging.info ("short_crypto not implemented")

    def long_crypto (self, _symbol, _quantity, _price):
        logging.info("long_crypto not implemented")

    def get_balance_usd (self):
        logging.info ("get_balance_usd not implemented")

    def get_make_fee (self):
        logging.info ("get_make_fee not implemented")

    def get_take_fee (self):
        logging.info ("get_take_fee not implemented")