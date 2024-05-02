from polars.dataframe import DataFrame
import polars as pl

def opportunity_score(df:DataFrame, importance_col:str, satisfaction_col:str) -> DataFrame:
    '''
    Opportunity Score
    
    Source: What Customers Want, Anthony Ulwick

    Input:
    ┌──────────────┬──────────────────┬────────────────────┐
    │ feature_name ┆ importance_score ┆ satisfaction_score │
    │ ---          ┆ ---              ┆ ---                │
    │ str          ┆ i64              ┆ i64                │
    ╞══════════════╪══════════════════╪════════════════════╡
    │ Feature1     ┆ 8                ┆ 7                  │
    │ Feature2     ┆ 9                ┆ 8                  │
    │ Feature3     ┆ 7                ┆ 9                  │
    │ Feature4     ┆ 8                ┆ 7                  │
    │ Feature5     ┆ 6                ┆ 6                  │
    │ Feature6     ┆ 9                ┆ 8                  │
    │ Feature7     ┆ 7                ┆ 9                  │
    │ Feature8     ┆ 6                ┆ 7                  │
    │ Feature9     ┆ 9                ┆ 8                  │
    │ Feature10    ┆ 8                ┆ 7                  │
    └──────────────┴──────────────────┴────────────────────┘
    '''
    df = df.with_columns(opportunity_score = pl.col(importance_col) + (pl.col(importance_col) - pl.col(satisfaction_col)).apply(lambda x: x if x >= 0 else 0,return_dtype=pl.UInt32))
    return df

def customer_value_delivered(df:DataFrame, importance_col:str, satisfaction_col:str) -> DataFrame:
    '''
    Customer Value Delivered
    
    Source: The Lean Product Playbook, Dan Olsen

    Input:
    ┌──────────────┬──────────────────┬────────────────────┐
    │ feature_name ┆ importance_score ┆ satisfaction_score │
    │ ---          ┆ ---              ┆ ---                │
    │ str          ┆ i64              ┆ i64                │
    ╞══════════════╪══════════════════╪════════════════════╡
    │ Feature1     ┆ 8                ┆ 7                  │
    │ Feature2     ┆ 9                ┆ 8                  │
    │ Feature3     ┆ 7                ┆ 9                  │
    │ Feature4     ┆ 8                ┆ 7                  │
    │ Feature5     ┆ 6                ┆ 6                  │
    │ Feature6     ┆ 9                ┆ 8                  │
    │ Feature7     ┆ 7                ┆ 9                  │
    │ Feature8     ┆ 6                ┆ 7                  │
    │ Feature9     ┆ 9                ┆ 8                  │
    │ Feature10    ┆ 8                ┆ 7                  │
    └──────────────┴──────────────────┴────────────────────┘
    '''
    cvd = df[importance_col]/10 * df[satisfaction_col]/10
    df = df.with_columns(cvd.alias('customer_value_delivered'))
    return df

def opportunity_to_add_value(df:DataFrame, importance_col:str, satisfaction_col:str) -> DataFrame:
    '''
    Opportunity to Add Value

    Source: The Lean Product Playbook, Dan Olsen

    Input:
    ┌──────────────┬──────────────────┬────────────────────┐
    │ feature_name ┆ importance_score ┆ satisfaction_score │
    │ ---          ┆ ---              ┆ ---                │
    │ str          ┆ i64              ┆ i64                │
    ╞══════════════╪══════════════════╪════════════════════╡
    │ Feature1     ┆ 8                ┆ 7                  │
    │ Feature2     ┆ 9                ┆ 8                  │
    │ Feature3     ┆ 7                ┆ 9                  │
    │ Feature4     ┆ 8                ┆ 7                  │
    │ Feature5     ┆ 6                ┆ 6                  │
    │ Feature6     ┆ 9                ┆ 8                  │
    │ Feature7     ┆ 7                ┆ 9                  │
    │ Feature8     ┆ 6                ┆ 7                  │
    │ Feature9     ┆ 9                ┆ 8                  │
    │ Feature10    ┆ 8                ┆ 7                  │
    └──────────────┴──────────────────┴────────────────────┘
    '''
    otav = df[importance_col]/10 * (1-df[satisfaction_col]/10)
    df = df.with_columns(otav.alias('opp_to_add_value'))
    return df

def customer_value_created(df:DataFrame
                           ,importance_col:str
                           ,satisfaction_before_col:str
                           ,satisfaction_after_col:str ) -> DataFrame:
    '''
    Customer Value Created

    Source: The Lean Product Playbook, Dan Olsen

    Input:
    ┌──────────────┬──────────────────┬───────────────────────────┬──────────────────────────┐
    │ feature_name ┆ importance_score ┆ satisfaction_score_before ┆ satisfaction_score_after │
    │ ---          ┆ ---              ┆ ---                       ┆ ---                      │
    │ str          ┆ i64              ┆ i64                       ┆ i64                      │
    ╞══════════════╪══════════════════╪═══════════════════════════╪══════════════════════════╡
    │ Feature1     ┆ 8                ┆ 7                         ┆ 9                        │
    │ Feature2     ┆ 9                ┆ 8                         ┆ 9                        │
    │ Feature3     ┆ 7                ┆ 9                         ┆ 8                        │
    │ Feature4     ┆ 8                ┆ 7                         ┆ 8                        │
    │ Feature5     ┆ 6                ┆ 6                         ┆ 8                        │
    │ Feature6     ┆ 9                ┆ 8                         ┆ 9                        │
    │ Feature7     ┆ 7                ┆ 9                         ┆ 8                        │
    │ Feature8     ┆ 6                ┆ 7                         ┆ 6                        │
    │ Feature9     ┆ 9                ┆ 8                         ┆ 8                        │
    │ Feature10    ┆ 8                ┆ 7                         ┆ 7                        │
    └──────────────┴──────────────────┴───────────────────────────┴──────────────────────────┘
    '''
    cvc = df[importance_col]/10 * (df[satisfaction_after_col]/10 - df[satisfaction_before_col]/10)
    df = df.with_columns(cvc.alias('customer_value_created'))
    return df
