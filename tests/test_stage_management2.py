import stage_management  # pyright: ignore[reportMissingImports]
import pytest


@pytest.fixture(autouse=True)
def clear_stages():
    stage_management.stages.clear()


def test_add():
    result = stage_management.add("Main Stage", 5000, "Central Park")
    assert result == "added stage successfully"

def test_view_existing_stage():
    stage_management.add("Main Stage", 5000, "Central Park")
    result = stage_management.view("Main Stage")  # This will print the stage details
    assert result == "Stage Name: Main Stage, Stage Capacity: 5000, Stage Location: Central Park"

def test_view_non_existing_stage():
    result = stage_management.view("Non-Existing Stage")  
    assert result == "Stage not found: Non-Existing Stage Please try agian."

def test_add_invalid_capacity():
    result = stage_management.add("Small Stage", "invalid_capacity", "Downtown")
    assert result == "Invalid input. Please enter a valid number for stage capacity."

def test_add_and_view_multiple_stages():
    stage_management.add("Stage A", 3000, "Location A")
    stage_management.add("Stage B", 4000, "Location B")
    
    result_a = stage_management.view("Stage A")
    result_b = stage_management.view("Stage B")
    
    assert result_a == "Stage Name: Stage A, Stage Capacity: 3000, Stage Location: Location A"
    assert result_b == "Stage Name: Stage B, Stage Capacity: 4000, Stage Location: Location B"

def test_view_all_stages():
    stage_management.add("Stage X", 2000, "Location X")
    stage_management.add("Stage Y", 2500, "Location Y")
    
    result_all = stage_management.view("All")
    
    assert result_all == "Stage Name: Stage X, Stage Capacity: 2000, Stage Location: Location X\n" + "Stage Name: Stage Y, Stage Capacity: 2500, Stage Location: Location Y\n"

def test_update_stage():
    stage_management.add("stage V", 12333, "location 5")
    result = stage_management.update("stage V", "new_stage_name", 6000, "new_location")
    assert result == "Updated stage V name to new_stage_name."


def test_update_invalid():
    stage_management.add("stage V", 12333, "location 5") 
    result = stage_management.update("stage V", "new_stage_name", "six", "new_location")
    assert result == "Invalid input. Please enter a valid number for stage capacity."

def test_delete():
    stage_management.add("test stage", 6400,"test location")
    stage_management.delete("test stage")
    result = stage_management.view("test stage")
    assert result == "Stage not found: test stage Please try agian."

def test_delete_invalid():
    result = stage_management.delete("invalid stage")
    assert result == "Nothing to delete"