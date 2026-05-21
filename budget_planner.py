import uuid
from datetime import datetime

_budgets = []

def add_budget(category, amount):
    budget = {
        "id": str(uuid.uuid4()),
        "category": category,
        "amount": float(amount),
        "created_at": datetime.now().isoformat()
    }
    _budgets.append(budget)
    return budget

def get_budgets():
    return list(_budgets)

def calculate_total_budget():
    return sum(b["amount"] for b in _budgets)
