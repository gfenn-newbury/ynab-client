

class transaction:

    import datetime
    from .objects import category

    def __init__(
        self,
        date=datetime.datetime.now(),
        payee='',
        category=category(),
        amountIn=0.00,
        amountOut=0.00,
        memo=''
    ):
        self.date = date
        self.payee = payee
        self.category = category
        self.amountIn = amountIn
        self.amountOut = amountOut
        self.memo = memo

    def to_dict(self):
        return {
                'Date': self.date,
                'Payee': self.payee.getName(),
                'Category': self.category.getName(),
                'In': self.amountIn,
                'Out': self.amountOut,
                'Memo': self.memo,
                }


class category:

    def __init__(
        self,
        name='',
        parent='',
        catType='',
        children=[],
        budgeted=0
    ):
        self.name = name
        self.type = catType
        if parent and children:
            print('Must only have parent or child')
        elif parent:
            self.parent = parent
            self.budgeted = budgeted
        elif children:
            self.children = children

    def addChild(self, child):
        self.children.append(child)

    def getName(self):
        return self.name


class budget:

    def __init__(self, categories):
        self.categories = categories


class account:

    def __init__(
            self,
            name='',
            transactions=[],
            opened='',
            closed=''
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


class payee:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
