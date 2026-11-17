import stage_management as stage_management_module
from stage_management import stage_management

def test_input(monkeypatch, tmp_path):
    monkeypatch.setattr(stage_management_module, "STAGES_FILE", tmp_path / "stages.csv")
    inputs = iter([
        "add",
        "Main Stage",
        "5000",
        "Central Park",
        "exit",
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    stage_management()

def test_invalid_choice_shows_try_again(monkeypatch, capsys, tmp_path):
    monkeypatch.setattr(stage_management_module, "STAGES_FILE", tmp_path / "stages.csv")
    inputs = iter(["invalid", "add", "Main Stage", "5000", "Central Park", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    assert "Please try again" in capsys.readouterr().out

def test_view_function(monkeypatch, capsys):
    inputs = iter(["view", "Main Stage"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    assert "view"

def test_view_storage(monkeypatch, capsys, tmp_path):
    stages_file = tmp_path / "stages.csv"
    stages_file.write_text(
        "Stage Name,Stage Capacity,Stage Location\n"
        "Main Stage,5000,Central Park\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(stage_management_module, "STAGES_FILE", stages_file)
    inputs = iter(["view", "Main Stage"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    output = capsys.readouterr().out
    assert "Stage Name: Main Stage" in output
    assert "Stage Capacity: 5000" in output
    assert "Stage Location: Central Park" in output

def test_exit_function(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    stage_management()

    assert "Exiting the stage management system." in capsys.readouterr().out