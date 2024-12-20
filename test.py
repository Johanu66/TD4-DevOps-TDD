import main

def test_hello():
    assert main.hello() == "Hello World !"

def test_events_type():
    assert isinstance(main.events, list)