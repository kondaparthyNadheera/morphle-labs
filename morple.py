from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    name = "Kondaparthy Nadheera"
    username = "Nadheera-naidu"
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z%z")
    top_output = subprocess.getoutput("top -n 1 -b")
    response = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {ist_time}<br>
    <pre>{top_output}</pre>
    """
    return response

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
