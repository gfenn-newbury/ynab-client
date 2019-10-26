class account:

    def __init__(
            self,
            name='',
            transactions=[],
            opened='',
            closed='',
            key=''
    ):
        self.name = name
        self.transactions = transactions
        self.opened = opened
        self.closed = closed

    def addTransaction(self, transaction):
        self.transactions.append(transaction)

    def to_dict(self):
        return {
                'Name': self.name,
                'Transactions': self.transactions,
                'Opened': self.opened,
                'Closed': self.closed
                }
