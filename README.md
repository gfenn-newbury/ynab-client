# YNAB Python project [![CircleCI](https://circleci.com/gh/GNewbury1/ynab-client/tree/master.svg?style=svg)](https://circleci.com/gh/GNewbury1/ynab-client/tree/master)


This is a new project for YNAB Python client.

View a changelog [here](CHANGELOG.md).

## Build Status

| Branch/Tag | Description | Status |
|------------|-------------|--------|
| master | Repository master | [![CircleCI](https://circleci.com/gh/GNewbury1/ynab-client/tree/master.svg?style=svg)](https://circleci.com/gh/GNewbury1/ynab-client/tree/master) |
| v0.4.0 | Current release | [![CircleCI](https://circleci.com/gh/GNewbury1/ynab-client/tree/release%2Fv0.4.0.svg?style=svg)](https://circleci.com/gh/GNewbury1/ynab-client/tree/release%2Fv0.4.0) |
| v0.5.0 | In-development release | [![CircleCI](https://circleci.com/gh/GNewbury1/ynab-client/tree/release%2Fv0.4.0.svg?style=svg)](https://circleci.com/gh/GNewbury1/ynab-client/tree/release%2Fv0.4.0) |
---

# Purpose and Usage

The purpose of this project is primarily just to mess around with REST APIs. If you're looking for a proper solution, have a look at [ynab-client-python](https://github.com/gchiam/ynab-client-python) by [gchiam] (https://github.com/gchiam). With that said, however, the aim is to get a fully functional desktop client which can view all aspects of YNAB. There are several components:

## APIs

### Budget API

This part of the API is concerned with budgets. It will get a list of budgets, or when one is specified, will get all details of a budget.

### Account API

This part of the API is concerned with accounts within a budget. It will get all accounts within a budget, and be able to list a specific account.

### Category API

This part of the API is concerned with categories within a budget. It can list all categories, and get details of each specific one.

### Payee API

This part of the API deals with payees per budget.

### Transaction API

This part of the API deals with transactions per account within a budget. It can list all transactions, segregate them per category, or per account.
