from pynput.keyboard import Controller as KeyboardController, Key, Listener
from pynput.mouse import Controller as MouseController, Button
from threading import Thread
from time import sleep
from json import load

with open("config.json", "r") as f:
    config = load(f)

kb = KeyboardController()
m = MouseController()

def reset_pos():
    print("Started reset pos thread.")
    while True:
        kb.press("e")
        sleep(0.1)
        kb.release("e")
        sleep(4)
        kb.press(Key.space)
        sleep(0.1)
        kb.release(Key.space)
        sleep(0.5)

def summon_minions():
    print("Started summon minions thread.")
    kb.press(config["summonKey"])
    sleep(0.1)
    kb.release(config["summonKey"])
    while True:
        for _ in range(config["summonCount"]):
            m.press(Button.left)
            sleep(0.5)
            m.release(Button.left)
            sleep(0.1)
        sleep(30)

def check_exit(key):
    if key == Key.esc:
        print("Exiting.")
        raise SystemExit()

print("Program will start in 5 seconds.")
sleep(5)

Thread(target=reset_pos, daemon=True).start()
Thread(target=summon_minions, daemon=True).start()

with Listener(
    on_press=check_exit,
) as listener:
    listener.join()
