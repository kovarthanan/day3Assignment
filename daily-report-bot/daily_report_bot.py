import pyautogui
import time
import pyperclip
from datetime import datetime
import os

# pyautogui.sleep(2);

pyautogui.press('win')
time.sleep(1)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)

pyautogui.write('https://www.nseindia.com/')
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

# 1. Copy data from Chrome (Chrome window must be active)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
data = pyperclip.paste()
data = " ".join(data.split())[:200]   # make it one line, keep it short

# 2. Open Excel and a blank workbook
pyautogui.press('win')
time.sleep(1)
pyautogui.write('excel')
time.sleep(1)
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('enter')
time.sleep(2)

# 3. Helper to put text in the current cell
def put(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('tab')            # move to next cell

# 4. Header row
put("Date & Time")
put("Fetched Data")
put("Comment")
pyautogui.press('enter')              # go to next row, column A

# 5. Data row
now = datetime.now().strftime("%d-%m-%Y")
put(now)
put(data)
put("Good for invesments today")
pyautogui.press('enter')



# 5b. Format the sheet
def ribbon(*keys):
    pyautogui.press('alt')
    time.sleep(0.3)
    for k in keys:
        pyautogui.press(k)
        time.sleep(0.3)

# Bold header (A1 to C1)
pyautogui.hotkey('ctrl', 'home')          # go to A1
pyautogui.hotkey('shift', 'right')
pyautogui.hotkey('shift', 'right')        # select A1:C1
pyautogui.hotkey('ctrl', 'b')             # bold
time.sleep(0.5)

# Column A: auto width
pyautogui.hotkey('ctrl', 'home')
pyautogui.hotkey('ctrl', 'space')         # select column A
ribbon('h', 'o', 'i')                     # AutoFit column width

# Column B: fixed width + wrap text (data is long)
pyautogui.press('right')
pyautogui.hotkey('ctrl', 'space')         # select column B
ribbon('h', 'o', 'w')                     # Column width box
pyautogui.write('60')
pyautogui.press('enter')
ribbon('h', 'w')                          # Wrap text

# Column C: auto width
pyautogui.press('right')
pyautogui.hotkey('ctrl', 'space')         # select column C
ribbon('h', 'o', 'i')

# Fit row heights so wrapped text shows fully
pyautogui.hotkey('ctrl', 'a')
ribbon('h', 'o', 'a')                     # AutoFit row height

pyautogui.hotkey('ctrl', 'home')          # back to A1
time.sleep(1)


filename = datetime.now().strftime("Report_%d-%m-%Y_%H-%M-%S.xlsx")
folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, filename)

pyautogui.press('f12')                # open Save As box
time.sleep(2)
pyperclip.copy(filepath)
pyautogui.hotkey('ctrl', 'v')         # paste full path
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)

shot_name = datetime.now().strftime("Screenshot_%d-%m-%Y_%H-%M-%S.png")
shot_path = os.path.join(folder, shot_name)

pyautogui.screenshot(shot_path)
print("Saved:", filepath)
print("Saved:", shot_path)

# 8. Close Excel
pyautogui.hotkey('alt', 'f4')       # Excel is the active window
time.sleep(2)

# 9. Close Chrome
# pyautogui.hotkey('alt', 'tab')      # switch back to Chrome
time.sleep(1)
pyautogui.hotkey('alt', 'f4')       # close that Chrome window