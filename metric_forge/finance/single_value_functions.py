class Finance_SVF:
    def gross_profit_margin(self, revenue: float, cogs: float) -> float:
        if revenue == 0:
            return 0.0
        return (revenue - cogs) / revenue

    def net_profit_margin(self, revenue: float, cogs: float, expenses: float) -> float:
        if revenue == 0:
            return 0.0
        net_income = revenue - cogs - expenses
        return net_income / revenue

    def ebitda_margin(self, revenue: float, cogs: float, expenses: float, depreciation: float, amortization: float) -> float:
        if revenue == 0:
            return 0.0
        ebitda = revenue - cogs - expenses + depreciation + amortization
        return ebitda / revenue

    def earnings_per_share(self, revenue: float, cogs: float, expenses: float, shares_outstanding: float) -> float:
        if shares_outstanding == 0:
            return 0.0
        net_income = revenue - cogs - expenses
        return net_income / shares_outstanding

    def current_ratio(self, current_assets: float, current_liabilities: float) -> float:
        if current_liabilities == 0:
            return 0.0
        return current_assets / current_liabilities

    def quick_ratio(self, current_assets: float, inventory: float, current_liabilities: float) -> float:
        if current_liabilities == 0:
            return 0.0
        quick_assets = current_assets - inventory
        return quick_assets / current_liabilities
    
    def free_cash_flow(self, operating_cash_flow: float, capital_expenditures: float) -> float:
        return operating_cash_flow - capital_expenditures

    def operating_cash_flow_ratio(self, operating_cash_flow: float, current_liabilities: float) -> float:
        if current_liabilities == 0:
            return 0.0
        return operating_cash_flow / current_liabilities