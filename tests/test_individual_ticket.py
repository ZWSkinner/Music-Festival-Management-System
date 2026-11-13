# Tests for core individual functionality

import ticket-manage.py

def test_create_ticket():
    assert ticket_record == ["standard", "5.00",  "500"]

def test_read_ticket():
    assert current_ticket == ["standard", "5.00", "500"]

def test_update_ticket():
    assert ticket_record == ["standard", "8.00", "500"]

def test_delete_ticket():
    assert ticket_record == []

def test_buy_ticket():
    assert ticket_record == ["standard", "8.00", "499"]
    