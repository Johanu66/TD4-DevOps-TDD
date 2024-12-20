import main
from datetime import datetime, timedelta

def test_hello():
    assert main.hello() == "Hello World !"

def test_events_type():
    assert isinstance(main.events, list)

def test_add_event():
    start_time = datetime.now()
    main.create_event(start_time, 100, "Event 1")
    assert main.events == [(start_time, 100, "Event 1")]