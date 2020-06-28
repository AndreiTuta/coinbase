class Wallet:
    # TODO: make all columns constats
    def __init__(self,cb_wallet):
        self.__dict__.update(cb_wallet)
        self.__dict__.pop('balance', None)
        self.__dict__.pop('native_balance', None)
        for k, v in cb_wallet.items():
            if isinstance(v, dict):
                val ={}
                for k,v in v.items():
                    val[k] = v
                if(val['currency'] =='ETH'):
                    self.__dict__['balance'] = val['amount']
                else:
                    self.__dict__['native_balance'] = val['amount']
                    self.__dict__['native_balance_currency'] = val['currency']


    def print_to_csv(self):
        sequence = [self.__dict__['id'],self.__dict__['name'], self.__dict__['balance'], self.__dict__['currency'], self.__dict__['native_balance'], self.__dict__['native_balance_currency']]
        line = ', '.join(sequence)
        return line

    def print(self):
        return vars(self)
