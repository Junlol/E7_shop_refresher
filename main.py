from time import sleep as wait
import os
import keyboard
import pyautogui

# move mouse to the top left of the screen to trigger
pyautogui.FAILSAFE = True

# image folder path
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# what items to buy
buy_covenants = True
buy_mystics = True

# item buy button x & y offset
# adjust this to the click the buy button to the right of the item
button_add_x = 800  # higher value = further right
button_add_y = 20  # higher value = further down

# start delay
start_timer = 5

# count var
c = 0
m = 0

# flags
searching = True
scrolled = False
bought_c = False
bought_m = False

print(f"Running in {start_timer}...")
wait(start_timer)
# hold down q to end
while not keyboard.is_pressed('q') or not (buy_covenants and buy_mystics):

    in_shop = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "shop.png"), confidence=.90)

    if in_shop:

        # mystic bookmarks
        mystic = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "mystic_icon.png"), confidence=.90)

        # covenant bookmarks
        covenant = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "covenant_icon.png"), confidence=.90)

        # refresh button
        refresh_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "refresh_button.png"),
                                                        confidence=.90)

        if mystic and not bought_m and buy_mystics:
            wait(0.5)

            # print("Mystics Found --> Buying")

            # click the buy button to the right of the item
            mystic_buy_button_x, mystic_buy_button_y = mystic
            pyautogui.click(int(mystic_buy_button_x) + button_add_x, int(mystic_buy_button_y) + button_add_y,
                            button='left')

            wait(0.5)
            # find and click the confirm button
            mystic_confirm_buy_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, "mystic_buy_button"
                                                                                                   ".png"),
                                                                       confidence=.80)

            pyautogui.click(mystic_confirm_buy_button, button='left')

            # wait for the animation to play
            wait(3)

            # count
            bought_m = True
            m += 1

        if covenant and not bought_c and buy_covenants:
            wait(0.5)

            # print("Covenants Found --> Buying")

            # click the buy button to the right of the item
            covenant_buy_button_x, covenant_buy_button_y = covenant
            pyautogui.click(int(covenant_buy_button_x) + button_add_x, int(covenant_buy_button_y) + button_add_y,
                            button='left')

            wait(0.5)
            # find and click the confirm button
            covenant_confirm_buy_button = pyautogui.locateCenterOnScreen(
                os.path.join(images_folder, "covenant_buy_button.png"),
                confidence=.80)

            pyautogui.click(covenant_confirm_buy_button, button='left', clicks=2)

            # wait for the animation to play
            wait(3)

            bought_c = True
            # count
            c += 1

        # scroll
        if not scrolled:
            # scroll down
            pyautogui.scroll(-5000)

            # wait for animation to end
            wait(1)

            # reset flag
            scrolled = True

            # search again after scroll
            continue

        # quit searching
        searching = False

        # refresh the shop
        if not searching:
            # print("Refreshing...")

            # click refresh button
            wait(0.5)
            pyautogui.click(refresh_button, button='left', clicks=2)
            wait(1)

            # find and click refresh confirm button
            refresh_button_confirm = pyautogui.locateCenterOnScreen(
                os.path.join(images_folder, "confirm_refresh_button.png"),
                confidence=.90)
            pyautogui.click(refresh_button_confirm, button='left')

            wait(1)

            # reset flags
            searching = True
            scrolled = False
            bought_m = False
            bought_c = False

    # break if not in shop
    else:
        print("NOT IN SHOP")
        break

# print when loop ends
if c > 0 or m > 0:
    print(f"Covenants found {c * 5}\nMystics found {m * 50}")
