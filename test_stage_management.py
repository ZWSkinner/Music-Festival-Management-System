import pytest
from stage_management import stage_management

def test_input(monkeypatch):
    # Simulate user input for the stage_management function
    inputs = iter([
        "add",
        "Main Stage",
        "5000",
        "Central Park"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run the stage-management workflow with mocked input.

    
    stage_management()

def test_invalid_choice_shows_try_again(monkeypatch, capsys):
    inputs = iter(["invalid", "add", "Main Stage", "5000", "Central Park"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    assert "Please try again" in capsys.readouterr().out

def test_view_function(monkeypatch, capsys):
    inputs = iter(["view", "Main Stage"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    assert "view"