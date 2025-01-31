import sys
sys.path.append("../../")

import webbrowser
from threading import Timer
from app import app

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(host="127.0.0.1", port=5000, debug=False)

'''
This script is used for generating excutable files.
The following are some notes about How I worked for it.

1. How to make flaskwebgui work as expected:
    a. install flaskwebgui: `pip install flaskwebgui`
        - flaskwebgui github repo: https://github.com/ClimenteA/flaskwebgui
    b. add some scripts to keep server running while gui is running
        - see here: https://github.com/ClimenteA/flaskwebgui#install
        - I added the code in the static/index.js (find "keep_alive_server()")
    c. Then run: `python app_desktop.py`, the web browser will be automatically lauched for onnx-modifier

2. How to generate excutable files:
    a. For Windows:
        - Run `pyinstaller -F -n onnx-modifier -i ./static/favicon.png --add-data "templates;templates" --add-data "static;static" app_desktop.py`
            - see here: https://stackoverflow.com/a/48976223/10096987
        - Then we can find the our target `.exe` file in the ./dist folder.
            - The icon will not show until we change it in another directory due to Windows Explorer caching.
                - see here: https://stackoverflow.com/a/35783199/10096987

    b. For Ubuntu (not done):
        - Run `pyinstaller -F -n onnx-modifier -i ./static/favicon.png --add-data "templates:templates" --add-data "static:static" app_desktop.py`
            - However, I get a file with size of 400+MB

'''