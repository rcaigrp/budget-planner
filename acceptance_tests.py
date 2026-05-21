import pytest
from budget_planner import BudgetPlanner

@pytest.fixture
def planner():
    return BudgetPlanner()

def test_criterion_1_module_import():
    from budget_planner import BudgetPlanner
    assert BudgetPlanner is not None

def test_criterion_2_add_budget_returns_dict(planner):
    result = planner.add_budget("Food", 100)
    assert isinstance(result, dict)
    assert result["name"] == "Food"
    assert result["amount"] == 100

def test_criterion_3_get_budgets_returns_list(planner):
    planner.add_budget("Food", 100)
    budgets = planner.get_budgets()
    assert isinstance(budgets, list)
    assert len(budgets) == 1

def test_criterion_4_calculate_total_budget(planner):
    planner.add_budget("Food", 100)
    planner.add_budget("Travel", 50)
    total = planner.calculate_total_budget()
    assert total == 150