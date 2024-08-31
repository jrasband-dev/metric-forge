from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime, timedelta
import math
import polars as pl


def monthly_payment(loan_amount: float, annual_interest_rate: float, loan_term: int) -> float:
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    return loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term)



@dataclass
class RefinanceOption:
    new_loan_amount: float
    new_annual_interest_rate: float
    new_term_years: int
    associated_costs: float

    def calculate_new_payment(self) -> float:
        # Method implementation
        pass


@dataclass
class Mortgage:
    principal: float
    annual_interest_rate: float
    term_years: int
    start_date: str = None
    extra_principal_payment: float = 0

    def __post_init__(self):
        self.calculate_monthly_payment()

    def calculate_monthly_payment(self) -> float:
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        number_of_payments = self.term_years * 12
        if monthly_interest_rate > 0:
            self.monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        else:
            self.monthly_payment = self.principal / number_of_payments

        return self.monthly_payment

    def generate_amortization_schedule(self) -> pl.DataFrame:
        schedule = []
        principal_remaining = self.principal
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        payment = self.monthly_payment
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')

        for i in range(1, self.term_years * 12 + 1):
            interest_payment = principal_remaining * monthly_interest_rate
            principal_payment = payment - interest_payment
            principal_remaining -= principal_payment
            payment_date = start_date + timedelta(days=30 * i)
            schedule.append({
                'payment_number': i,
                'payment_date': payment_date.strftime('%Y-%m-%d'),
                'payment': payment,
                'interest_payment': interest_payment,
                'principal_payment': principal_payment,
                'principal_remaining': max(principal_remaining, 0),
            })

        return pl.DataFrame(schedule)

    def loan_to_value_ratio(self, home_value: float) -> float:
        return (self.principal / home_value) * 100

    def total_interest_paid(self) -> float:
        total_payment = self.monthly_payment * self.term_years * 12
        return total_payment - self.principal

    def calculate_principal_only_payment(self) -> Dict[str, float]:
        monthly_interest_rate = self.annual_interest_rate / 12 / 100
        number_of_payments = self.term_years * 12
        total_payment = self.monthly_payment + self.extra_principal_payment

        if monthly_interest_rate > 0:
            new_term_months = math.log((total_payment / (total_payment - self.principal * monthly_interest_rate))) / math.log(1 + monthly_interest_rate)
        else:
            new_term_months = self.principal / total_payment

        new_term_years = new_term_months / 12
        time_saved_years = self.term_years - new_term_years

        return {
            'new_term_years': new_term_years,
            'time_saved_years': time_saved_years
        }

    def to_dict(self) -> Dict[str, float]:
        return {
            'principal': self.principal,
            'annual_interest_rate': self.annual_interest_rate,
            'term_years': self.term_years,
            'monthly_payment': self.monthly_payment,
            'extra_principal_payment': self.extra_principal_payment,
        }

    def amortization_to_dict(self) -> pl.DataFrame:
        return self.generate_amortization_schedule()
    
    def refinance_assessment(self, refinance_option: RefinanceOption, break_even_threshold=36) -> Dict[str, float]:
        """
        Determine if refinancing is worth it by calculating the break-even point, total savings, and monthly savings.

        :param refinance_option: RefinanceOption object containing new loan details
        :param break_even_threshold: Optional maximum acceptable break-even point in months
        :return: A dictionary containing old and new monthly mortgage payments, break-even point (BEP), total savings (TSOT), monthly savings (MS), and refinance recommendation
        """
        current_payment = self.monthly_payment
        current_loan_amount = self.principal
        current_interest_rate = self.annual_interest_rate
        current_loan_term = self.term_years * 12  # Convert years to months
        remaining_term = current_loan_term  # Use the full term as the remaining term for simplicity

        # Extract details from RefinanceOption
        new_payment = monthly_payment(refinance_option.new_loan_amount, refinance_option.new_annual_interest_rate, refinance_option.new_term_years * 12)
        new_term = refinance_option.new_term_years * 12
        refinance_cost = refinance_option.associated_costs

        monthly_savings = current_payment - new_payment
        
        break_even_point = refinance_cost / monthly_savings if monthly_savings > 0 else float('inf')
        
        total_cost_current = remaining_term * current_payment
        total_cost_new = new_term * new_payment + refinance_cost
        total_savings = total_cost_current - total_cost_new

        should_refinance = (break_even_point < remaining_term and total_savings > 0) if break_even_threshold is None else (break_even_point < break_even_threshold and total_savings > 0)

        return {
            "Old Monthly Payment": current_payment,
            "New Monthly Payment": new_payment,
            "Monthly Savings": monthly_savings,
            "Break-Even Point (months)": break_even_point,
            "Total Savings (over the loan term)": total_savings,
            "Should Refinance": should_refinance
        }

