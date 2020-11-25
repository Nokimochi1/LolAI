import time
import sys
import pyautogui
from pynput.keyboard import Key, Controller
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import os
import subprocess
import time

acceptButton    = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/acceptButton.png'
searchButton    = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/searchButton.png'
chatButton      = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/chatButton.png'
lockinButton    = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/lockinButton.png'
playButton      = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/playButton.png'
coopButton      = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/botsButton.png'
introButton     = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/introButton.png'
confirmButton   = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/confirmButton.png'
findMatchButton = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/fendmetch.png'
soraka          = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/sorakaPic.png'
lockChampButton = 'C://Users/warza/OneDrive/Pulpit/LeaugeOfLegendsBOT/Screenshots/lockChampion.png'


class findGame:

    @staticmethod
    def clickPlayButton():
        pos = imagesearch(playButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.clickPlayButton()

    @staticmethod
    def clickCoopButton():
        pos = imagesearch(coopButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.clickCoopButton()

    @staticmethod
    def clickIntroButton():
        pos = imagesearch(introButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.clickIntroButton()

    @staticmethod
    def clickConfirmButton():
        pos = imagesearch(confirmButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.clickConfirmButton()

    @staticmethod
    def clickFindMatchButton():
        time.sleep(2)
        pos = imagesearch(findMatchButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.clickFindMatchButton()

    @staticmethod
    def acceptGame():
        pos = imagesearch(acceptButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            findGame.acceptGame()


class championSelect:

    @staticmethod
    def choseChampion():
        pos = imagesearch(searchButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            pyautogui.typewrite("soraka")
        else:
            pos1 = imagesearch(acceptButton)
            if pos1[0] != -1:
                pyautogui.moveTo(pos1[0], pos1[1])
                pyautogui.click()
            championSelect.choseChampion()

    @staticmethod
    def clickChampion():
        time.sleep(1)
        pos = imagesearch(soraka)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            pos1 = imagesearch(acceptButton)
            if pos1[0] != -1:
                pyautogui.moveTo(pos1[0], pos1[1])
                pyautogui.click()
            championSelect.clickChampion()

    @staticmethod
    def lockChampion():
        pos = imagesearch(lockChampButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
        else:
            pos1 = imagesearch(acceptButton)
            if pos1[0] != -1:
                pyautogui.moveTo(pos1[0], pos1[1])
                pyautogui.click()
            championSelect.lockChampion()

    @staticmethod
    def nameRole():
        pos = imagesearch(chatButton)
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            pyautogui.click()
            pyautogui.typewrite("supp")
            pyautogui.press("enter")
            dodgedMain()
        else:
            pos1 = imagesearch(acceptButton)
            if pos1[0] != -1:
                pyautogui.moveTo(pos1[0], pos1[1])
                pyautogui.click()
            championSelect.nameRole()




def main():
    findGame.clickPlayButton()
    findGame.clickCoopButton()
    findGame.clickIntroButton()
    findGame.clickConfirmButton()
    findGame.clickFindMatchButton()
    findGame.acceptGame()
    championSelect.choseChampion()
    championSelect.clickChampion()
    championSelect.lockChampion()
    championSelect.nameRole()

def dodgedMain():
    findGame.acceptGame()
    championSelect.choseChampion()
    championSelect.clickChampion()
    championSelect.lockChampion()
    championSelect.nameRole()

    


if __name__ == "__main__":
    main()
