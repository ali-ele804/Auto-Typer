import pyautogui
import time

# im dying inside

__title__ = """
    _         _      _____
   / \  _   _| |_ __|_   __   _ _ __   ___ _ __
  / _ \| | | | __/ _ \| || | | | '_ \ / _ | '__|
 / ___ | |_| | || (_) | || |_| | |_) |  __| |
/_/   \_\__,_|\__\___/|_| \__, | .__/ \___|_|
                          |___/|_|
                                       by Ali
"""
print(__title__)

print("NOTE! Failsafe will be triggered if put the cursor on a corner on screen.\n")

print("\nTo start i need info:\n")

sentence = input("What would you like the sentence to be?: ")

_time_ = input("How many lines would you like it to create? (0 for infinite): ")

_time_ = int(_time_) -1

delay = input("How long do you want it to delay? This is for applications that block spamming like Discord, (0 & Decimal point for milliseconds) (0 for none): ")

delay = float(delay)

input("Once this starts it will begin typing. Before you start go to the desired application . Press enter to begin.")

if _time_ == -1:
    while(1 < 2):
        pyautogui.typewrite(sentence)

        time.sleep(delay)

        pyautogui.press("enter")

for i in range(_time_):

    pyautogui.typewrite(sentence)

    time.sleep(delay)

    pyautogui.press("enter")
