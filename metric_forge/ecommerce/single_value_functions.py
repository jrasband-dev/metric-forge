class Ecommerce_SVF:
    @staticmethod
    def customer_acquisition_cost(cost: float
                                  ,customers: int) -> float:
        """
        Calculate Customer Acquisition Cost (CAC) for single values.

        Parameters
        ----------
        cost
            The total cost for acquiring customers.
        customers
            The number of customers acquired.

        Returns
        -------
        float
            The calculated CAC.
        """
        if customers == 0:
            return 0.0
        return cost / customers
    
    @staticmethod
    def average_order_value(total_revenue, number_of_orders):
        """
        Calculate the Average Order Value (AOV).

        Parameters
        ----------

        total_revenue
            The total revenue generated.
        number_of_orders
            The total number of orders.

        Returns
        -------

        float 

            The average order value (AOV).
        """
        if number_of_orders == 0:
            return 0.0
        return total_revenue / number_of_orders

    def cart_abandonment_rate(carts_created, completed_purchases):
        """
        Calculate the Cart Abandonment Rate.

        Parameters
        ----------

        carts_created
            The number of shopping carts created.
        completed_purchases
            The number of purchases completed.

        Returns
        -------
        float
            The cart abandonment rate as a percentage.
        """
        if carts_created == 0:
            return 0.0
        return ((carts_created - completed_purchases) / carts_created) * 100


    def return_on_advertising_spend(revenue_from_ads, advertising_spend):
        """
        Calculate the Return on Advertising Spend (ROAS).

        Parameters
        ----------

        revenue_from_ads
            The revenue generated from ads.
        advertising_spend
            The total advertising spend.

        Returns
        -------
        float
            The ROAS.
        """
        if advertising_spend == 0:
            return 0.0
        return revenue_from_ads / advertising_spend

    def conversion_rate(num_conversions, num_visitors):
        """
        Calculate Conversion Rate
        """
        conversion_rate = (num_conversions / num_visitors) * 100
        return conversion_rate

    def customer_lifetime_value(revenue_per_customer, average_customer_lifetime):
        """
        Calculate Customer Lifetime Value (CLV)
        """
        clv = revenue_per_customer * average_customer_lifetime
        return clv

    def customer_churn_rate(num_customers_lost, total_customers_beginning):
        """
        Calculate Customer Churn Rate
        """
        churn_rate = (num_customers_lost / total_customers_beginning) * 100
        return churn_rate



