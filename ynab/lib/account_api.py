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

    def __init__(self, account_json):
        self.__account_json = account_json
        self.__create_account()

    def __create_account(self):
        self.__id = self.__account_json['id']
        self.__name = self.__account_json['name']
        self.__type = self.__account_json['type']
        self.__on_budget = self.__account_json['on_budget']
        self.__closed = self.__account_json['closed']
        self.__note = self.__account_json['note']
        self.__balance = self.__account_json['balance']
        self.__cleared_balance = self.__account_json['cleared_balance']
        self.__uncleared_balance = self.__account_json['uncleared_balance']
        self.__transfer_payee_id = self.__account_json['transfer_payee_id']
        self.__deleted = self.__account_json['deleted']

    def get_balance(self):
        return {
            'Uncleared Balance': self.__uncleared_balance,
            'Cleared Balance': self.__cleared_balance
        }

    def get_id(self):
        return self.__id

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

    def get_account_json(self):
        account_json = {
            'id': self.__id,
            'name': self.__name,
            'type': self.__type,
            'on_budget': self.__on_budget,
            'closed': self.__closed,
            'note': self.__note,
            'balance': self.__balance,
            'cleared_balance': self.__cleared_balance,
            'uncleared_balance': self.__uncleared_balance,
            'transfer_payee_id': self.__transfer_payee_id,
            'deleted': self.__deleted
        }
        return account_json
