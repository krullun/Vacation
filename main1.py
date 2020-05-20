import logging
from kiteconnect import KiteTicker
from key import *
from db import insert_candle
from main import Kite
logging.basicConfig(level=logging.DEBUG)

def initkws():
    with open('at.txt', 'r') as f:
        access_token = f.read();
    return KiteTicker(key, access_token)

try:
    kws = initkws()
except:
    kiteinit = Kite(key,secret)
    #debug
    # kite = kiteinit.get()
    # print(kite.holdings())
    kws = initkws()

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    logging.debug("Ticks: {}".format(ticks))
    insert_candle(ticks)

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
    ws.subscribe([738561])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, [738561])

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()