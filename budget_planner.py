class BudgetPlanner:
    def __init__(self):
        self.budgets = []

    def add_budget(self, name, amount):
        budget = {"name": name, "amount": amount}
        self.budgets.append(budget)
        return budget

    def get_budgets(self):
        return self.budgets

    def calculate_total_budget(self):
        return sum(b["amount"] for b in self.budgets)