from src.producer import create_event


def test_event_contract():
    event = create_event(7)
    assert event["event_id"] == "evt-7"
    assert event["event_type"] == "purchase"
    assert event["amount"] > 0
    assert 1000 <= event["customer_id"] <= 9999
