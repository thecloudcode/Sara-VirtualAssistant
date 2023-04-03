import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
import time
from time import sleep
import pyautogui

# to stop it from closing
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.codechef.com/")
driver.maximize_window()

# links = driver.find_elements("xpath","//a[@href]")
link=driver.find_elements("xpath","//button[@class='m-login-button-no-border']")
link[0].click()
sleep(4)

keyboard.write('the_cloud')
keyboard.press_and_release('tab')
keyboard.write('#BADboy17')
keyboard.press_and_release('enter')
sleep(7)

driver.get("https://www.codechef.com/practice")
for i in range(37):
    sleep(5)
    pyautogui.click(917, 400)
    sleep(5)
    # problem=driver.find_elements("id","MUIDataTableBodyRow-0")
    # problem[0].click()
    # options diff
    pyautogui.click(217, 567)
    sleep(3)
    # choose diff
    pyautogui.click(217, 380)
    sleep(5)
    # diff sort
    pyautogui.click(1317, 567)
    sleep(5)

    pyautogui.click(917, 625)
    sleep(4)
    # submit
    # pyautogui.click(1800, 980)
    # sleep(https://www.codechef.com/practice
    # )

    # # view others solution
    pyautogui.click(777, 70)
    sleep(3)
    pyautogui.click(777, 70)
    sleep(2)
    for i in range(107):
        keyboard.press_and_release("left arrow")
    sleep(1)
    for i in range(25):
        keyboard.press_and_release("right arrow")
    sleep(1)
    for i in range(8):
        keyboard.press_and_release("delete")
    sleep(1)
    keyboard.write('status')
    sleep(1)
    keyboard.press_and_release("enter")
    sleep(5)
    # for i in range(30):
    #     keyboard.press_and_release("down arrow")
    # pyautogui.click(1800, 857)
    # sleep(3)

    # lang
    pyautogui.click(300, 387)
    sleep(1)

    # select
    pyautogui.click(300, 447)
    sleep(2)

    # status
    pyautogui.click(400, 387)
    sleep(1)

    # correct
    pyautogui.click(400, 447)
    sleep(4)

    #link
    pyautogui.click(1600, 857)
    sleep(5)

    #answer-click
    pyautogui.click(777, 777)
    sleep(1)

    keyboard.press_and_release("ctrl+a")
    sleep(1)
    keyboard.press_and_release("ctrl+c")
    sleep(1)
    keyboard.press_and_release("ctrl+tab")
    sleep(3)
    # problem=driver.find_elements("id","MUIDataTableBodyRow-0")
    # problem[0].click()
    pyautogui.click(917, 625)
    sleep(5)

    # start of answer changing
    pyautogui.click(1200, 477)
    sleep(3)
    keyboard.press_and_release("ctrl+a")
    sleep(1)
    keyboard.press_and_release("ctrl+v")
    sleep(3)
    pyautogui.click(1800, 980)
    sleep(47)
    # keyboard.press_and_release("alt+F4")
    keyboard.press_and_release("ctrl+t")
    sleep(1)
    keyboard.press_and_release("ctrl+tab")
    sleep(1)
    keyboard.press_and_release("ctrl+w")
    sleep(1)
    keyboard.press_and_release("ctrl+w")
    sleep(1)
    keyboard.press_and_release("ctrl+w")
    sleep(1)
    keyboard.press_and_release("ctrl+w")
    sleep(2)
    pyautogui.click(777, 70)
    sleep(1)
    keyboard.write("https://www.codechef.com/practice")
    sleep(1)
    keyboard.press_and_release("enter")



# -------------------------------------------------------------------


#LINKEDIN



# gotosoln=driver.find_elements("")

# submit=driver.find_elements("xpath","//button[@class='_submit__btn_y21ua_156 _dark_y21ua_12']")
# print(submit)
# link[0].click()
# submit[0].click()
# problem[0].click()
# print(problem)
# practises=driver.find_elements("xpath","//a[@href]")
# for p in practises:
#     if "practice" in p.get_attribute("innerHTML"):
#         p.click()
#         break
# username = driver.find_elements("id","edit-name")
# username[0].click()


# for i in username:
    # print(i)
# username[0].send_keys('the_cloud')
# for link in links:
#     print(link.get_attribute("innerHTML"))

    # print(link)
    # if "Login" in link.get_attribute("innerHTML"):
    #     link.click()
    #     break