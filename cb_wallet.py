class Wallet:
    
    
    
    # default constructor
    def __init__(self, cb_account, fetched):
        self.__dict__.update(cb_account)
        self.__dict__['fetched'] = fetched

    def has_currency(self, currency):
        if(self.__dict__['balance']['currency'].lower() == currency.lower()):
            return True
        return False

    def get_dates_UTC(self):
        switcher = { 
            'fetched': "zero", 
            'updated_at': "one", 
            }     
        # get() method of dictionary data type returns  
        # value of passed argument if it is present  
        # in dictionary otherwise second argument will 
        # be assigned as default value of passed argument 
        self.__dict__['fetched'] = switcher.get('fetched', "") 
        self.__dict__['updated_at'] = switcher.get('updated_at', "") 


    def to_dict(self):
        clone = {}
        clone.update(self.__dict__)
        # TODO: Move to constants using Coinbase model
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

    
    """
        params order: [included rates]
    """

    def add_rates(self, exachange_rates, *args, **kwargs):
        
        filtered_exchange_rates = {key: value[:8] for (
            key, value) in exachange_rates.items() if (key) in args[0]}
        print(filtered_exchange_rates)
        self.__dict__['exachange_rates'] = filtered_exchange_rates
