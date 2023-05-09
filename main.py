from flask import Flask, render_template, request
import pyautogui

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/left')
def left():
    pyautogui.press("prevtrack")
    return ''

@app.route('/right')
def right():
    pyautogui.press("nexttrack")
    return ''
@app.route('/up')
def up():
    pyautogui.press("volumeup")
    pyautogui.press("volumeup")
    return ''

@app.route('/down')
def down():
    pyautogui.press("volumedown")
    pyautogui.press("volumedown")
    return ''
@app.route('/tap')
def tap():
    pyautogui.press('playpause')
    return ''
pyautogui. FAILSAFE = False
pyautogui.PAUSE = 0
if __name__ == '__main__':
    app.run(host="0.0.0.0")