import polars as pl

@pl.api.register_expr_namespace("forge_ecommerce")
class Ecommerce_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def customer_acquisition_cost(self, cost_column: str, customers_column: str) -> pl.Expr:
        """
        Calculate Customer Acquisition Cost (CAC) for DataFrames.
        """
        cost_expr = pl.col(cost_column)
        customers_expr = pl.col(customers_column)
        return pl.when(customers_expr == 0).then(0.0).otherwise(cost_expr / customers_expr).alias('customer_acquisition_cost')

    def average_order_value(self, total_revenue_column: str, number_of_orders_column: str) -> pl.Expr:
        """
        Calculate the Average Order Value (AOV).
        """
        total_revenue_expr = pl.col(total_revenue_column)
        number_of_orders_expr = pl.col(number_of_orders_column)
        return pl.when(number_of_orders_expr == 0).then(0.0).otherwise(total_revenue_expr / number_of_orders_expr).alias('average_order_value')

    def cart_abandonment_rate(self, carts_created_column: str, completed_purchases_column: str) -> pl.Expr:
        """
        Calculate the Cart Abandonment Rate.
        """
        carts_created_expr = pl.col(carts_created_column)
        completed_purchases_expr = pl.col(completed_purchases_column)
        return pl.when(carts_created_expr == 0).then(0.0).otherwise(((carts_created_expr - completed_purchases_expr) / carts_created_expr) * 100).alias('cart_abandonment_rate')

    def return_on_advertising_spend(self, revenue_from_ads_column: str, advertising_spend_column: str) -> pl.Expr:
        """
        Calculate the Return on Advertising Spend (ROAS).
        """
        revenue_from_ads_expr = pl.col(revenue_from_ads_column)
        advertising_spend_expr = pl.col(advertising_spend_column)
        return pl.when(advertising_spend_expr == 0).then(0.0).otherwise(revenue_from_ads_expr / advertising_spend_expr).alias('return_on_advertising_spend')

    def conversion_rate(self, num_conversions_column: str, num_visitors_column: str) -> pl.Expr:
        """
        Calculate Conversion Rate.
        """
        num_conversions_expr = pl.col(num_conversions_column)
        num_visitors_expr = pl.col(num_visitors_column)
        return pl.when(num_visitors_expr == 0).then(0.0).otherwise((num_conversions_expr / num_visitors_expr) * 100).alias('conversion_rate')

    def customer_lifetime_value(self, revenue_per_customer_column: str, average_customer_lifetime_column: str) -> pl.Expr:
        """
        Calculate Customer Lifetime Value (CLV).
        """
        revenue_per_customer_expr = pl.col(revenue_per_customer_column)
        average_customer_lifetime_expr = pl.col(average_customer_lifetime_column)
        return (revenue_per_customer_expr * average_customer_lifetime_expr).alias('customer_lifetime_value')

    def customer_churn_rate(self, num_customers_lost_column: str, total_customers_beginning_column: str) -> pl.Expr:
        """
        Calculate Customer Churn Rate.
        """
        num_customers_lost_expr = pl.col(num_customers_lost_column)
        total_customers_beginning_expr = pl.col(total_customers_beginning_column)
        return pl.when(total_customers_beginning_expr == 0).then(0.0).otherwise((num_customers_lost_expr / total_customers_beginning_expr) * 100).alias('customer_churn_rate')
