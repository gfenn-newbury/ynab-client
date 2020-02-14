# Changelog

### 0.5.0 (2020/02/14)
**Changes**
- Restructured classes such that:
  - `ynab.api.Client` is now `ynab.core.Client`
  - `ynab.tests.test_api` is now `tests.test_core`

### 0.4.0 (2019/10/27)
**Changes**
- Implemented `ynab.api.Client`, `ynab.lib.budget_api.Budget`, and `ynab.lib.account_api.Account` to allow for correct storage of budgets and accounts
- Implemented `ynab.tests.test_api.ClientTests` to test functionality of budgets and accounts via the `ynab.api.Client` module

### 0.3.0 (2019/10/26)
**Changes**
- Added unit testing
- Created new layout to allow for tests
- Made some parameters key rather than positional

### 0.2.0
**Changes:**
- `ynab/objects/*.py no longer exists, having beeing replaced by `ynab/objects.py`, which then contains relevent classes (eg, `from ynab.objects import transaction`)
- `ynab.api.ynab` has been expanded and changed to `ynab.api.client`

### 0.1.0

- Initial release
