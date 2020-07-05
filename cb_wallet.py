class Wallet:
    # default constructor
    def __init__(self, cb_account):
        self.__dict__.update(cb_account)
    # currency based wallet

    def has_currency(self, currency):
        if(self.__dict__['balance']['currency'].lower() == currency.lower()):
            return True
        return False

    def to_str(self):
        clone = {}
        clone.update(self.__dict__)
        clone.pop("resource_path")
        clone.pop("id")
        clone.pop("type")
        clone.pop("primary")
        clone.pop("resource")
        clone.pop("allow_withdrawals")
        clone.pop("allow_deposits")
        clone.pop("created_at")
        return clone

    # external use
    def add_prices(self, buy, sell):
        self.__dict__['buy_price'] = buy
        self.__dict__['sell_price'] = sell

    # external use

    """
        params order: [included coins]
    """

    def add_rates(self, exachange_rates, *args, **kwargs):
        filtered_exchange_rates = {key: value for (
            key, value) in exachange_rates.items() if (key) in args[0]}
        self.__dict__['exachange_rates'] = filtered_exchange_rates
