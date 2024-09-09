import yfinance as yf
import polars as pl
import pandas as pd

from .objects import FinancialStatements, FinancialDataImporter

class YahooFinanceImporter(FinancialDataImporter):
    def load_data(self, ticker):
        stock = yf.Ticker(ticker)

        income_statement = stock.financials
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow

        income_statement_columns = [str(col) for col in income_statement.columns]
        balance_sheet_columns = [str(col) for col in balance_sheet.columns]
        cash_flow_columns = [str(col) for col in cash_flow.columns]

        income_statement.reset_index(inplace=True)
        balance_sheet.reset_index(inplace=True)
        cash_flow.reset_index(inplace=True)

        income_statement = pl.from_pandas(
            income_statement
        ).unpivot(index='index', on=income_statement_columns, variable_name='date').pivot(on='index', values='value', index='date')

        balance_sheet = pl.from_pandas(
            balance_sheet
        ).unpivot(index='index', on=balance_sheet_columns, variable_name='date').pivot(on='index', values='value', index='date')

        cash_flow = pl.from_pandas(
            cash_flow
        ).unpivot(index='index', on=cash_flow_columns, variable_name='date').pivot(on='index', values='value', index='date')

        return income_statement, balance_sheet, cash_flow
    

def import_financials(ticker, engine='yfinance'):
    if engine == 'yfinance':
        importer = YahooFinanceImporter()
    else:
        raise ValueError(f"Unsupported engine: {engine}")

    return FinancialStatements(ticker, importer)




