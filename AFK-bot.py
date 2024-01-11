import pyautogui as pag
import random
import time


def random_movement():
    x = random.randint(0, pag.size().width)
    y = random.randint(0, pag.size().height)
    pag.moveTo(x, y, duration=random.uniform(0.1, 1.0))


def main(afk_threshold=6, check_interval=2):
    afk_counter = 0
    curr_coords = pag.position()

    while True:
        if pag.position() == curr_coords:
            afk_counter += 1
        else:
            afk_counter = 0
            curr_coords = pag.position()
        
        if afk_counter > afk_threshold:
            random_movement()
            curr_coords = pag.position()
        
        time.sleep(random.uniform(1, check_interval))


if __name__ == "__main__":
    main()
