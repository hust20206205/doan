import pyautogui


class MyView:
    def CloseTab():
        pyautogui.hotkey('ctrl', 'k')
        pyautogui.hotkey('ctrl', 'w')

    def Target(number):
        pyautogui.hotkey('alt', f'{number}')

    def CloseTerminal():
        pyautogui.hotkey('ctrl', 'j')

    def CloseScrollBar():
        pyautogui.hotkey('ctrl', 'shift', 'e')
        pyautogui.hotkey('ctrl', 'b')

    def CollapseFolders():
        pyautogui.hotkey('ctrl', 'shift', 'e')

        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')

    def OpenGit():
        pyautogui.hotkey('ctrl', 'shift', 'g')

    def OpenLatex():
        MyView.Target(2)
        pyautogui.hotkey('ctrl', 'alt', 'v')
