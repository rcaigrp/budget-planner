import pytest
from budget_planner import add_budget, get_budgets, calculate_remaining

@pytest.fixture
def clear_budgets():
    from budget_planner import _budgets
    _budgets.clear()
    yield
    _budgets.clear()

def test_criterion_1_module_exists():
    import budget_planner
    assert budget_planner is not None

def test_criterion_2_add_budget():
    result = add_budget(category="food", amount=50)
    assert isinstance(result, dict)
    assert result["category"] == "food"
    assert result["amount"] == 50

def test_criterion_3_get_budgets():
    add_budget(category="food", amount=50)
    budgets = get_budgets()
    assert isinstance(budgets, list)
    assert len(budgets) == 1

def test_criterion_4_calculate_remaining():
    add_budget(category="food", amount=50)
    add_budget(category="transport", amount=30)
    remaining = calculate_remaining(100)
    assert remaining == 20
