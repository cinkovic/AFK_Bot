import pyautogui as pag
import random
import time

afk_counter = 0
curr_coords = pag.position()

while True:
    # print(curr_coords)
    if pag.position() == curr_coords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_coords = pag.position()
    if afk_counter > 6:
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        pag.moveTo(x, y, duration=0.5)
        curr_coords = pag.position()
    print(f'AFK counter: {afk_counter}, current coords: {curr_coords}')
    time.sleep(2)
