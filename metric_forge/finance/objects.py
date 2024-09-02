from dataclasses import dataclass, asdict, field

@dataclass
class IncomeStatement:
    revenue: float = None
    cogs: float = None
    expenses: float = None
    interest_expense: float = None
    depreciation: float = 0
    amortization: float = 0
    shares_outstanding: float = None

    def gross_profit_margin(self):
        if self.revenue is None or self.cogs is None:
            return "Missing parameters: revenue, cogs"
        return (self.revenue - self.cogs) / self.revenue

    def net_profit_margin(self):
        if self.revenue is None or self.cogs is None or self.expenses is None:
            return "Missing parameters: revenue, cogs, expenses"
        net_income = self.revenue - self.cogs - self.expenses
        return net_income / self.revenue

    def ebitda_margin(self):
        if self.revenue is None or self.cogs is None or self.expenses is None:
            return "Missing parameters: revenue, cogs, expenses"
        ebitda = self.revenue - self.cogs - self.expenses + self.depreciation + self.amortization
        return ebitda / self.revenue

    def earnings_per_share(self):
        if self.revenue is None or self.cogs is None or self.expenses is None or self.shares_outstanding is None:
            return "Missing parameters: revenue, cogs, expenses, shares_outstanding"
        net_income = self.revenue - self.cogs - self.expenses
        return net_income / self.shares_outstanding
    
    def to_dict(self):
        return asdict(self)

    # Add more methods as needed



@dataclass
class BalanceSheet:
    assets: float = None
    total_liabilities: float = None
    equity: float = None
    current_assets: float = None
    current_liabilities: float = None
    inventory: float = None
    cash_and_cash_equivalents: float = None
    accounts_receivable: float = None

    def current_ratio(self):
        if self.current_assets is None or self.current_liabilities is None:
            return "Missing parameters: current_assets, current_liabilities"
        return self.current_assets / self.current_liabilities

    def quick_ratio(self):
        if self.current_assets is None or self.inventory is None or self.current_liabilities is None:
            return "Missing parameters: current_assets, inventory, current_liabilities"
        quick_assets = self.current_assets - self.inventory
        return quick_assets / self.current_liabilities

    def cash_ratio(self):
        if self.cash_and_cash_equivalents is None or self.current_liabilities is None:
            return "Missing parameters: cash_and_cash_equivalents, current_liabilities"
        return self.cash_and_cash_equivalents / self.current_liabilities

    def debt_to_equity_ratio(self):
        if self.total_liabilities is None or self.equity is None:
            return "Missing parameters: total_liabilities, equity"
        return self.total_liabilities / self.equity

    def debt_to_assets_ratio(self):
        if self.total_liabilities is None or self.assets is None:
            return "Missing parameters: total_liabilities, assets"
        return self.total_liabilities / self.assets

    def asset_turnover_ratio(self):
        if self.revenue is None or self.assets is None:
            return "Missing parameters: revenue, assets"
        return self.revenue / self.assets

    def check_balance(self):
        if self.assets is None or self.total_liabilities is None or self.equity is None:
            return "Missing parameters: assets, total_liabilities, equity"
        balance_check = (self.assets - self.total_liabilities)
        if balance_check == self.equity:
            return "The balance equation is correct: Assets - Liabilities = Equity"
        else:
            return f"Balance equation is incorrect: Assets - Liabilities ({self.assets} - {self.total_liabilities}) = {balance_check}, expected Equity = {self.equity}"
    # Add more methods as needed


@dataclass
class CashFlowStatement:
    operating_cash_flow: float = None
    capital_expenditures: float = None
    asset_sales: float = None
    new_debt: float = None
    debt_repayments: float = None
    new_equity: float = None
    dividends_paid: float = None
    dividend_per_share: float = None
    market_price_per_share: float = None
    days_sales_outstanding: float = None
    days_inventory_outstanding: float = None
    days_payable_outstanding: float = None

    def free_cash_flow(self):
        if self.capital_expenditures is None:
            return "Missing parameter: capital_expenditures"
        return self.operating_cash_flow - self.capital_expenditures

    def cash_flow_margin(self):
        if self.operating_cash_flow is None or self.revenue is None:
            return "Missing parameters: operating_cash_flow, revenue"
        return self.operating_cash_flow / self.revenue

    def cash_flow_per_share(self):
        if self.shares_outstanding is None:
            return "Missing parameter: shares_outstanding"
        return self.operating_cash_flow / self.shares_outstanding

    def cash_conversion_cycle(self):
        if (self.days_sales_outstanding is None or
            self.days_inventory_outstanding is None or
            self.days_payable_outstanding is None):
            return "Missing parameters: days_sales_outstanding, days_inventory_outstanding, days_payable_outstanding"
        return self.days_sales_outstanding + self.days_inventory_outstanding - self.days_payable_outstanding

    def cash_flow_from_investing(self):
        if self.capital_expenditures is None or self.asset_sales is None:
            return "Missing parameters: capital_expenditures, asset_sales"
        return self.asset_sales - self.capital_expenditures

    def cash_flow_from_financing(self):
        if (self.new_debt is None or self.debt_repayments is None or
            self.new_equity is None or self.dividends_paid is None):
            return "Missing parameters: new_debt, debt_repayments, new_equity, dividends_paid"
        return self.new_debt - self.debt_repayments + self.new_equity - self.dividends_paid

    # Add more methods as needed


@dataclass
class CombinedFinancialStatement:
    income_statement: IncomeStatement
    balance_sheet: BalanceSheet
    cash_flow_statement: CashFlowStatement

    def to_dict(self):
        return {
            'income_statement': asdict(self.income_statement),
            'balance_sheet': asdict(self.balance_sheet),
            'cash_flow_statement': asdict(self.cash_flow_statement),
        }
