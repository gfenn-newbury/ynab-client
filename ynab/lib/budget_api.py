import requests


class budget:

    __categories = []
    __url = 'https://api.youneedabudget.com/v1/budgets'
    __key = None
    __budget_overview = None
    __budgets = None

    def __init__(self, key=''):
        self.__key = key
        self.__get_all_budgets()

    def __get_all_budgets(self):
        all_budgets = []
        h = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.key}',
        }
        budgets = requests.get(self.url, headers=h).json()['data']['budgets']
        self.__budget_overview = budgets
        for budget in budgets:
            url = f'{self.url}/{budget["id"]}'
            r = requests.get(url, headers=h).json()['data']
            all_budgets.append(r)
        self.__budgets = all_budgets

    def __create_categories(self):
        raise NotImplementedError()

    def __create_transactions(self):
        raise NotImplementedError()

    def __create_payees(self):
        raise NotImplementedError()

    def __create_accounts(self):
        raise NotImplementedError

    def get_budgets(self):
        return self.__budget_overview
