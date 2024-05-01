import polars as pl
from polars.dataframe import DataFrame


def cac(dataframe: DataFrame ,cost_column:str, customers_column:str) -> DataFrame:
    """
    Calculate Customer Acquisition Cost (CAC)

    Description: The cost of acquiring a new customer. 
    """
    cac = dataframe[cost_column] / dataframe[customers_column]
    dataframe = dataframe.with_columns(cac.alias('CAC'))
    return dataframe

def calculate_clv(revenue_per_customer, average_customer_lifetime):
    """
    Calculate Customer Lifetime Value (CLV)
    """
    clv = revenue_per_customer * average_customer_lifetime
    return clv


def calculate_conversion_rate(num_conversions, num_visitors):
    """
    Calculate Conversion Rate
    """
    conversion_rate = (num_conversions / num_visitors) * 100
    return conversion_rate

def calculate_ctr(num_clicks, num_impressions):
    """
    Calculate Click-Through Rate (CTR)
    """
    ctr = (num_clicks / num_impressions) * 100
    return ctr

def calculate_cpc(total_cost, num_clicks):
    """
    Calculate Cost per Click (CPC)
    """
    cpc = total_cost / num_clicks
    return cpc

def calculate_churn_rate(num_customers_lost, total_customers_beginning):
    """
    Calculate Customer Churn Rate
    """
    churn_rate = (num_customers_lost / total_customers_beginning) * 100
    return churn_rate
