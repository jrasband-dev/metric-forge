


class ProductDevelopment_SVF:
    def opportunity_score(importance: float, satisfaction: float) -> float:
        '''
        Opportunity Score
        
        Source: What Customers Want, Anthony Ulwick
        '''
        if importance == 0:
            return 0.0
        return importance + (importance - satisfaction)

    def customer_value_delivered(importance: float, satisfaction: float) -> float:
        '''
        Customer Value Delivered
        
        Source: The Lean Product Playbook, Dan Olsen
        '''
        return (importance / 10) * (satisfaction / 10)

    def opportunity_to_add_value(importance: float, satisfaction: float) -> float:
        '''
        Opportunity to Add Value

        Source: The Lean Product Playbook, Dan Olsen
        '''
        return (importance / 10) * (1 - satisfaction / 10)

    def customer_value_created(importance: float, satisfaction_before: float, satisfaction_after: float) -> float:
        '''
        Customer Value Created

        Source: The Lean Product Playbook, Dan Olsen
        '''
        return (importance / 10) * ((satisfaction_after / 10) - (satisfaction_before / 10))
