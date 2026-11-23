import stage_management
""" TODO:
REMEBER TO DO TESTS FIRST.
add functionality to update and delete stages.
add persistence to the stages dictionary using a file type try json.
"""
def test_input(monkeypatch, tmp_path):
    inputs = iter([
        "add",
        "Main Stage",
        "5000",
        "Central Park",
        "exit",
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    stage_management.stage_management()

def test_invalid_choice_shows_try_again(monkeypatch, capsys, tmp_path):
    inputs = iter(["invalid",
                    "add", 
                    "Main Stage", 
                    "5000", 
                    "Central Park",
                     "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management.stage_management()

    assert "Please try again" in capsys.readouterr().out

def test_view_function(monkeypatch, capsys):
    stage_management.stages["Main Stage"] = {
        "Stage Name": "Main Stage",
        "Stage Capacity": 5000,
        "Stage Location": "Central Park",
    }
    inputs = iter(["view", "Main Stage", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management.stage_management()

    output = capsys.readouterr().out
    assert "Stage Name: Main Stage" in output
    assert "Stage Capacity: 5000" in output
    assert "Stage Location: Central Park" in output

def test_exit_function(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management.stage_management()

    assert "Exiting the stage management system." in capsys.readouterr().out


#def test_