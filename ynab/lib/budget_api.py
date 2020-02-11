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

    def __create_category(self):
        categories = []
        for category in self.__budget['budget']['categories']:
            categories.append(
                category_api.Category(
                    category['id'],
                    category['category_group_id'],
                    category['name'],
                    category['hidden'],
                    category['original_category_group_id'],
                    category['note'],
                    category['budgeted'],
                    category['activity'],
                    category['balance'],
                    category['goal_type'],
                    category['goal_creation_month'],
                    category['goal_target'],
                    category['goal_target_month'],
                    category['goal_percentage_complete'],
                    category['deleted']
                ).get_category()
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

    def get_categories(self):
        return self.__categories
