import polars as pl

@pl.api.register_expr_namespace("forge_operations")
class Operations_Polars:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    # Cycle Time (e.g., production cycle time)
    def cycle_time(self, total_production_time_column: str, units_produced_column: str) -> pl.Expr:
        total_production_time_expr = pl.col(total_production_time_column)
        units_produced_expr = pl.col(units_produced_column)
        return pl.when(units_produced_expr == 0).then(0.0).otherwise(total_production_time_expr / units_produced_expr).alias('cycle_time')

    # Throughput (e.g., units produced per period)
    def throughput(self, units_produced_column: str, time_period_column: str) -> pl.Expr:
        units_produced_expr = pl.col(units_produced_column)
        time_period_expr = pl.col(time_period_column)
        return pl.when(time_period_expr == 0).then(0.0).otherwise(units_produced_expr / time_period_expr).alias('throughput')

    # Overall Equipment Effectiveness (OEE)
    def oee(self, availability_column: str, performance_column: str, quality_column: str) -> pl.Expr:
        availability_expr = pl.col(availability_column)
        performance_expr = pl.col(performance_column)
        quality_expr = pl.col(quality_column)
        return (availability_expr * performance_expr * quality_expr).alias('oee')

    # Capacity Utilization Rate
    def capacity_utilization(self, actual_output_column: str, potential_output_column: str) -> pl.Expr:
        actual_output_expr = pl.col(actual_output_column)
        potential_output_expr = pl.col(potential_output_column)
        return pl.when(potential_output_expr == 0).then(0.0).otherwise(actual_output_expr / potential_output_expr).alias('capacity_utilization')

    # Defect Rate
    def defect_rate(self, defective_units_column: str, total_units_produced_column: str) -> pl.Expr:
        defective_units_expr = pl.col(defective_units_column)
        total_units_produced_expr = pl.col(total_units_produced_column)
        return pl.when(total_units_produced_expr == 0).then(0.0).otherwise(defective_units_expr / total_units_produced_expr).alias('defect_rate')

    # Lead Time (e.g., time from order to delivery)
    def lead_time(self, order_date_column: str, delivery_date_column: str) -> pl.Expr:
        order_date_expr = pl.col(order_date_column)
        delivery_date_expr = pl.col(delivery_date_column)
        return (delivery_date_expr - order_date_expr).alias('lead_time')
