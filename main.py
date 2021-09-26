import os
import sys
import pandas as pd
import pyautogui
import time
from datetime import datetime

def startWemeetApp():
    work_dir = os.path.dirname(sys.argv[0])

    btn=pyautogui.locateCenterOnScreen(work_dir+"/renwulan.png")
    if btn == None:
        os.startfile("C:/Program Files (x86)/Tencent/WeMeet/wemeetapp.exe")
    else:
        clickImage(work_dir+"/renwulan.png")
    time.sleep(3)

def clickImage(image_path):
    btn=pyautogui.locateCenterOnScreen(image_path)
    print(image_path + ":" + str(btn))
    pyautogui.moveTo(btn)
    pyautogui.click()

def jiaRuHuiYi(meeting_id,password):
    startWemeetApp()

    joinbtn=pyautogui.locateCenterOnScreen("jiaruhuiyi.png")
    pyautogui.moveTo(joinbtn)
    pyautogui.click()
    time.sleep(1)

def kuaiSuHuiYi():
    work_dir = os.path.dirname(sys.argv[0])
    startWemeetApp()

    clickImage(work_dir+"/kuaisuhuiyi.png")
    time.sleep(1)

def jieShuHuiYi():
    work_dir = os.path.dirname(sys.argv[0])
    startWemeetApp()
    
    clickImage(work_dir+"/jieshuhuiyi1.png")
    time.sleep(1)
    clickImage(work_dir+"/jieshuhuiyi2.png")
    time.sleep(1)


#jiaRuHuiYi("meeting_id", "password")

kuaiSuHuiYi()
jieShuHuiYi()
