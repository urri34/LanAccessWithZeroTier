from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

ALLOWED_COMMANDS = {
    "list": ["ls", "-l"],
    "disk": ["df", "-h"],
    "restart_service": ["systemctl", "restart", "apache2"]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_command():
    cmd_key = request.form.get("command")
    if cmd_key in ALLOWED_COMMANDS:
        result = subprocess.run(ALLOWED_COMMANDS[cmd_key], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre><a href='/'>Tornar</a>"
    else:
        return "Comanda no permesa", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
