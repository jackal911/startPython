import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import hide_info

url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.implicitly_wait(10) # 페이지가 로딩될때까지 최대 10초 기다려줌
browser.maximize_window() # 화면 최대화
browser.get(url) # 페이지 열기

# 아이디 입력창
id = browser.find_element(By.CSS_SELECTOR, "#id")
# id.send_keys(id_pw.get_id)
id.click()
pyperclip.copy(hide_info.get_id())
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = browser.find_element(By.ID, "pw")
# pw.send_keys(id_pw.get_pw)
pw.click()
pyperclip.copy(hide_info.get_pw())
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
login_btn = browser.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()

# 메일함으로 이동
mail_url = "https://mail.naver.com/"
browser.get(mail_url) # 페이지 열기
time.sleep(2)

# 메일 쓰기 버튼 클릭
writeBtn = browser.find_element(By.CSS_SELECTOR, "#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault")
writeBtn.click()
time.sleep(2)

# 받는 사람 입력
receiveMan = browser.find_element(By.ID, "toInput")
receiveMan.send_keys(hide_info.get_receiveMan(), Keys.RETURN)
# pyautogui.write("januaryj@naver.com", 0.25)
# pyautogui.press("enter")
# pyautogui.press('tab')
# pyautogui.press('tab')

time.sleep(2)

# 제목 입력
# pyautogui.write("제목을 여기에 쓰자", 0.25) # pyautogui는 한글 지원 X
subject = browser.find_element(By.ID, "subject")
subject.send_keys("제목을 여기에 쓰자")
# pyperclip.copy('제목을 여기에 쓰자')
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('tab')
time.sleep(2)

# 내부 iframe 안으로 들어가기
iframe = browser.find_element(By.ID, 'se2_iframe')
browser.switch_to.frame(iframe)

# 내용 입력
browser.find_element(By.TAG_NAME, 'body').send_keys('내용은 여기에 쓰자')

'''
# JS로 해결
# browser.execute_script("document.querySelector('#se2_iframe').contentWindow.document.querySelector('body').innerHTML = '내용은 여기에 쓰자'")

# 키보드 제어
# pyautogui.write("내용은 여기에 쓰자", 0.25) # pyautogui는 한글 지원 X
# pyperclip.copy('내용은 여기에 쓰자')
# pyautogui.hotkey('ctrl', 'v')
'''

time.sleep(2)

# 메인프레임으로 다시 전환
browser.switch_to.default_content()

# 보내기 버튼 클릭
sendBtn = browser.find_element(By.ID, 'sendBtn')
sendBtn.click()