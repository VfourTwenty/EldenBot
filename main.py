import time
from helpers.win32_helpers import Win32Helpers

import mss
from PIL import Image
import pytesseract
import re


class Bot():
    def __init__(self):
        self.elden_ring_window = Win32Helpers.get_window('ELDEN RING™')

        self.soul_num = 0

    def check_window(self):
        activeWindow = Win32Helpers.get_active_window()
        return activeWindow == self.elden_ring_window

    def take_screenshot(self):
        new_soul_num = 0
        with mss.mss() as sct:
            # Define the region to capture (left, top, width, height)
            region = {"left": 1438, "top": 891, "width": 132, "height": 30}

            # Capture the specified region
            screenshot = sct.grab(region)

            # Save the screenshot to a file
            mss.tools.to_png(screenshot.rgb, screenshot.size, output="region_screenshot.png")

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img = Image.open('region_screenshot.png')

        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img)

        # Extract the number from the text
        new_soul_num = re.findall(r'\d+', text)

        if not new_soul_num or int(new_soul_num[0]) < self.soul_num:
            return False

        print(f'Soul balance: {int(new_soul_num[0])} gain = {int(new_soul_num[0]) - self.soul_num}')
        self.soul_num = int(new_soul_num[0])
        return True

        # screenshot #
        ##############

    def main(self):
        i = 0
        print("Waiting 5 seconds before starting...")
        time.sleep(5)
        print("starting")
        while self.check_window():
            Win32Helpers.pressAndHold('g')
            time.sleep(0.5)
            Win32Helpers.release('g')

            Win32Helpers.pressAndHold('s')
            time.sleep(0.1)
            Win32Helpers.release('s')

            Win32Helpers.pressAndHold('w')
            time.sleep(0.1)
            Win32Helpers.release('w')

            Win32Helpers.pressAndHold('enter')
            time.sleep(0.1)
            Win32Helpers.release('enter')
            time.sleep(0.5)
            Win32Helpers.pressAndHold('enter')
            time.sleep(0.1)
            Win32Helpers.release('enter')
            time.sleep(8)

            # teleport routine #
            ####################
            for j in range(30):
                if not self.take_screenshot():
                    time.sleep(0.1)
                else:
                    print(f"took a screenshot on the {j} attempt")
                    break

            else:
                print('Encountered a problem. Stopping.')
                return

            time.sleep(2)

            Win32Helpers.pressAndHold('w', 'd')
            time.sleep(1.9)
            Win32Helpers.release('d')
            time.sleep(0.8)
            Win32Helpers.release('w')

            Win32Helpers.pressAndHold('w')
            time.sleep(1.4)
            Win32Helpers.release('w')

            Win32Helpers.pressAndHold('a')
            time.sleep(0.3)
            Win32Helpers.release('a')
            time.sleep(19.15)

            Win32Helpers.pressAndHold('s','a')
            time.sleep(1.3)
            Win32Helpers.release('s')
            time.sleep(1.6)
            Win32Helpers.release('a')
            Win32Helpers.pressAndHold('w')
            time.sleep(1.2)
            Win32Helpers.release('w')
            time.sleep(0.3)

            Win32Helpers.pressAndHold('e')
            time.sleep(0.1)
            Win32Helpers.release('e')

            time.sleep(1)

            Win32Helpers.pressAndHold('e')
            time.sleep(0.1)
            Win32Helpers.release('e')
            time.sleep(2)
            Win32Helpers.click_mouse(150, 620)
            time.sleep(3.5)

            i += 1
            print(f"finished {i} runs", sep=' ')

        print("Stopped session because we're no longer in the right window")
        return


bot = Bot()
bot.main()
