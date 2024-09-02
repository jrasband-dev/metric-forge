import polars as pl


@pl.api.register_expr_namespace("forge_product_dev")
class ProductDevelopment_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def opportunity_score(self, importance_col: str, satisfaction_col: str) -> pl.Expr:
        '''
        Opportunity Score
        
        Source: What Customers Want, Anthony Ulwick
        '''
        importance_expr = pl.col(importance_col)
        satisfaction_expr = pl.col(satisfaction_col)
        return pl.when(importance_expr == 0).then(0.0).otherwise(
            importance_expr + (importance_expr - satisfaction_expr)
        ).alias('opportunity_score')

    def customer_value_delivered(self, importance_col: str, satisfaction_col: str) -> pl.Expr:
        '''
        Customer Value Delivered
        
        Source: The Lean Product Playbook, Dan Olsen
        '''
        importance_expr = pl.col(importance_col) / 10
        satisfaction_expr = pl.col(satisfaction_col) / 10
        return pl.when(importance_expr == 0).then(0.0).otherwise(
            importance_expr * satisfaction_expr
        ).alias('customer_value_delivered')

    def opportunity_to_add_value(self, importance_col: str, satisfaction_col: str) -> pl.Expr:
        '''
        Opportunity to Add Value

        Source: The Lean Product Playbook, Dan Olsen
        '''
        importance_expr = pl.col(importance_col) / 10
        satisfaction_expr = pl.col(satisfaction_col) / 10
        return pl.when(importance_expr == 0).then(0.0).otherwise(
            importance_expr * (1 - satisfaction_expr)
        ).alias('opp_to_add_value')

    def customer_value_created(self, importance_col: str, satisfaction_before_col: str, satisfaction_after_col: str) -> pl.Expr:
        '''
        Customer Value Created

        Source: The Lean Product Playbook, Dan Olsen
        '''
        importance_expr = pl.col(importance_col) / 10
        satisfaction_before_expr = pl.col(satisfaction_before_col) / 10
        satisfaction_after_expr = pl.col(satisfaction_after_col) / 10
        return pl.when(importance_expr == 0).then(0.0).otherwise(
            importance_expr * (satisfaction_after_expr - satisfaction_before_expr)
        ).alias('customer_value_created')

    # def return_on_investment():
