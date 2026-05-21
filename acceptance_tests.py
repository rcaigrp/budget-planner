import pytest
from budget_planner import add_budget, get_budgets, calculate_total_budget, _budgets

@pytest.fixture
def clear_budgets():
    initial = _budgets[:]
    _budgets.clear()
    yield
    _budgets.clear()
    _budgets.extend(initial)

def test_criterion_1_module_exists():
    import budget_planner
    assert budget_planner is not None

def test_criterion_2_add_budget(clear_budgets):
    result = add_budget("Food", 500.0)
    assert isinstance(result, dict)
    assert result["category"] == "Food"
    assert result["amount"] == 500.0

def test_criterion_3_get_budgets(clear_budgets):
    add_budget("Food", 500.0)
    budgets = get_budgets()
    assert isinstance(budgets, list)
    assert len(budgets) == 1

def test_criterion_4_calculate_total_budget(clear_budgets):
    add_budget("Food", 500.0)
    add_budget("Rent", 1000.0)
    total = calculate_total_budget()
    assert total == 1500.0
