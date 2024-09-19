import polars as pl

@pl.api.register_expr_namespace("forge_ecommerce")
class Ecommerce_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def customer_acquisition_cost(self, cost_column: str, customers_column: str) -> pl.Expr:
        """
        Calculate Customer Acquisition Cost (CAC).

        Parameters
        ----------
        cost_column
            Total Customer Aquisition Costs
        customers_column
            Number of New Customers

        Returns
        -------
        Expr

        Notes
        -----
   
        Examples
        --------
        >>> import polars as pl
        ... from metric_forge.ecommerce import * 
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')
        
        >>> data.select(pl.col('cost_of_acquisition'),
        ...             pl.col('new_customers'),
        ...             pl.col('*').forge_ecommerce.customer_acquisition_cost('cost_of_acquisition', 'new_customers'))
        shape: (12, 3)
        ┌─────────────────────┬───────────────┬───────────────────────────┐
        │ cost_of_acquisition ┆ new_customers ┆ customer_acquisition_cost │
        │ ---                 ┆ ---           ┆ ---                       │
        │ f64                 ┆ i64           ┆ f64                       │
        ╞═════════════════════╪═══════════════╪═══════════════════════════╡
        │ 22958.350559        ┆ 406           ┆ 56.547661                 │
        │ 18736.874206        ┆ 234           ┆ 80.072112                 │
        │ 28355.586842        ┆ 120           ┆ 236.296557                │
        │ 14184.81582         ┆ 428           ┆ 33.142093                 │
        │ 18764.339456        ┆ 266           ┆ 70.54263                  │
        │ …                   ┆ …             ┆ …                         │
        │ 33555.278842        ┆ 188           ┆ 178.485526                │
        │ 15990.213465        ┆ 415           ┆ 38.530635                 │
        │ 25427.033152        ┆ 113           ┆ 225.017992                │
        │ 27772.437066        ┆ 341           ┆ 81.444097                 │
        │ 11393.512382        ┆ 364           ┆ 31.300858                 │
        └─────────────────────┴───────────────┴───────────────────────────┘
        """
        cost_expr = pl.col(cost_column)
        customers_expr = pl.col(customers_column)
        return pl.when(customers_expr == 0).then(0.0).otherwise(cost_expr / customers_expr).alias('customer_acquisition_cost')

    def average_order_value(self, total_revenue_column: str, number_of_orders_column: str) -> pl.Expr:
        """
        Calculate the Average Order Value (AOV).

        Parameters
        ----------
        total_revenue_column
            Total Revenue
        number_of_orders_column
            Number of Orders

        Returns
        -------
        Expr

        Notes
        -----
   
        Examples
        --------
        >>> import polars as pl
        ... from metric_forge.ecommerce import * 
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')
        
        >>> data.select(pl.col('total_revenue'),
        ...             pl.col('new_customers'),
        ...             pl.col('*').forge_ecommerce.average_order_value('total_revenue', 'number_of_orders'))
        shape: (12, 3)
        ┌───────────────┬───────────────┬─────────────────────┐
        │ total_revenue ┆ new_customers ┆ average_order_value │
        │ ---           ┆ ---           ┆ ---                 │
        │ f64           ┆ i64           ┆ f64                 │
        ╞═══════════════╪═══════════════╪═════════════════════╡
        │ 87454.011885  ┆ 406           ┆ 88.248246           │
        │ 145071.430641 ┆ 234           ┆ 158.895324          │
        │ 123199.394181 ┆ 120           ┆ 94.405666           │
        │ 109865.84842  ┆ 428           ┆ 124.142202          │
        │ 65601.864044  ┆ 266           ┆ 94.937575           │
        │ …             ┆ …             ┆ …                   │
        │ 136617.614577 ┆ 188           ┆ 206.996386          │
        │ 110111.501174 ┆ 415           ┆ 114.819084          │
        │ 120807.25778  ┆ 113           ┆ 148.594413          │
        │ 52058.44943   ┆ 341           ┆ 99.920248           │
        │ 146990.985216 ┆ 364           ┆ 195.466736          │
        └───────────────┴───────────────┴─────────────────────┘
        """
        total_revenue_expr = pl.col(total_revenue_column)
        number_of_orders_expr = pl.col(number_of_orders_column)
        return pl.when(number_of_orders_expr == 0).then(0.0).otherwise(total_revenue_expr / number_of_orders_expr).alias('average_order_value')

    def cart_abandonment_rate(self, carts_created_column: str, completed_purchases_column: str) -> pl.Expr:
        """
        Calculate the Cart Abandonment Rate.

        Parameters
        ----------
        carts_created_column
            Number of online shopping carts created over a given time period.
        completed_purchases_column
            Number of completed purchases over a given time period.

        Returns
        -------
        Expr

        Notes
        -----
   
        Examples
        --------
        >>> import polars as pl
        ... from metric_forge.ecommerce import * 
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')
        
        >>> data.select(pl.col('carts_created'),
        ...             pl.col('completed_purchases'),
        ...             pl.col('*').forge_ecommerce.cart_abandonment_rate('carts_created', 'completed_purchases'))
        shape: (12, 3)
        ┌───────────────┬─────────────────────┬───────────────────────┐
        │ carts_created ┆ completed_purchases ┆ cart_abandonment_rate │
        │ ---           ┆ ---                 ┆ ---                   │
        │ i64           ┆ i64                 ┆ f64                   │
        ╞═══════════════╪═════════════════════╪═══════════════════════╡
        │ 1969          ┆ 1425                ┆ 27.628238             │
        │ 1506          ┆ 1421                ┆ 5.64409               │
        │ 1497          ┆ 965                 ┆ 35.537742             │
        │ 1963          ┆ 1102                ┆ 43.861437             │
        │ 1009          ┆ 801                 ┆ 20.61447              │
        │ …             ┆ …                   ┆ …                     │
        │ 1108          ┆ 601                 ┆ 45.758123             │
        │ 1975          ┆ 1395                ┆ 29.367089             │
        │ 800           ┆ 669                 ┆ 16.375                │
        │ 2005          ┆ 1215                ┆ 39.401496             │
        │ 1704          ┆ 855                 ┆ 49.823944             │
        └───────────────┴─────────────────────┴───────────────────────┘
       """
    
        carts_created_expr = pl.col(carts_created_column)
        completed_purchases_expr = pl.col(completed_purchases_column)
        return pl.when(carts_created_expr == 0).then(0.0).otherwise(((carts_created_expr - completed_purchases_expr) / carts_created_expr) * 100).alias('cart_abandonment_rate')

    def return_on_advertising_spend(self, revenue_from_ads_column: str, advertising_spend_column: str) -> pl.Expr:
        """
        Calculate the Return on Advertising Spend (ROAS).

        Parameters
        ----------
        revenue_from_ads_column
            Revenue attributed to advertising over a given time period.
        advertising_spend_column
            Advertising expense incurred over a given time period.

        Returns
        -------
        Expr

        Notes
        -----
   
        Examples
        --------
        >>> import polars as pl
        ... from metric_forge.ecommerce import * 
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')

        >>> data.select(pl.col('revenue_from_ads'),
        ...             pl.col('advertising_spend'),
        ...             pl.col('*').forge_ecommerce.return_on_advertising_spend('revenue_from_ads', 'advertising_spend'))
        shape: (12, 3)
        ┌──────────────────┬───────────────────┬─────────────────────────────┐
        │ revenue_from_ads ┆ advertising_spend ┆ return_on_advertising_spend │
        │ ---              ┆ ---               ┆ ---                         │
        │ f64              ┆ f64               ┆ f64                         │
        ╞══════════════════╪═══════════════════╪═════════════════════════════╡
        │ 81339.957696     ┆ 5390.910169       ┆ 15.088353                   │
        │ 76875.083402     ┆ 15585.037018      ┆ 4.932621                    │
        │ 116505.482191    ┆ 14872.037954      ┆ 7.833861                    │
        │ 106008.046381    ┆ 12337.204368      ┆ 8.59255                     │
        │ 97258.809912     ┆ 5351.995568       ┆ 18.172438                   │
        │ …                ┆ …                 ┆ …                           │
        │ 116872.977654    ┆ 24754.388513      ┆ 4.721303                    │
        │ 84633.082292     ┆ 20148.99937       ┆ 4.200362                    │
        │ 54839.926382     ┆ 28157.521963      ┆ 1.947612                    │
        │ 56664.615513     ┆ 21276.925638      ┆ 2.663196                    │
        │ 44874.024516     ┆ 27873.991889      ┆ 1.609889                    │
        └──────────────────┴───────────────────┴─────────────────────────────┘
        """
        revenue_from_ads_expr = pl.col(revenue_from_ads_column)
        advertising_spend_expr = pl.col(advertising_spend_column)
        return pl.when(advertising_spend_expr == 0).then(0.0).otherwise(revenue_from_ads_expr / advertising_spend_expr).alias('return_on_advertising_spend')

    def conversion_rate(self, num_conversions_column: str, num_visitors_column: str) -> pl.Expr:
        """
        Calculate Conversion Rate.

        Parameters
        ----------
        num_conversions_column
            Total number of conversions for a given time period. Definition is subjective. 
        num_visitors_column
            Total number of visitors for a given time period.

        Returns
        -------
        Expr

        Notes
        -----
   
        Examples
        --------
        >>> import polars as pl
        ... from metric_forge.ecommerce import * 
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')

        >>> data.select(pl.col('num_conversions'),
        ...             pl.col('num_visitors'),
        ...             pl.col('*').forge_ecommerce.conversion_rate('num_conversions', 'num_visitors'))
        shape: (12, 3)
        ┌─────────────────┬──────────────┬─────────────────┐
        │ num_conversions ┆ num_visitors ┆ conversion_rate │
        │ ---             ┆ ---          ┆ ---             │
        │ i64             ┆ i64          ┆ f64             │
        ╞═════════════════╪══════════════╪═════════════════╡
        │ 300             ┆ 13154        ┆ 2.280675        │
        │ 427             ┆ 14762        ┆ 2.892562        │
        │ 367             ┆ 10056        ┆ 3.649562        │
        │ 132             ┆ 19948        ┆ 0.66172         │
        │ 147             ┆ 13110        ┆ 1.121281        │
        │ …               ┆ …            ┆ …               │
        │ 392             ┆ 8840         ┆ 4.434389        │
        │ 198             ┆ 6028         ┆ 3.284672        │
        │ 271             ┆ 12385        ┆ 2.188131        │
        │ 459             ┆ 5502         ┆ 8.342421        │
        │ 313             ┆ 11910        ┆ 2.628044        │
        └─────────────────┴──────────────┴─────────────────┘
        """
        num_conversions_expr = pl.col(num_conversions_column)
        num_visitors_expr = pl.col(num_visitors_column)
        return pl.when(num_visitors_expr == 0).then(0.0).otherwise((num_conversions_expr / num_visitors_expr) * 100).alias('conversion_rate')

    def customer_lifetime_value(self, revenue_per_customer_column: str, average_customer_lifetime_column: str, method='basic', **kwargs) -> pl.Expr:
        """
        Calculate Customer Lifetime Value (CLV).        

        **Basic Method:**

        .. math::

            CLV = R \\times L

        where:

        - CLV is the customer lifetime value,
        - R is the average revenue per customer,
        - L is the average customer lifetime.

        
        **Discounted**

        .. math::

            CLV_{discounted} = \\frac{R \\times L}{(1 + d)}

        where:

        - d is the discount rate.

        Parameters
        ----------
        revenue_per_customer_column
            Total revenue per customer measured yearly. 
        average_customer_lifetime_column
            Number of years the customer is expected to be a paying customer.
        method
            The CLV method used. Can be any of the following:

            * `basic (default)`: Simple calculation. Does not take other factors into account.
            * `discounted`: takes into account the present value of future cash flows
            * `predictive`: uses probabilities and costs to estimate the lifetime value

        Returns
        -------
        Expr

        Examples
        --------
        >>> from metric_forge.ecommerce import * 
        ... import polars as pl
        ... data = pl.read_csv('datasets/ecommerce_metrics.csv')

        >>> data.select(pl.col('revenue_per_customer'),
        ...             pl.col('average_customer_lifetime'),
        ...             pl.col('*').forge_ecommerce.customer_lifetime_value(revenue_per_customer_column='revenue_per_customer',average_customer_lifetime_column='average_customer_lifetime',method='basic'))
        shape: (12, 3)
        ┌──────────────────────┬───────────────────────────┬─────────────────────────┐
        │ revenue_per_customer ┆ average_customer_lifetime ┆ customer_lifetime_value │
        │ ---                  ┆ ---                       ┆ ---                     │
        │ f64                  ┆ f64                       ┆ f64                     │
        ╞══════════════════════╪═══════════════════════════╪═════════════════════════╡
        │ 202.427329           ┆ 3.159364                  ┆ 639.54169               │
        │ 116.173436           ┆ 1.812245                  ┆ 210.534716              │
        │ 384.265156           ┆ 4.771414                  ┆ 1833.488253             │
        │ 144.356328           ┆ 3.395462                  ┆ 490.156408              │
        │ 275.734601           ┆ 3.77914                   ┆ 1042.039585             │
        │ …                    ┆ …                         ┆ …                       │
        │ 290.148089           ┆ 2.182535                  ┆ 633.258286              │
        │ 325.310229           ┆ 1.421977                  ┆ 462.583676              │
        │ 378.206435           ┆ 2.826138                  ┆ 1068.863683             │
        │ 155.732582           ┆ 1.873762                  ┆ 291.805755              │
        │ 341.766952           ┆ 2.66604                   ┆ 911.164293              │
        └──────────────────────┴───────────────────────────┴─────────────────────────┘
        """
        
        if method == 'basic':
            revenue_per_customer_expr = pl.col(revenue_per_customer_column)
            average_customer_lifetime_expr = pl.col(average_customer_lifetime_column)
            return (revenue_per_customer_expr * average_customer_lifetime_expr).alias('customer_lifetime_value')

        elif method == 'discounted':
            discount_rate_column = kwargs.get('discount_rate_column', 'discount_rate')  # Default column name
            revenue_per_customer_expr = pl.col(revenue_per_customer_column)
            average_customer_lifetime_expr = pl.col(average_customer_lifetime_column)
            discount_rate_expr = pl.col(discount_rate_column)

            return (revenue_per_customer_expr * average_customer_lifetime_expr / (1 + discount_rate_expr)).alias('discounted_customer_lifetime_value')

        else:
            raise ValueError("Invalid method selected")

    def customer_churn_rate(self, num_customers_lost_column: str, total_customers_beginning_column: str) -> pl.Expr:
        """
        Calculate Customer Churn Rate.
        """
        num_customers_lost_expr = pl.col(num_customers_lost_column)
        total_customers_beginning_expr = pl.col(total_customers_beginning_column)
        return pl.when(total_customers_beginning_expr == 0).then(0.0).otherwise((num_customers_lost_expr / total_customers_beginning_expr) * 100).alias('customer_churn_rate')
