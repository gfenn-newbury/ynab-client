import requests
from ynab.lib import budget_api


class Client:

    __categories = []
    __url = 'https://api.youneedabudget.com/v1/budgets'
    __key = None
    __budget_overview = None
    __budgets_json = None
    __budgets = None

    def __init__(self, key=''):
        self.__key = key
        self.__get_budgets()
        self.__create_budgets()
        self.print_budget()

    def __get_budgets(self):
        all_budgets = []
        h = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.__key}',
        }
        budgets = requests.get(self.__url, headers=h).json()['data']['budgets']
        self.__budget_overview = budgets
        for budget in budgets:
            url = f'{self.__url}/{budget["id"]}'
            r = requests.get(url, headers=h).json()['data']
            all_budgets.append(r)
        self.__budgets_json = all_budgets

    def __create_budgets(self):
        budgets = []
        for budget in self.__budgets_json:
            print(f'Budget ID: {budget["budget"]["id"]}')
            budgets.append(budget_api.Budget(budget))
        self.__budgets = budgets

    def __create_categories(self):
        raise NotImplementedError()

    def __create_transactions(self):
        raise NotImplementedError()

    def __create_payees(self):
        raise NotImplementedError()

    def __create_accounts(self):
        raise NotImplementedError()

    def print_budget(self):
        for budget in self.__budgets:
            budget.get_budget()
