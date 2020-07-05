class Wallet:
    # default constructor
    def __init__(self, cb_wallet):
        self.__dict__.update(cb_wallet)
    # currency based wallet

    def get_currency(self, currency):
        if(self.__dict__['balance']['currency'].lower() == currency.lower()):
            return self
        return None

    def to_str(self):
        return vars(self)

    # external use
    def add_prices(self, buy, sell):
        self.__dict__['buy_price'] = buy
        self.__dict__['sell_price'] = sell
    
    # external use
    def add_rates(self, exachange_rates):
        self.__dict__['exachange_rates'] = exachange_rates