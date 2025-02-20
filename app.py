from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

# Function to get `top` command output
def get_top_output():
    try:
        output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
        return "<pre>" + output + "</pre>"
    except Exception as e:
        return f"Error fetching top output: {str(e)}"

@app.route('/htop')
def htop():
    full_name = "Sooraj S"  
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S IST')

    return f"""
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <h2>Top Command Output:</h2>
        {get_top_output()}
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)  