class Account:

    __id = None
    __name = None
    __type = None
    __on_budget = None
    __closed = None
    __note = None
    __balance = None
    __cleared_balance = None
    __uncleared_balance = None
    __transfer_payee_id = None
    __deleted = None

    def __init__(
        self,
        id,
        name,
        type,
        on_budget,
        closed,
        note,
        balance,
        cleared_balance,
        uncleared_balance,
        transfer_payee_id,
        deleted
    ):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__on_budget = on_budget
        self.__closed = closed
        self.__note = note
        self.__balance = balance
        self.__cleared_balance = cleared_balance
        self.__uncleared_balance = uncleared_balance
        self.__transfer_payee_id = transfer_payee_id
        self.__deleted = deleted

    def get_balance(self):
        return {
            'Uncleared Balance': self.__uncleared_balance,
            'Cleared Balance': self.__cleared_balance
        }

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_closed(self):
        return self.__closed

    def print_account(self):
        print(
            f'{self.__name}\t\t\t{self.__type}\t{self.__uncleared_balance}\t{self.__cleared_balance}'
        )
