def get_category_summary(expenses, category):
    total = sum(exp['amount'] for exp in expenses if exp['category'] == category)
    return total

def get_monthly_summary(expenses, month):
    total = sum(exp['amount'] for exp in expenses if exp['date'].startswith(month))
    return total
