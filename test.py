from ynab.objects import transaction, account, budget, category, payee
from pprint import pprint

def main():
    c = category('TestCat', '', 'child', '', '')
    p = payee('Guy Newbury')
    transactions = []
    transactions.append(transaction('01/01/2019', p, c, '1.00', '0.00', 'TestMemo').to_dict())
    transactions.append(transaction('02/01/2019', p, c, '1.00', '0.00', 'TestMemo2').to_dict())

    a = account('Test Account', transactions, '01/01/2019', '')
    pprint(a.to_dict())

if __name__ == '__main__':
    main()
