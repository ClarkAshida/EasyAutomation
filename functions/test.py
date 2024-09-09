import pyautogui

local = pyautogui.locateOnScreen('assets/error_netnumen.png', confidence=0.9)
print(local)
pyautogui.click(local)
