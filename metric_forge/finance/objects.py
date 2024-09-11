from dataclasses import dataclass, asdict, field
import polars as pl
from abc import ABC, abstractmethod
from IPython.display import display , HTML


class FinancialDataImporter(ABC):
    @abstractmethod
    def load_data(self, ticker):
        pass


class FinancialStatements:
    def __init__(self, ticker, importer: FinancialDataImporter):
        self.ticker = ticker
        self.importer = importer
        self.income_statement = None
        self.balance_sheet = None
        self.cash_flow = None
        self._load_data()

    def _load_data(self):
        self.income_statement, self.balance_sheet, self.cash_flow = self.importer.load_data(self.ticker)

    def get_income_statement(self):
        return self.income_statement

    def get_balance_sheet(self):
        return self.balance_sheet

    def get_cash_flow(self):
        return self.cash_flow
    
    def __repr__(self):

        display(HTML(f"<h2>Income Statement</h2>"))
        display(self.income_statement)
        display(HTML(f"<h2>Balance Sheet</h2>"))
        display(self.balance_sheet)
        display(HTML(f"<h2>Cash Flow</h2>"))
        display(self.cash_flow)
        return f"FinancialStatements(ticker={self.ticker})"

