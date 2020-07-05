class Wallet:
    # TODO: make all columns constats
    def __init__(self, cb_wallet):
        self.__dict__.update(cb_wallet)

    def toStr(self):
        return vars(self)
