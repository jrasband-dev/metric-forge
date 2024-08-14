def monthly_payment(loan_amount, annual_interest_rate, loan_term):
    """
    Calculate the monthly mortgage payment using the loan amount, annual interest rate, and loan term.

    :param loan_amount: Total loan amount
    :param annual_interest_rate: Annual interest rate (in percentage, e.g., 3.5 for 3.5%)
    :param loan_term: Loan term in months
    :return: Monthly mortgage payment
    """
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term)
    return payment


def refinance_assessment(current_payment=None,
                         new_payment=None,
                         refinance_cost=0,
                         remaining_term=0,
                         new_term=0,
                         current_loan_amount=None,
                         current_interest_rate=None,
                         current_loan_term=None,
                         new_loan_amount=None,
                         new_interest_rate=None,
                         new_loan_term=None,
                         break_even_threshold=None):
    """
    Determine if refinancing is worth it by calculating the break-even point, total savings, and monthly savings.

    :param current_payment: Current monthly mortgage payment (CMP)
    :param new_payment: New monthly mortgage payment after refinancing (NMP)
    :param refinance_cost: Total cost of refinancing (CoR)
    :param remaining_term: Remaining loan term in months (RLT)
    :param new_term: New loan term in months after refinancing (NLT)
    :param current_loan_amount: Current loan amount (Optional if current_payment is provided)
    :param current_interest_rate: Current annual interest rate (Optional if current_payment is provided)
    :param current_loan_term: Original loan term in months (Optional if current_payment is provided)
    :param new_loan_amount: New loan amount after refinancing (Optional if new_payment is provided)
    :param new_interest_rate: New annual interest rate (Optional if new_payment is provided)
    :param new_loan_term: New loan term in months after refinancing (Optional if new_payment is provided)
    :param break_even_threshold: Optional maximum acceptable break-even point in months
    :return: A dictionary containing old and new monthly mortgage payments, break-even point (BEP), total savings (TSOT), monthly savings (MS), and refinance recommendation
    """
    
    if current_payment is None and current_loan_amount is not None and current_interest_rate is not None and current_loan_term is not None:
        current_payment = monthly_payment(current_loan_amount, current_interest_rate, current_loan_term)
        remaining_term = remaining_term or current_loan_term
    
    if new_payment is None and new_loan_amount is not None and new_interest_rate is not None and new_loan_term is not None:
        new_payment = monthly_payment(new_loan_amount, new_interest_rate, new_loan_term)
        new_term = new_term or new_loan_term
    
    if current_payment is None or new_payment is None:
        raise ValueError("Insufficient data provided. Please provide either current/new payments or loan details.")

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
