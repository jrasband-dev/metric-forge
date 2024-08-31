import polars as pl

@pl.api.register_expr_namespace("forge_web_traffic")
class WebTraffic_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def average_session_duration(total_duration_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Average Session Duration using Polars expressions.

        Parameters:
        total_duration_col (pl.Expr): Column for total duration of all sessions.
        total_sessions_col (pl.Expr): Column for total number of sessions.

        Returns:
        pl.Expr: The average session duration.
        """

        
        return (total_duration_col / pl.when(total_sessions_col == 0).then(1).otherwise(total_sessions_col))

    def bounce_rate(single_page_sessions_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Bounce Rate using Polars expressions.

        Parameters:
        single_page_sessions_col (pl.Expr): Column for sessions where only one page was viewed.
        total_sessions_col (pl.Expr): Column for total number of sessions.

        Returns:
        pl.Expr: The bounce rate as a percentage.
        """
        return (single_page_sessions_col / pl.when(total_sessions_col == 0).then(1).otherwise(total_sessions_col)) * 100

    def click_through_rate(num_clicks_col: str, num_impressions_col: str) -> pl.Expr:
        """
        Calculate Click-Through Rate (CTR) using Polars expressions.

        Parameters:
        num_clicks_col (pl.Expr): Column for the number of clicks.
        num_impressions_col (pl.Expr): Column for the number of impressions.

        Returns:
        pl.Expr: The click-through rate as a percentage.
        """
        return (num_clicks_col / num_impressions_col) * 100

    def cost_per_click(total_cost_col: pl.Expr, num_clicks_col: pl.Expr) -> pl.Expr:
        """
        Calculate Cost per Click (CPC) using Polars expressions.

        Parameters:
        total_cost_col (pl.Expr): Column for the total cost.
        num_clicks_col (pl.Expr): Column for the number of clicks.

        Returns:
        pl.Expr: The cost per click.
        """
        return total_cost_col / pl.when(num_clicks_col == 0).then(1).otherwise(num_clicks_col)

    def exit_rate(exits_col: str, total_page_views_col: str) -> pl.Expr:
        """
        Calculate the Exit Rate using Polars expressions.

        Parameters:
        exits_col (pl.Expr): Column for the number of exits from a specific page.
        total_page_views_col (pl.Expr): Column for the total number of page views.

        Returns:
        pl.Expr: The exit rate as a percentage.
        """
        return (exits_col / pl.when(total_page_views_col == 0).then(1).otherwise(total_page_views_col)) * 100

    def pages_per_session(total_page_views_col: str, total_sessions_col: str) -> pl.Expr:
        """
        Calculate the Pages per Session using Polars expressions.

        Parameters:
        total_page_views_col (pl.Expr): Column for the total number of page views.
        total_sessions_col (pl.Expr): Column for the total number of sessions.

        Returns:
        pl.Expr: The average number of pages per session.
        """
        return total_page_views_col / pl.when(total_sessions_col == 0).then(1).otherwise(total_sessions_col)

