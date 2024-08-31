import polars as pl


class WebTraffic_SVF:
    def average_session_duration(total_duration, total_sessions):
        """
        Calculate the Average Session Duration.

        Parameters:
        total_duration (float): The total duration of all sessions in seconds.
        total_sessions (int): The total number of sessions.

        Returns:
        float: The average session duration in seconds.
        """
        if total_sessions == 0:
            return 0.0
        return total_duration / total_sessions

    def bounce_rate(single_page_sessions, total_sessions):
        """
        Calculate the Bounce Rate.

        Parameters:
        single_page_sessions (int): The number of sessions where only one page was viewed.
        total_sessions (int): The total number of sessions.

        Returns:
        float: The bounce rate as a percentage.
        """
        if total_sessions == 0:
            return 0.0
        return (single_page_sessions / total_sessions) * 100

    def click_through_rate(num_clicks, num_impressions):
        """
        Calculate Click-Through Rate (CTR)
        """
        ctr = (num_clicks / num_impressions) * 100
        return ctr

    def cost_per_click(total_cost, num_clicks):
        """
        Calculate Cost per Click (CPC)
        """
        cpc = total_cost / num_clicks
        return cpc

    def exit_rate(exits, total_page_views):
        """
        Calculate the Exit Rate.

        Parameters:
        exits (int): The number of exits from a specific page.
        total_page_views (int): The total number of page views.

        Returns:
        float: The exit rate as a percentage.
        """
        if total_page_views == 0:
            return 0.0
        return (exits / total_page_views) * 100

    def pages_per_session(total_page_views, total_sessions):
        """
        Calculate the Pages per Session.

        Parameters:
        total_page_views (int): The total number of page views.
        total_sessions (int): The total number of sessions.

        Returns:
        float: The average number of pages per session.
        """
        if total_sessions == 0:
            return 0.0
        return total_page_views / total_sessions


