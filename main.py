def hello(msg="Hello World !"):
    return msg

events = []

def create_event(start_time, duration, name):
    events.append((start_time, duration, name))