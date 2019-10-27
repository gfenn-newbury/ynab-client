from ynab.lib import account_api


class Budget:

    __accounts = None
    __categories = None
    __payees = None
    __transactions = None
    __budget = None

    def __init__(self, budget):
        self.__budget = budget
        self.__create_accounts()

    def __create_accounts(self):
        accounts = []
        for account in self.__budget['budget']['accounts']:
            accounts.append(
                account_api.Account(
                    account['id'],
                    account['name'],
                    account['type'],
                    account['on_budget'],
                    account['closed'],
                    account['note'],
                    account['balance'],
                    account['cleared_balance'],
                    account['uncleared_balance'],
                    account['transfer_payee_id'],
                    account['deleted']
                )
            )
        self.__accounts = accounts

    def get_budget(self):
        print('-------------------------------------------')
        print(f'| Budget {self.__budget["budget"]["name"]} |')
        print('-------------------------------------------')
        print('Name\t\t\t\tType\tUncBal\tBal')
        for account in self.__accounts:
            account.get_account()
