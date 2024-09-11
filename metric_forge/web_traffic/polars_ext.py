import polars as pl

@pl.api.register_expr_namespace("forge_web_traffic")
class WebTraffic_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def average_session_duration(self, total_duration_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Average Session Duration using Polars expressions.

        Parameters:
        total_duration_col (str): Column name for total duration of all sessions.
        total_sessions_col (str): Column name for total number of sessions.

        Returns:
        pl.Expr: The average session duration with alias.
        """
        return (pl.col(total_duration_col) / 
                pl.when(pl.col(total_sessions_col) == 0)
                  .then(1)
                  .otherwise(pl.col(total_sessions_col))
               ).alias("average_session_duration")

    def bounce_rate(self, single_page_sessions_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Bounce Rate using Polars expressions.

        Parameters:
        single_page_sessions_col (str): Column name for sessions where only one page was viewed.
        total_sessions_col (str): Column name for total number of sessions.

        Returns:
        pl.Expr: The bounce rate as a percentage with alias.
        """
        return (pl.col(single_page_sessions_col) / 
                pl.when(pl.col(total_sessions_col) == 0)
                  .then(1)
                  .otherwise(pl.col(total_sessions_col)) * 100
               ).alias("bounce_rate")

    def click_through_rate(self, num_clicks_col: str, num_impressions_col: str) -> pl.Expr:
        """
        Calculate Click-Through Rate (CTR) using Polars expressions.

        Parameters:
        num_clicks_col (str): Column name for the number of clicks.
        num_impressions_col (str): Column name for the number of impressions.

        Returns:
        pl.Expr: The click-through rate as a percentage with alias.
        """
        return (pl.col(num_clicks_col) / pl.col(num_impressions_col) * 100).alias("click_through_rate")

    def cost_per_click(self, total_cost_col: str, num_clicks_col: str) -> pl.Expr:
        """
        Calculate Cost per Click (CPC) using Polars expressions.

        Parameters:
        total_cost_col (str): Column name for the total cost.
        num_clicks_col (str): Column name for the number of clicks.

        Returns:
        pl.Expr: The cost per click with alias.
        """
        return (pl.col(total_cost_col) / 
                pl.when(pl.col(num_clicks_col) == 0).then(1).otherwise(pl.col(num_clicks_col))
               ).alias("cost_per_click")

    def exit_rate(self, exits_col: str, total_page_views_col: str) -> pl.Expr:
        """
        Calculate the Exit Rate using Polars expressions.

        Parameters:
        exits_col (str): Column name for the number of exits from a specific page.
        total_page_views_col (str): Column name for the total number of page views.

        Returns:
        pl.Expr: The exit rate as a percentage with alias.
        """
        return (pl.col(exits_col) / 
                pl.when(pl.col(total_page_views_col) == 0)
                  .then(1)
                  .otherwise(pl.col(total_page_views_col)) * 100
               ).alias("exit_rate")

    def pages_per_session(self, total_page_views_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Pages per Session using Polars expressions.

        Parameters:
        total_page_views_col (str): Column name for the total number of page views.
        total_sessions_col (str): Column name for the total number of sessions.

        Returns:
        pl.Expr: The average number of pages per session with alias.
        """
        return (pl.col(total_page_views_col) / 
                pl.when(pl.col(total_sessions_col) == 0).then(1).otherwise(pl.col(total_sessions_col))
               ).alias("pages_per_session")
