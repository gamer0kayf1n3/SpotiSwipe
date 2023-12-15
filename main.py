from flask import Flask, render_template, request, jsonify
import pyautogui
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
sessions = AudioUtilities.GetAllSessions()
def vol(i):
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process:
            print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
            volume.SetMasterVolume(int(i)/100, None)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
@app.route('/slider')
def skdier():
    return render_template('volume.html')
@app.route('/volume', methods=["POST"])
def vols():
    data = request.get_json()
    volume = data.get('volume')
    # Here, you can handle the volume data as needed (e.g., store in a database, perform actions, etc.)
    vol(volume)
    return jsonify({'message': 'Volume received successfully'})

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