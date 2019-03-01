class transaction:

    def __init__(self, date, payee, category, amountIn, amountOut, memo):
        self.date = date
        self.payee = payee
        self.category = category
        self.amountIn = amountIn
        self.amountOut = amountOut
        self.memo = memo

    def to_dict(self):
        return {
                'Date': self.date,
                'Payee': self.payee,
                'Category': self.category,
                'In': self.amountIn,
                'Out': self.amountOut,
                'Memo': self.memo,
                }
