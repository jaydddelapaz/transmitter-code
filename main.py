radio.set_group(2)

def on_forever():
    radio.send_value("T", 0)
forever(on_forever)
