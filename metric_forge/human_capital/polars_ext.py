import polars as pl

@pl.api.register_expr_namespace("forge_human_capital")
class HumanCapital_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    # Employee Turnover Rate
    def employee_turnover_rate(self, employees_left_column: str, total_employees_column: str) -> pl.Expr:
        '''
        Calculates the employee turnover rate by dividing the number of employees who have left by the total number of employees.

        Parameters
        ----------
        employees_left_column : str
            The column name representing the number of employees who have left during a given period.
        total_employees_column : str
            The column name representing the total number of employees during the same period.

        Returns
        -------
        pl.Expr
            An expression representing the employee turnover rate, set to 0 if the total number of employees is zero.
        '''
        employees_left_expr = pl.col(employees_left_column)
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(employees_left_expr / total_employees_expr).alias('employee_turnover_rate')

    # Sales per Employee
    def sales_per_employee(self, sales_column: str, total_employees_column: str) -> pl.Expr:
        '''
        Calculates the sales per employee by dividing total sales by the number of employees.

        Parameters
        ----------
        sales_column : str
            The column name representing the total sales over a given time period.
        total_employees_column : str
            The column name representing the total number of employees during the same period.

        Returns
        -------
        pl.Expr
            An expression representing sales per employee, set to 0 if the total number of employees is zero.
        '''
        sales_expr = pl.col(sales_column)
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(sales_expr / total_employees_expr).alias('sales_per_employee')

    # Absenteeism Rate
    def absenteeism_rate(self, absent_days_column: str, total_workdays_column: str) -> pl.Expr:
        '''
        Calculates the absenteeism rate by dividing the number of absent days by the total number of workdays.

        Parameters
        ----------
        absent_days_column : str
            The column name representing the number of days employees were absent.
        total_workdays_column : str
            The column name representing the total number of workdays in a given period.

        Returns
        -------
        pl.Expr
            An expression representing the absenteeism rate, set to 0 if the total number of workdays is zero.
        '''
        absent_days_expr = pl.col(absent_days_column)
        total_workdays_expr = pl.col(total_workdays_column)
        return pl.when(total_workdays_expr == 0).then(0.0).otherwise(absent_days_expr / total_workdays_expr).alias('absenteeism_rate')

    # Average Tenure of Employees
    def average_tenure(self, total_tenure_column: str, total_employees_column: str) -> pl.Expr:
        '''
        Calculates the average tenure of employees by dividing the total tenure by the total number of employees.

        Parameters
        ----------
        total_tenure_column : str
            The column name representing the total tenure of employees, typically in years or months.
        total_employees_column : str
            The column name representing the total number of employees.

        Returns
        -------
        pl.Expr
            An expression representing the average tenure of employees, set to 0 if the total number of employees is zero.
        '''
        total_tenure_expr = pl.col(total_tenure_column)
        total_employees_expr = pl.col(total_employees_column)
        return pl.when(total_employees_expr == 0).then(0.0).otherwise(total_tenure_expr / total_employees_expr).alias('average_tenure')
