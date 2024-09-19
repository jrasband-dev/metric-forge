import polars as pl

@pl.api.register_expr_namespace("forge_human_capital")
class HumanCapital_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    # Employee Turnover Rate
    def employee_turnover_rate(self, employees_left_column: str, total_employees_column: str) -> pl.Expr:
        employees_left_expr = pl.col(employees_left_column)
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(employees_left_expr / total_employees_expr).alias('employee_turnover_rate')

    # Sales per Employee
    def sales_per_employee(self, sales_column: str, total_employees_column: str) -> pl.Expr:
        sales_expr = pl.col(sales_column)
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(sales_expr / total_employees_expr).alias('sales_per_employee')

    # Absenteeism Rate
    def absenteeism_rate(self, absent_days_column: str, total_workdays_column: str) -> pl.Expr:
        absent_days_expr = pl.col(absent_days_column)
        total_workdays_expr = pl.col(total_workdays_column)
        return pl.when(total_workdays_expr == 0).then(0.0).otherwise(absent_days_expr / total_workdays_expr).alias('absenteeism_rate')

    # Average Tenure of Employees
    def average_tenure(self, total_tenure_column: str, total_employees_column: str) -> pl.Expr:
        total_tenure_expr = pl.col(total_tenure_column)  # Assumes total tenure in years or months
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(total_tenure_expr / total_employees_expr).alias('average_tenure')
