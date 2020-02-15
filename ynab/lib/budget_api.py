from ynab.lib import account_api, category_api


class Budget:

    __accounts = None
    __categories = None
    __payees = None
    __transactions = None
    __budget = None

    def __init__(self, budget):
        self.__budget = budget
        self.__create_accounts()
        self.__create_category()

    def __create_accounts(self):
        accounts = []
        for account in self.__budget['budget']['accounts']:
            accounts.append(account_api.Account(account))
        self.__accounts = accounts

    def __create_category(self):
        categories = []
        for category in self.__budget['budget']['categories']:
            categories.append(
                category_api.Category(category)
            )
        self.__categories = categories

    def print_budget(self):
        print('-------------------------------------------')
        print(f'| Budget {self.__budget["budget"]["name"]} |')
        print('-------------------------------------------')
        print('Name\t\t\t\tType\tUncBal\tBal')
        for account in self.__accounts:
            account.print_account()

    def get_budget_id(self):
        return self.__budget['budget']['id']

    def get_budget_json(self):
        return self.__budget['budget']

    def get_category_list(self):
        return self.__categories

    def get_account_list(self):
        return self.__accounts

    def get_account(self, id):
        for account in self.__accounts:
            if account.get_id() == id:
                return account.get_account_json()
