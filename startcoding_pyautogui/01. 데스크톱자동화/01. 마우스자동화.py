import time
import pyautogui

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 3. 마우스 이동
# pyautogui.moveTo(41, 442)
# pyautogui.moveTo(41, 442, 2)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다 하셈

# 5. 마우스 드래그
# 437,46 -> 275,47
pyautogui.moveTo(437, 46, 1)
pyautogui.dragTo(275, 47, 1)