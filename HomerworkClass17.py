def calculate_due_amount(total_bill, amount_paid):
    """
    Calculates the due amount after a customer pays a bill.
    """
    due_amount = total_bill - amount_paid
    return due_amount

# Example usage
bill = 150.00
payment = 100.00
remaining_due = calculate_due_amount(bill, payment)
print(f"The remaining due amount is: ${remaining_due:.2f}")