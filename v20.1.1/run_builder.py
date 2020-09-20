# -- this script runs a standalone lab.js builder in a local server.
# -- lab.js builder version: 20.1.1
import subprocess
import webbrowser
import os

os.chdir("./build")
#subprocess.Popen(['python', '-m', 'SimpleHTTPServer', '8000'])
subprocess.Popen(['python', '-m', 'http.server', '8000'])
webbrowser.open('http://localhost:8000',new=0,autoraise=True)
