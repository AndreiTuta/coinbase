class Wallet:
    def __init__(self,cb_wallet):
        self.allow_deposits= cb_wallet["allow_deposits"],
        self.allow_withdrawals= cb_wallet["allow_withdrawals"],
        self.balance= cb_wallet["balance"],
        self.created_at= cb_wallet["created_at"],
        self.currency= cb_wallet["currency"],
        self.id= cb_wallet["id"],
        self.name= cb_wallet["name"],
        self.native_balance= cb_wallet["native_balance"],
        self.primary= cb_wallet["primary"],
        self.resource= cb_wallet["resource"],
        self.resource_path= cb_wallet["resource_path"],
        self.type= cb_wallet["type"],
        self.updated_at= cb_wallet["updated_at"]

    def print_wallet(self, current):
        sequence = [str(current), str(self.name)]
        line = ', '.join(sequence)
        print(line)
