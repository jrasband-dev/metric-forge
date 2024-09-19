import polars as pl

@pl.api.register_expr_namespace("forge_income_statement")
class IncomeStatement_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def gross_profit_margin(self, revenue_column: str, cogs_column: str) -> pl.Expr:
        """
        Calculate gross profit margin.

        Parameters:
        - revenue_column (str): The column containing total revenue.
        - cogs_column (str): The column containing cost of goods sold (COGS).

        Returns:
        - pl.Expr: The calculated gross profit margin.
        """
        revenue_expr = pl.col(revenue_column)
        cogs_expr = pl.col(cogs_column)
        return pl.when(revenue_expr == 0).then(0.0).otherwise((revenue_expr - cogs_expr) / revenue_expr).alias('gross_profit_margin')

    def net_profit_margin(self, revenue_column: str, cogs_column: str, expenses_column: str) -> pl.Expr:
        """
        Calculate net profit margin.

        Parameters:
        - revenue_column (str): The column containing total revenue.
        - cogs_column (str): The column containing cost of goods sold (COGS).
        - expenses_column (str): The column containing operating expenses.

        Returns:
        - pl.Expr: The calculated net profit margin.
        """
        revenue_expr = pl.col(revenue_column)
        cogs_expr = pl.col(cogs_column)
        expenses_expr = pl.col(expenses_column)
        net_income_expr = revenue_expr - cogs_expr - expenses_expr
        return pl.when(revenue_expr == 0).then(0.0).otherwise(net_income_expr / revenue_expr).alias('net_profit_margin')

    def ebitda_margin(self, revenue_column: str, cogs_column: str, expenses_column: str, depreciation_column: str, amortization_column: str) -> pl.Expr:
        """
        Calculate EBITDA margin.

        Parameters:
        - revenue_column (str): The column containing total revenue.
        - cogs_column (str): The column containing cost of goods sold (COGS).
        - expenses_column (str): The column containing operating expenses.
        - depreciation_column (str): The column containing depreciation expense.
        - amortization_column (str): The column containing amortization expense.

        Returns:
        - pl.Expr: The calculated EBITDA margin.
        """
        revenue_expr = pl.col(revenue_column)
        cogs_expr = pl.col(cogs_column)
        expenses_expr = pl.col(expenses_column)
        depreciation_expr = pl.col(depreciation_column)
        amortization_expr = pl.col(amortization_column)
        ebitda_expr = revenue_expr - cogs_expr - expenses_expr + depreciation_expr + amortization_expr
        return pl.when(revenue_expr == 0).then(0.0).otherwise(ebitda_expr / revenue_expr).alias('ebitda_margin')

    def earnings_per_share(self, revenue_column: str, cogs_column: str, expenses_column: str, shares_outstanding_column: str) -> pl.Expr:
        """
        Calculate earnings per share (EPS).

        Parameters:
        - revenue_column (str): The column containing total revenue.
        - cogs_column (str): The column containing cost of goods sold (COGS).
        - expenses_column (str): The column containing operating expenses.
        - shares_outstanding_column (str): The column containing the number of outstanding shares.

        Returns:
        - pl.Expr: The calculated earnings per share.
        """
        revenue_expr = pl.col(revenue_column)
        cogs_expr = pl.col(cogs_column)
        expenses_expr = pl.col(expenses_column)
        shares_outstanding_expr = pl.col(shares_outstanding_column)
        net_income_expr = revenue_expr - cogs_expr - expenses_expr
        return pl.when(shares_outstanding_expr == 0).then(0.0).otherwise(net_income_expr / shares_outstanding_expr).alias('earnings_per_share')


@pl.api.register_expr_namespace("forge_balance_sheet")
class BalanceSheet_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def current_ratio(self, current_assets_column: str, current_liabilities_column: str) -> pl.Expr:
        """
        Calculate current ratio.

        Parameters:
        - current_assets_column (str): The column containing current assets.
        - current_liabilities_column (str): The column containing current liabilities.

        Returns:
        - pl.Expr: The calculated current ratio.
        """
        current_assets_expr = pl.col(current_assets_column)
        current_liabilities_expr = pl.col(current_liabilities_column)
        return pl.when(current_liabilities_expr == 0).then(0.0).otherwise(current_assets_expr / current_liabilities_expr).alias('current_ratio')

    def quick_ratio(self, current_assets_column: str, inventory_column: str, current_liabilities_column: str) -> pl.Expr:
        """
        Calculate quick ratio.

        Parameters:
        - current_assets_column (str): The column containing current assets.
        - inventory_column (str): The column containing inventory.
        - current_liabilities_column (str): The column containing current liabilities.

        Returns:
        - pl.Expr: The calculated quick ratio.
        """
        current_assets_expr = pl.col(current_assets_column)
        inventory_expr = pl.col(inventory_column)
        current_liabilities_expr = pl.col(current_liabilities_column)
        quick_assets_expr = current_assets_expr - inventory_expr
        return pl.when(current_liabilities_expr == 0).then(0.0).otherwise(quick_assets_expr / current_liabilities_expr).alias('quick_ratio')
    

@pl.api.register_expr_namespace("forge_cash_flow")
class CashFlow_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def free_cash_flow(self, operating_cash_flow_column: str, capital_expenditures_column: str) -> pl.Expr:
        """
        Calculate free cash flow.

        Parameters:
        - operating_cash_flow_column (str): The column containing operating cash flow.
        - capital_expenditures_column (str): The column containing capital expenditures.

        Returns:
        - pl.Expr: The calculated free cash flow.
        """
        operating_cash_flow_expr = pl.col(operating_cash_flow_column)
        capital_expenditures_expr = pl.col(capital_expenditures_column)
        return (operating_cash_flow_expr - capital_expenditures_expr).alias('free_cash_flow')

    def operating_cash_flow_ratio(self, operating_cash_flow_column: str, current_liabilities_column: str) -> pl.Expr:
        """
        Calculate operating cash flow ratio.

        Parameters:
        - operating_cash_flow_column (str): The column containing operating cash flow.
        - current_liabilities_column (str): The column containing current liabilities.

        Returns:
        - pl.Expr: The calculated operating cash flow ratio.
        """
        operating_cash_flow_expr = pl.col(operating_cash_flow_column)
        current_liabilities_expr = pl.col(current_liabilities_column)
        return pl.when(current_liabilities_expr == 0).then(0.0).otherwise(operating_cash_flow_expr / current_liabilities_expr).alias('operating_cash_flow_ratio')


@pl.api.register_expr_namespace("forge_finance")
class Finance_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def commission_bps(self, revenue_column: str, bps_column: str) -> pl.Expr:
        """
        Calculate commission based on basis points (bps).

        Parameters:
        - revenue_column (str): The column containing revenue or transaction value.
        - bps_column (str): The column containing basis points (bps) for commission rate.

        Returns:
        - pl.Expr: The calculated commission based on bps.
        """
        revenue_expr = pl.col(revenue_column)
        bps_expr = pl.col(bps_column)
        commission_rate_expr = bps_expr / 10000  # Convert basis points to percentage
        return (revenue_expr * commission_rate_expr).alias('commission_bps')
